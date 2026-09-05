#!/usr/bin/env python3
"""Validate Astra's task graph and scaffold a repository. Never starts workers."""
import argparse,hashlib,json,re,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def require(ok,msg):
 if not ok:raise ValueError(msg)
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def validate(plan):
 require(not re.search(r'REPLACE|OWNER/REPO',json.dumps(plan)), 'Replace every planning placeholder before validation/publication')
 require(re.fullmatch(r'[A-Za-z0-9_.-]+',plan['plan_id']), 'Use a simple stable plan ID')
 require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',plan['repository']),'Use an exact owner/repository')
 require(plan.get('delivery_branch'), 'Set the branch downstream issues will read')
 require(plan['visibility'] in ['private','public'],'Specify repository visibility')
 require(plan['mode']=='plan-first-manual-execution','Automatic dispatch is not supported')
 require(plan['planner']=='GPT-6 Astra','Planner must be Astra')
 require(plan.get('objective') and plan.get('sources') and plan.get('plan_id'),'Objective, source definitions and stable plan ID required')
 for s in plan['sources']:require(s.get('id') and s.get('location') and s.get('scope') and s.get('revision_or_identity'),'Specify exact sources, scope and revision/identity')
 nodes=plan['issues'];byid={n['id']:n for n in nodes};require(nodes and len(nodes)==len(byid),'Empty graph or duplicate issue IDs')
 for n in nodes:
  require(re.fullmatch(r'[A-Z0-9-]+',n['id']),'Use stable uppercase issue IDs')
  require(n['worker'] in ['GPT-5.6 Sol','GPT-5.6 Luna'],'Worker must be Sol or Luna')
  for key in ['title','goal','worker_reason','owned_paths','inputs','outputs','acceptance','verification','evidence']:
   require(n.get(key),n['id']+': missing '+key)
  for key in ['owned_paths','inputs','outputs','acceptance','verification','evidence']:
   require(isinstance(n[key],list) and all(isinstance(x,str) and x.strip() for x in n[key]),n['id']+': '+key+' must be a list of concrete strings')
  require(isinstance(n['depends_on'],list), 'depends_on must be a list')
  require(len(n['depends_on'])==len(set(n['depends_on'])) and all(d in byid and d!=n['id'] for d in n['depends_on']),n['id']+': invalid dependency')
  for path in n['owned_paths']:
   require(not Path(path).is_absolute() and '..' not in Path(path).parts,n['id']+': owned path must be repository-relative')
 order=[];todo=set(byid)
 while todo:
  ready=[n['id'] for n in nodes if n['id'] in todo and set(n['depends_on'])<=set(order)]
  require(ready,'Dependency graph contains a cycle');order.extend(ready);todo-=set(ready)
 # Unordered writers to overlapping paths are ambiguous even under manual execution.
 ancestors={}
 for nid in order:
  ancestors[nid]=set(byid[nid]['depends_on'])
  for d in byid[nid]['depends_on']:ancestors[nid]|=ancestors[d]
 def overlap(a,b):
  a=a.rstrip('/');b=b.rstrip('/');return a==b or a.startswith(b+'/') or b.startswith(a+'/')
 for i,a in enumerate(nodes):
  for b in nodes[i+1:]:
   if any(overlap(x,y) for x in a['owned_paths'] for y in b['owned_paths']):
    require(a['id'] in ancestors[b['id']] or b['id'] in ancestors[a['id']],'Overlapping writers need a dependency: '+a['id']+' / '+b['id'])
 return order

