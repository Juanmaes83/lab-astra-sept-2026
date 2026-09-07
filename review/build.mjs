import fs from 'node:fs';
const assets=['references/solace/HRUOGWHaMAATXEa.jpg','evidence/gate-2-solace/03-top-verified.png','evidence/gate-2-solace/04-perspective-verified.png','evidence/gate-2-solace/SOLACE_BLOCKOUT_v01.glb','evidence/gate-2-solace/GATE-2-RESULT.md','evidence/gate-2-solace/scene_manifest.json','evidence/gate-2-solace/source_manifest.json'];
for(const file of assets){fs.mkdirSync(`dist/${file.substring(0,file.lastIndexOf('/'))}`,{recursive:true});fs.copyFileSync(file,`dist/${file}`);}
fs.mkdirSync('dist/vendor',{recursive:true});
fs.copyFileSync('node_modules/@google/model-viewer/dist/model-viewer.min.js','dist/vendor/model-viewer.min.js');
fs.copyFileSync('node_modules/@google/model-viewer/LICENSE','dist/vendor/LICENSE-model-viewer');
for(const file of ['index.html','review.css','review.js'])fs.copyFileSync(`review/${file}`,`dist/${file}`);
const manifest=JSON.parse(fs.readFileSync(assets[5]));
fs.writeFileSync('dist/asset-info.json',JSON.stringify({objects:manifest.object_count,glbBytes:fs.statSync(assets[3]).size}));
console.log('Review build complete; actual evidence assets copied without transformation.');
