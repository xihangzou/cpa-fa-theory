#!/usr/bin/env python3
"""Publish a validated issue plan to an already-created repository; never execute issues."""
import argparse,json,re,subprocess
from pathlib import Path
import plan_repo as P

def gh(*args):
 return subprocess.run(['gh',*map(str,args)],check=True,capture_output=True,text=True).stdout.strip()
def publish(root):
 plan=P.read(root/'plan.json');order=P.validate(plan);repo=plan['repository']
 remote=json.loads(gh('repo','view',repo,'--json','nameWithOwner'))
 P.require(remote['nameWithOwner'].casefold()==repo.casefold(),'Repository mismatch')
 issues=json.loads(gh('issue','list','--repo',repo,'--state','all','--limit','10000','--json','number,title,body,url,state'))
 P.require(len(issues)<10000,'Issue listing reached its bound; use complete pagination before publication')
 byid={n['id']:n for n in plan['issues']};links={}
 for nid in order:
  marker=f"<!-- learning-plan:{plan['plan_id']}:{nid} -->"
  matching=[i for i in issues if marker in i['body']]
  P.require(len(matching)<=1,'Duplicate plan marker: '+nid)
  if matching:links[nid]=matching[0]['url']
  else:
   path=root/'issue-drafts'/f'{nid}.md';path.write_text(P.issue_body(plan,byid[nid],links),encoding='utf-8')
   url=gh('issue','create','--repo',repo,'--title',f"[{nid}] {byid[nid]['title']}",'--body-file',path)
   P.require(re.fullmatch(r'https://[^/]+/[^/]+/[^/]+/issues/[0-9]+',url),'Uncertain create response: re-list issues by stable marker before retrying')
   links[nid]=url
  (root/'issue-map.json').write_text(json.dumps(links,indent=2)+'\n')
 # A second pass resolves every prerequisite to a real issue link, then verifies readback.
 for nid in order:
  path=root/'issue-drafts'/f'{nid}.md';expected=P.issue_body(plan,byid[nid],links);path.write_text(expected,encoding='utf-8')
  current=json.loads(gh('issue','view',links[nid],'--repo',repo,'--json','title,body,url,state'))
  title=f"[{nid}] {byid[nid]['title']}"
  if current['body']!=expected or current['title']!=title:
   P.require(current['state']!='CLOSED','Closed issue contract changed: '+nid+'; have Astra explicitly reconcile the plan before updating it')
   gh('issue','edit',links[nid],'--repo',repo,'--title',title,'--body-file',path)
  actual=json.loads(gh('issue','view',links[nid],'--repo',repo,'--json','title,body,url,state'))
  P.require(actual['body']==expected and actual['title']==title,'Remote issue readback mismatch: '+nid)
 table=['# GitHub issue index','','| Issue | Model | Dependencies |','|---|---|---|']
 table += [f"| [{nid}]({links[nid]}) | {byid[nid]['worker']} | "+(', '.join(f'[{d}]({links[d]})' for d in byid[nid]['depends_on']) or 'None')+' |' for nid in order]
 (root/'ISSUES.md').write_text('\n'.join(table)+'\n',encoding='utf-8')
 return {'issues':links,'initially_ready':[links[n] for n in order if not byid[n]['depends_on']],'workers_started':0,'next':'Commit and push issue-map.json, ISSUES.md, and updated drafts; verify remote files, then hand off to user.'}
def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('repository_directory',type=Path);a=parser.parse_args()
 try:print(json.dumps(publish(a.repository_directory.resolve()),indent=2))
 except (ValueError,KeyError,subprocess.CalledProcessError) as e:parser.exit(1,str(e)+'\nNo workers launched. Re-list stable issue markers before retrying uncertain writes.\n')
if __name__=='__main__':main()
