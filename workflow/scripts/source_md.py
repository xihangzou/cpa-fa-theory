#!/usr/bin/env python3
"""Prepare and validate source-image Markdown projects; no integration or Anki operations."""
import argparse, collections, hashlib, json, re, shutil, subprocess, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def require(ok, message):
    if not ok: raise ValueError(message)

def read(path): return json.loads(Path(path).read_text(encoding='utf-8'))

def write(path, obj):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def safe(root, relative):
    p = (root / relative).resolve()
    require(p.is_relative_to(root.resolve()), 'Path escapes project: '+str(relative))
    return p

def text(path): return Path(path).read_text(encoding='utf-8')

def ingest(project, source, source_id, dpi):
    from PIL import Image
    require(re.fullmatch(r'[A-Za-z0-9_-]+', source_id), 'Use a simple unique source ID.')
    manifest = read(project/'sources.json')
    require(source_id not in {s['id'] for s in manifest}, 'Source ID already exists; preserve existing edition.')
    require(dpi>=150, 'Use at least 150 DPI; default 300.')
    destination = project/'pages'/source_id
    require(not destination.exists(), 'Page directory already exists.')
    records=[]
    with tempfile.TemporaryDirectory() as temp:
        stage=Path(temp)
        if source.is_file() and source.suffix.lower()=='.pdf':
            require(shutil.which('pdftoppm') and shutil.which('pdfinfo'), 'Install Poppler: pdftoppm and pdfinfo.')
            info=subprocess.run(['pdfinfo',str(source)],check=True,capture_output=True,text=True).stdout
            count=int(re.search(r'^Pages:\s+(\d+)',info,re.M)[1])
            subprocess.run(['pdftoppm','-jpeg','-r',str(dpi),'-jpegopt','quality=95',str(source),str(stage/'page')],check=True,capture_output=True)
            files=sorted(stage.glob('page-*.jpg'),key=lambda p:int(p.stem.split('-')[-1]))
            require(len(files)==count, 'Rendered page count differs from PDF count.')
            original='sources/'+source_id+'.pdf'
            require(not (project/original).exists(), 'Original destination already exists.')
            (project/'sources').mkdir(exist_ok=True)
            shutil.copy2(source,project/original)
            source_record={'id':source_id,'kind':'pdf','original':original,'sha256':sha(project/original),'dpi':dpi}
        else:
            require(source.is_dir(), 'Input must be a PDF or a directory of page-NNN.jpg images. Export slides to PDF first.')
            files=list(source.iterdir())
            require(files and all(p.is_file() and re.fullmatch(r'page-[0-9]+\.jpg',p.name) for p in files), 'Image directory must contain only page-NNN.jpg files.')
            files.sort(key=lambda p:int(p.stem.split('-')[-1]))
            nums=[int(p.stem.split('-')[-1]) for p in files]
            require(len(nums)==len(set(nums)) and min(nums)>0, 'Duplicate or invalid page numbers.')
            source_record={'id':source_id,'kind':'images','original':'Provided page images; copied byte-for-byte','sha256':None,'dpi':None}
        destination.mkdir(parents=True)
        for file in files:
            number=int(file.stem.split('-')[-1]); target=destination/f'page-{number:03}.jpg'
            shutil.copy2(file,target)
            with Image.open(target) as im:
                im.verify()
            with Image.open(target) as im: width,height=im.size
            records.append({'id':f'{source_id}:{number:03}','pdf_page':number,'printed_page':None,'image':str(target.relative_to(project)),'sha256':sha(target),'width':width,'height':height,'disposition':'include','reason':''})
    source_record.update(edition='FILL IN title and edition',pages=records)
    manifest.append(source_record); write(project/'sources.json',manifest)
    print(f'Ingested {len(records)} pages. Verify orientation, legibility, edition, printed-page mapping, and exclusions.')

