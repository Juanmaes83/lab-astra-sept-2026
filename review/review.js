const model=document.querySelector('#model');
const toolbar=document.querySelector('.toolbar');
for(const [label,factor] of [['Zoom in',.8],['Zoom out',1.25]]){const button=document.createElement('button');button.textContent=label;button.onclick=()=>{const o=model.getCameraOrbit();model.cameraOrbit=`${o.theta}rad ${o.phi}rad ${o.radius*factor}m`;};toolbar.append(button);}
const cameraReadout=document.createElement('p');cameraReadout.id='camera-readout';cameraReadout.className='hint';model.after(cameraReadout);
model.addEventListener('camera-change',()=>{const o=model.getCameraOrbit();cameraReadout.textContent=`Camera: ${(o.theta*180/Math.PI).toFixed(1)}° azimuth · ${(o.phi*180/Math.PI).toFixed(1)}° elevation angle · ${o.radius.toFixed(2)} m distance`;});
model.addEventListener('load',()=>document.querySelector('#model-status').textContent='Actual GLB loaded — ready for inspection');
customElements.whenDefined('model-viewer').then(()=>{if(model.loaded)document.querySelector('#model-status').textContent='Actual GLB loaded — ready for inspection';});
model.addEventListener('error',()=>document.querySelector('#model-status').textContent='GLB failed to load. Check the download and network connection.');
document.querySelector('#reset').onclick=()=>{model.cameraOrbit='35deg 45deg 65m';model.cameraTarget='auto auto auto';model.fieldOfView='auto';model.jumpCameraToGoal();};
document.querySelector('#large').onclick=()=>{const active=document.querySelector('#inspection').classList.toggle('expanded');document.querySelector('#large').textContent=active?'Close large view':'Large view';};
document.addEventListener('keydown',e=>{if(e.key==='Escape'){document.querySelector('#inspection').classList.remove('expanded');document.querySelector('#large').textContent='Large view';}});
try{const r=await fetch('/asset-info.json');if(!r.ok)throw Error(r.status);const m=await r.json();document.querySelector('#metadata').textContent=`Objects: ${m.objects} · GLB: ${m.glbBytes.toLocaleString('en-US')} bytes · final scene reconfirmed from v04 .blend`;}catch{document.querySelector('#metadata').textContent='Metadata unavailable — consult the scene manifest.';}
try{const r=await fetch('/evidence/gate-2-solace/GATE-2-RESULT.md');if(!r.ok)throw Error(r.status);document.querySelector('#report').textContent=await r.text();}catch{document.querySelector('#report').textContent='Report unavailable. Use the evidence link.';}