def issue_body(plan,n,links=None):
 links=links or {};lines=[f"<!-- learning-plan:{plan['plan_id']}:{n['id']} -->",'# Goal',n['goal'],'','# Execution',f"Recommended model: {n['worker']}",f"Delivery branch: {plan['delivery_branch']}",n['worker_reason'],'User launches this issue manually. Do not start another issue or switch models automatically.','','# Dependencies']
 lines += ['- '+links.get(d,d) for d in n['depends_on']] or ['None; this issue is initially ready.']
 lines += ['Verify prerequisite outputs are saved and reviewed at the expected repository revision; a closed issue alone is insufficient.','','# Source authority']
 for s in plan['sources']:lines += [f"- {s['id']}: {s['location']} | {s['revision_or_identity']} | scope: {s['scope']}"]
 lines += ['Read workflow/SKILL.md, workflow/WORKFLOW.md, and the repository AGENTS.md. Source facts and current user instructions govern the work.']
 for title,key in [('Inputs','inputs'),('Owned paths','owned_paths'),('Outputs','outputs'),('Acceptance criteria','acceptance'),('Verification','verification'),('Evidence required','evidence')]:
  lines += ['', '# '+title]+[('- [ ] ' if key=='acceptance' else '- ')+x for x in n[key]]
 lines += ['','# Completion and stop','Save only the scoped outputs using the repository delivery policy. Re-fetch remote files and compare with the intended content. Report exact output paths, commit/hash, checks, and any remaining uncertainty. Close only when all criteria pass and outputs are available downstream, if the user launch authorizes closure. Otherwise leave open. Stop after this issue.','','# Blocked or failed','Preserve partial work and state the exact missing source, dependency, failed criterion, or required decision. Do not broaden source scope, begin descendants, change the assigned model, or fabricate a pass.','']
 return '\n'.join(lines)

def scaffold(plan,dest):
 order=validate(plan);require(not dest.resolve().is_relative_to(ROOT.resolve()),'Place the scaffold outside the workflow folder');require(not dest.exists(),'Choose a new scaffold directory; existing repositories must be updated conservatively')
 dest.mkdir(parents=True);shutil.copytree(ROOT,dest/'workflow',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
 shutil.copytree(ROOT/'assets/project-template',dest/'project')
 (dest/'issue-drafts').mkdir();(dest/'.github/ISSUE_TEMPLATE').mkdir(parents=True)
 (dest/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
 (dest/'issue-map.json').write_text('{}\n')
 byid={n['id']:n for n in plan['issues']}
 for nid in order:(dest/'issue-drafts'/f'{nid}.md').write_text(issue_body(plan,byid[nid]),encoding='utf-8')
 rows=['# Plan','','Planner: GPT-6 Astra. Execution: one user-launched Sol/Luna issue at a time.','','| ID | Outcome | Model | Depends on |','|---|---|---|---|']
 rows += [f"| {nid} | {byid[nid]['title']} | {byid[nid]['worker']} | {', '.join(byid[nid]['depends_on']) or 'None'} |" for nid in order]
 (dest/'PLAN.md').write_text('\n'.join(rows)+'\n')
 (dest/'SOURCES.md').write_text('# Sources\n\n'+'\n'.join(f"- {s['id']}: {s['location']} — {s['revision_or_identity']} — {s['scope']}" for s in plan['sources'])+'\n')
 (dest/'README.md').write_text('# '+plan['repository'].split('/')[1]+'\n\n'+plan['objective']+'\n\nStart with PLAN.md and the linked GitHub issues. Planning does not start execution.\n\nUse workflow/GITHUB_ISSUES.md for manual launch and completion commands.\n')
 (dest/'AGENTS.md').write_text((ROOT/'assets/REPO_AGENTS.md').read_text())
 (dest/'.github/ISSUE_TEMPLATE/learning-task.md').write_text((ROOT/'assets/ISSUE_TEMPLATE.md').read_text())
 (dest/'.gitignore').write_text('**/__pycache__/\n**/*.pyc\n.venv/\nproject/sources/\nproject/pages/\nproject/media/\nproject/export/*.apkg\n.DS_Store\n')
 print(json.dumps({'repository':plan['repository'],'issue_order':order,'initially_ready':[n for n in order if not byid[n]['depends_on']],'status':'local scaffold ready; publish repository and issues using GITHUB_ISSUES.md; no workers launched'},indent=2))
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('plan',type=Path);p.add_argument('--scaffold',type=Path);args=p.parse_args()
 try:
  plan=read(args.plan)
  if args.scaffold:scaffold(plan,args.scaffold.resolve())
  else:print(json.dumps({'valid':True,'order':validate(plan)},indent=2))
 except (ValueError,KeyError) as e:p.exit(1,str(e)+'\n')
if __name__=='__main__':main()
