# AGENTS.md

## Mission

Build reference-grounded spatial/cinematic outputs that prove real visual capability, not merely tool connectivity or file production.

For the active SOLACE benchmark, the production method is:

```text
REFERENCE → ASSETS → ASSEMBLY → CRITIQUE → SHIP
```

Canonical strategy:

`docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`

Primary external guide:

https://somethingbig.ai/3d-worlds

## Current model state

- Current execution model: `gpt-6-astra` through Codex CLI.
- Astra access is confirmed on the project owner's Windows machine.
- Blender 5.2.1 LTS + Blender MCP are operational.
- Keep the workflow model-swappable; no architecture contract may depend permanently on Astra.
- Never claim Astra is active unless the active Codex session reports `gpt-6-astra`.

## Closed historical gates

Gate 1 / Blender MCP connectivity is CLOSED.

SOLACE floorplan/blockout proof is also complete as a spatial capability proof.

Do NOT repeat setup, Gate 1, test-cube work, blockout existence checks, viewer QA or other historical infrastructure tasks unless an actual regression blocks the current goal.

## Current active goal

**SOLACE PHOTOREAL CINEMATIC RECONSTRUCTION**

Target:

- authoritative source: `references/solace/video/VIDEO_REFERENCIA_SOLACE_CINEMATIC_TARGET.mp4`;
- first continuous shot approximately `00:00.000 → 00:13.967`;
- hard cut at approximately `00:14.000`;
- 30 fps;
- Living → Dining → Kitchen;
- visually premium, reference-grounded reconstruction.

`SOLACE_VIDEO_PROOF_v01` and `v02` are historical technical proofs only. They are not accepted photoreal outputs.

## Goal-mode execution

For this benchmark, use `/goal` when supported.

Do not stop merely because:
- a `.blend` exists;
- an MP4 exists;
- Blender rendered without error;
- the sequence generally travels Living → Dining → Kitchen.

Stop only when:
- the reference-driven quality bar is materially met; or
- a real technical / policy / approved-budget blocker requires human intervention.

Do not expose dozens of internal micro-gates to the user. Internal iteration is expected.

## Reference rules

Reference truth order:

1. authoritative SOLACE cinematic target;
2. verified source plan / floorplan;
3. supplied SOLACE still references;
4. Blender/process reference as process support only;
5. generated LAB outputs as implementation history only.

Never let a previous generated scene overrule real source evidence.

## Specialized workers

When the active environment supports sub-agents/workers, fan out focused ownership rather than having one builder cut corners across the full scene.

Preferred SOLACE domains:

1. reference + frame analysis;
2. camera / lens / timing;
3. architecture + openings;
4. living hero assets;
5. dining hero assets;
6. kitchen hero assets;
7. materials + surface imperfections;
8. glazing + exterior + vegetation;
9. lighting + exposure + atmosphere;
10. render / finishing;
11. independent visual critic.

Each worker is responsible for visual fidelity of its domain.

## Builder / critic separation

The builder must not grade its own work.

Use a fresh-context critic when supported.

For significant reference checkpoints:
- pair the real reference frame with the generated render;
- normalize presentation where practical;
- blind/shuffle them;
- ask the critic which is the real reference and why;
- translate every visible tell into a concrete work order;
- send the work order to the responsible builder;
- iterate.

The critic must be demanding. Generic praise is not acceptance evidence.

## Blender rules

- Prefer Safe Mode for agent-driven Blender execution.
- Save/version `.blend` before major mutations.
- Use Blender/Python procedurally when useful, but procedural does not justify primitive hero assets.
- Cubes/cylinders are acceptable for hidden structure and internal proxies; hero-visible final assets require credible geometry/material response.
- Do not assume more render samples can fix weak geometry/materials.
- Preserve useful existing work from v02 where it accelerates fidelity; do not rebuild blindly from zero.
- Camera must be measured against source frames, not simply described as manually inferred.

## Camera reconstruction rule

Use source-frame checkpoints around:

```text
0.0 s
2.0 s
4.0 s
6.0 s
8.0 s
10.0 s
12.0 s
13.8 s
```

Compare stable screen-space landmarks: glazing, library, sofa, dining table, island, rear windows and tall kitchen units.

The first shot target is 14.0 s at 30 fps / 420 frames for review delivery.

## Cost discipline

Astra is expensive. Spend its budget on the differential 3D work that improves the benchmark:

- reference analysis;
- camera reconstruction;
- asset modeling;
- materials;
- lighting;
- rendering;
- independent critique and correction.

Do not spend Astra tokens on:
- repeated setup checks;
- viewer/Vercel housekeeping;
- long documentation reports;
- unrelated PROJECT-PELU work;
- refining invisible property areas;
- work ChatGPT + Juanma can do outside Blender.

## Human approval gates

Stop before:
- merging;
- destructive overwrite of important source data without saved version;
- publishing externally beyond already approved review channels;
- changing permissions/secrets;
- paid external-service usage outside the already approved tool/model budget.

Final human visual acceptance belongs to Juanma + ChatGPT.

Astra must report `HUMAN VISUAL REVIEW: PENDING`, never self-approve the cinematic benchmark.

## PROJECT-PELU handoff rules

- This LAB produces; PROJECT-PELU consumes.
- Do not duplicate PROJECT-PELU runtime, hotspots, analytics or commercial logic here.
- Only human-`ACCEPTED` assets may be handed off.
- Preserve provenance and source manifests.
- F1 panorama fallback remains owned by PROJECT-PELU.

## Geospatial rules

- Target recognizability and coherent geography, not survey/BIM accuracy unless sources support it.
- Use open/owned geodata for editable geometry.
- Keep Google Photorealistic 3D Tiles as separate compliant visualization/human reference.
- Do not extract, trace or machine-derive owned geometry from Google Map Tiles content.

## Scope discipline

Do not expand to unrelated Unreal/geospatial/world-building work until the active SOLACE photoreal benchmark has a clear result or an explicit strategy decision changes priority.

## Completion evidence

A production goal is reviewable when it leaves:
- versioned `.blend`;
- final MP4/render;
- relevant source/reference mapping;
- concise record of critic findings / work orders resolved;
- commit SHA;
- explicit `HUMAN VISUAL REVIEW: PENDING`.

Do not create evidence bureaucracy that does not improve visual decision-making.

## Reporting

Keep final Astra reporting concise:
1. result path(s);
2. technical facts;
3. commit SHA;
4. unresolved material limitations;
5. human visual review pending.