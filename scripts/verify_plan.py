#!/usr/bin/env python3
"""Validate planning coverage and contracts; never ingest or convert sources."""
import argparse,collections,hashlib,importlib.util,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def require(ok,msg):
 if not ok:raise ValueError(msg)
def validate(setup_only=False):
 spec=importlib.util.spec_from_file_location('planner',ROOT/'workflow/scripts/plan_repo.py');P=importlib.util.module_from_spec(spec);spec.loader.exec_module(P)
 plan=read(ROOT/'plan.json');order=P.validate(plan);nodes={n['id']:n for n in plan['issues']}
 catalog=read(ROOT/'contracts/source-catalog.json');pageplan=read(ROOT/'contracts/page-plan.json')
 require(len(catalog)==6 and len(pageplan['books'])==6,'Expected six sources')
 source_by_id={b['id']:b for b in catalog};counts={}
 required=['README.md','AGENTS.md','PLAN.md','SOURCES.md','contracts/CONTENT_RULES.md','contracts/RECORDS.md','contracts/DELIVERY.md','workflow/GITHUB_ISSUES.md','workflow/scripts/publish_issues.py','.github/ISSUE_TEMPLATE/learning-task.md','planning/baseline.json']
 for p in required:require((ROOT/p).is_file(),'Missing '+p)
 total=0
 for bp in pageplan['books']:
  bid=bp['source_id'];b=source_by_id[bid];count=b['physical_page_count'];total+=count
  images=b['images'];nums=[x['physical_page'] for x in images]
  require((bid=='CS' and not images) or sorted(nums)==list(range(1,count+1)),bid+': image sequence mismatch')
  require(re.fullmatch('[a-f0-9]{64}',b['pdf_sha256']),bid+': invalid PDF hash')
  if images:
   digest=hashlib.sha256(json.dumps(images,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
   require(digest==b['image_inventory_sha256'],bid+': image inventory digest mismatch')
   for f in images:require(re.fullmatch('[a-f0-9]{64}',f['sha256']),bid+': invalid image hash')
  body=set();chapkeys=[]
  for c in bp['chapters']:
   ps=set(range(c['start'],c['end']+1));require(not body&ps,bid+': chapter overlap');body|=ps;chapkeys.append(c['key'])
  meta=set(bp['metadata_only_candidate_pages'])
  require(body.isdisjoint(meta) and body|meta==set(range(1,count+1)),bid+': unaccounted physical page')
  owners=collections.Counter();batchids=[]
  for u in bp['batches']:
   uid=u['id'];n=nodes[uid];batchids.append(uid)
   require(1<=u['end']-u['start']+1<=24,uid+': unbounded conversion range')
   expected=[f'{bid}:{x:03}' for x in range(u['start'],u['end']+1)]
   require(u['expected_pages']==expected and n['physical_ranges']==[[u['start'],u['end']]],uid+': issue/range mismatch')
   require(n['source_id']==bid and n['batch_id']==uid,uid+': source mismatch')
   owners.update(range(u['start'],u['end']+1))
   require('JPG-000' in n['depends_on'] and f'JPG-{bid}-INV' in n['depends_on'],uid+': prerequisite absent')
   require(u['pilot'] or f'JPG-{bid}-PILOT-QA' in n['depends_on'],uid+': bulk not gated')
   if bid.startswith('W') and u['chapters'][0]['key']!='00':
    require(u['start']%2==0 and u['end']%2==1,uid+': question/answer page-pair split')
  require(set(owners)==body and all(x==1 for x in owners.values()),bid+': page ownership gap/overlap')
  chapter_qas=collections.Counter(k for q in bp['chapter_qa_groups'] for k in q['chapter_keys'])
  require(set(chapter_qas)==set(chapkeys) and all(x==1 for x in chapter_qas.values()),bid+': chapter QA ownership incomplete')
  asm=nodes[f'JPG-{bid}-ASSEMBLE'];require(set(asm['depends_on'])=={q['id'] for q in bp['chapter_qa_groups']},bid+': assembly gate incomplete')
  for uid in batchids:require((ROOT/'issue-drafts'/f'{uid}.md').is_file(),uid+': missing issue draft')
  if setup_only:
   project=ROOT/'project'/bid
   require(read(project/'sources.json')==[] and read(project/'tasks.json')==[],bid+': setup began inventory/conversion')
   require(set(p.name for p in project.iterdir())=={'README.md','sources.json','tasks.json'},bid+': unexpected production output')
  counts[bid]={'physical_pages':count,'candidate_body_pages':len(body),'metadata_only_candidate_pages':len(meta),'conversion_batches':len(batchids),'chapter_records':len(chapkeys),'chapter_qa_issues':len(bp['chapter_qa_groups'])}
 require(total==2108,'Source total mismatch')
 require(set(nodes['JPG-HANDOFF']['depends_on'])=={f'JPG-{b["id"]}-ACCEPT' for b in catalog},'Corpus handoff gate incomplete')
 # Original copied rules/helpers are unchanged during setup. Future JPG-000 can update only its scoped helper.
 for f in read(ROOT/'workflow/provenance.json'):
  if not setup_only and f['repository_path']=='workflow/scripts/source_md.py':continue
  require(hashlib.sha256((ROOT/f['repository_path']).read_bytes()).hexdigest()==f['sha256'],'Copied workflow changed: '+f['repository_path'])
 if setup_only:
  forbidden={'.pdf','.jpg','.jpeg','.png','.apkg','.colpkg'}
  for p in ROOT.rglob('*'):
   if '.git' in p.parts:continue
   require(not (p.is_file() and p.suffix.lower() in forbidden),'Raw source/media in scaffold: '+str(p.relative_to(ROOT)))
 require(not (ROOT/'.github/workflows').exists(),'Unexpected automated workflow')
 return {'status':'PASS','plan_id':plan['plan_id'],'revision':plan['revision'],'issue_count':len(nodes),'ready':[nid for nid in order if not nodes[nid]['depends_on']],'sources':counts,'total_physical_pages':total,'production_checked_absent':setup_only,'semantic_conversion_reviewed':False}
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--setup-only',action='store_true');args=parser.parse_args()
 print(json.dumps(validate(args.setup_only),ensure_ascii=False,indent=2))
