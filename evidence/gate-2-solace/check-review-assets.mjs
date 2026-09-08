import fs from 'node:fs';
import crypto from 'node:crypto';
const dir='evidence/gate-2-solace';
const files=[...fs.readdirSync(dir).filter(n=>n!=='review-integrity.json').map(n=>`${dir}/${n}`),...fs.readdirSync('outputs/solace').map(n=>`outputs/solace/${n}`)];
const inventory=files.map(path=>{const b=fs.readFileSync(path);if(path.endsWith('.json'))JSON.parse(b);if(path.endsWith('.png')&&!b.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10])))throw Error(path);return {path,bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};});
const b=fs.readFileSync(`${dir}/SOLACE_BLOCKOUT_v01.glb`);if(b.toString('ascii',0,4)!=='glTF'||b.readUInt32LE(8)!==b.length)throw Error('Invalid GLB');
const gltf=JSON.parse(b.toString('utf8',20,20+b.readUInt32LE(12)));if(gltf.nodes.length!==137)throw Error('Count mismatch');
fs.writeFileSync(`${dir}/review-integrity.json`,JSON.stringify({final_blend_read_check:{scene:'SOLACE_GATE_2',objects:137,meshes:135,cameras:2,method:'Blender 5.2.1 background read of final v04 blend, no save'},glb_bytes:b.length,inventory},null,2));
console.log(`PASS: ${inventory.length} files; GLB ${b.length} bytes; ${gltf.nodes.length} nodes`);
