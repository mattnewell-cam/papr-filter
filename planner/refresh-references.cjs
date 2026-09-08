// Regenerate long-search reference scores after catalogue corrections.
const fs=require('node:fs'),path=require('node:path');
const {load,cases,solver}=require('./test-solver.cjs');
const source=fs.readFileSync(path.join(__dirname,'src.html'),'utf8');
const strong=load(source.replace(/generations=quick\?65:\(n>4\?\d+:\d+\)/,'generations=1200').replace(/Math.max\(\d+,orders.length\)/,'Math.max(10,orders.length)'));
const best=(sel,p=202,r=15,h=50,ri=null,q=3000)=>{
  solver.solve(sel,p,r,h,ri,q);
  return strong.solve(sel,p,r,h,ri,q,structuredClone(solver.seed()));
};
const refs=JSON.parse(fs.readFileSync(path.join(__dirname,'solver-reference.json'),'utf8'));
const update=m=>{const current=strong.mats.find(x=>x.id===m.id);if(!current)throw Error(m.id);return {...m,A:current.A,C:current.C,B:current.B,alpha:current.alpha,beta:current.beta,k:current.k,t:current.t,vlo:current.vlo,vhi:current.vhi};};
const standard=cases.map(([name,sel,...args])=>{const t=best(sel.map(update),...args);console.log(name,t.logs);return t.logs;});
for(const [i,r] of refs.entries()){const updated=r.args[0].map(update);const unchanged=JSON.stringify(updated)===JSON.stringify(r.args[0]);r.args[0]=updated;const t=best(...r.args);r.logs=unchanged?Math.max(r.logs,t.logs):t.logs;console.log('varied',i,r.logs);}
fs.writeFileSync(path.join(__dirname,'solver-reference.json'),JSON.stringify(refs,null,2)+'\n');
fs.writeFileSync(path.join(__dirname,'standard-reference.json'),JSON.stringify(standard,null,2)+'\n');