def source_check(project):
    sources=read(project/'sources.json'); tasks=read(project/'tasks.json')
    require(sources and tasks, 'Sources and tasks must be populated.')
    pages={}; ids=set(); used=collections.Counter(); chunks=set()
    for s in sources:
        require(s['id'] not in ids, 'Duplicate source ID'); ids.add(s['id'])
        require(s.get('edition') and 'FILL IN' not in s['edition'], 'Record the source title and edition.')
        if s['kind']=='pdf': require(sha(safe(project,s['original']))==s['sha256'],'Original PDF changed.')
        for page in s['pages']:
            pid=page['id']; require(pid not in pages,'Duplicate page ID: '+pid)
            require(sha(safe(project,page['image']))==page['sha256'],'Page changed: '+pid)
            require(page['disposition'] in ['include','exclude'],'Invalid page disposition')
            require(page['disposition']!='exclude' or page.get('reason'),'Excluded page needs reason')
            pages[pid]=page
    for task in tasks:
        tid=task['id']; require(tid not in chunks,'Duplicate task ID'); chunks.add(tid)
        expected=task['expected_pages']; processing=task.get('processing_pages',expected)
        require(expected and processing and len(expected)==len(set(expected)) and len(processing)==len(set(processing)),tid+': empty/duplicate page list')
        require(set(expected)<=pages.keys() and set(processing)<=set(expected),tid+': invalid page scope')
        require(all(pages[p]['disposition']=='include' for p in processing),tid+': processes excluded page')
        require(task['status']=='pass',tid+': source review not complete')
        path=safe(project,task['output']); require(path.is_file(),tid+': missing chunk')
        body=text(path)
        require(not re.search(r'\[要(?:画像|原本)確認|\[UNRESOLVED',body),tid+': unresolved source content')
        require('**' not in body,tid+': remove bold formatting from structured source Markdown')
        used.update(processing)
    require(all(used[p]==1 for p,v in pages.items() if v['disposition']=='include'), 'Included pages must belong to exactly one processing task (context-only pages may repeat in expected_pages).')
    return pages,tasks

def assembled(project):
    import yaml
    pages,tasks=source_check(project)
    chapters=collections.OrderedDict(); sections={}; chapter_titles={}; evidence=[]; previous_chapter=None
    for task in tasks:  # explicit order, never lexicographic filename order
        raw=text(safe(project,task['output']))
        match=re.match(r'\A---\r?\n(.*?)\r?\n---\r?\n',raw,re.S)
        require(match is not None,task['id']+': missing YAML metadata')
        meta=yaml.safe_load(match[1]); require(meta['id']==task['id'], 'Chunk ID does not match task')
        require(str(meta['chapter'])==str(task['chapter']), 'Chunk chapter does not match task')
        chapter=str(task['chapter'])
        require(chapter==previous_chapter or chapter not in chapters,'Tasks must be grouped in chapter reading order')
        previous_chapter=chapter; out=chapters.setdefault(chapter,[])
        # A section ID (not title text) determines whether a boundary heading is repeated.
        section=str(task['section']); seen=sections.setdefault(chapter,{})
        for line in raw[match.end():].splitlines(keepends=True):
            if line.startswith('# '):
                title=line.strip()
                if chapter in chapter_titles:
                    require(chapter_titles[chapter]==title,'Conflicting chapter titles'); continue
                chapter_titles[chapter]=title
            elif line.startswith('## '):
                title=line.strip()
                if section in seen:
                    require(seen[section]==title,'Conflicting section headings; split tasks per section'); continue
                seen[section]=title
            out.append(line)
        out.append('\n')
        evidence.append({'task':task['id'],'chunk_sha256':sha(safe(project,task['output'])),'processing_pages':task.get('processing_pages',task['expected_pages'])})
    require(set(chapters)==set(chapter_titles),'Each chapter must have a chapter heading')
    chapter_text={k:''.join(v).strip()+'\n' for k,v in chapters.items()}
    return chapter_text,'\n'.join(chapter_text.values()),evidence

def assemble(project):
    chapters,body,evidence=assembled(project)
    (project/'merged').mkdir(exist_ok=True)
    for i,(chapter,content) in enumerate(chapters.items()):
        (project/'merged'/f'chapter-{i:03}.md').write_text(content,encoding='utf-8')
    (project/'merged/textbook.md').write_text(body,encoding='utf-8')
    write(project/'merged/assembly.json',{'chapters':list(chapters),'chunks':evidence,'sha256':sha(project/'merged/textbook.md')})
    print('Merged without rewriting body text. Source revision: sha256:'+sha(project/'merged/textbook.md'))

def main():
 parser=argparse.ArgumentParser(description=__doc__); sub=parser.add_subparsers(dest='command',required=True)
 for name in ['init','check','assemble']:
  s=sub.add_parser(name); s.add_argument('project',type=Path)
 s=sub.add_parser('ingest');s.add_argument('project',type=Path);s.add_argument('source',type=Path);s.add_argument('--source-id',required=True);s.add_argument('--dpi',type=int,default=300)
 a=parser.parse_args();p=a.project.resolve()
 try:
  if a.command=='init':
   require(not p.exists(),'Choose a new project directory');shutil.copytree(ROOT/'assets/project-template',p)
   for d in ['sources','pages','chunks','merged']: (p/d).mkdir()
  elif a.command=='ingest':ingest(p,a.source.resolve(),a.source_id,a.dpi)
  elif a.command=='check':source_check(p);print('Source/task structural checks pass; image-to-text meaning requires review.')
  else:assemble(p)
 except (ValueError,KeyError,FileNotFoundError) as e:parser.exit(1,str(e)+'\n')
if __name__=='__main__':main()
