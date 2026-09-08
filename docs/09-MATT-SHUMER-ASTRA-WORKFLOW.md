# 09 — Matt Shumer Astra Workflow

Date adopted: 2026-09-08

Primary external workflow guide:

- Matt Shumer — **How to Build 3D Worlds with Astra**
- https://somethingbig.ai/3d-worlds

This document is the canonical production strategy for the SOLACE photoreal reconstruction benchmark unless a later explicit project decision supersedes it.

## Core production loop

```text
REFERENCE
→ ASSETS
→ ASSEMBLY
→ CRITIQUE
→ SHIP
```

The LAB must not treat an agent-produced MP4, render, GLB or `.blend` as success merely because the file exists.

The target is visual fidelity against a specific reference.

## 1. Reference is the authority

Astra must anchor on supplied real reference media instead of inventing a plausible generic scene.

For SOLACE, authority order is:

1. `references/solace/video/VIDEO_REFERENCIA_SOLACE_CINEMATIC_TARGET.mp4` — authoritative cinematic target;
2. verified source plan / floorplan — spatial/topological constraint;
3. other supplied SOLACE stills / boards — material, architecture and detail support;
4. `VIDEO_REFERENCIA_SOLACE_BLENDER_PROCESS.mp4` — process support only, never visual authority;
5. previous LAB renders — implementation history only, never truth.

If source evidence conflicts with a previous generated scene, source evidence wins.

## 2. Goal mode, not micro-gates

For a production benchmark, use `/goal` and define the human goal once.

Do not split the user-facing workflow into dozens of approval gates.

Astra may internally iterate many times, but the user should receive one coherent production result unless a real blocker requires intervention.

The active human goal for SOLACE is:

> Reconstruct the first continuous SOLACE cinematic shot at photoreal quality so that camera choreography, visible architecture, furnishings, materials, lighting and atmosphere are recognizably aligned with the real reference.

File existence is not the stopping condition.

## 3. Fan out to specialized workers

A single builder holding the entire scene in one context tends to cut corners.

When supported by the active Astra environment, fan out specialized workers with clear ownership. For the SOLACE shot, preferred domains are:

- reference / shot analysis;
- camera + lens + timing;
- architectural shell + openings;
- living furniture / hero sofa + library;
- dining furniture + fixtures;
- kitchen cabinetry + island + appliances;
- materials / surface imperfections;
- glazing + exterior vegetation;
- lighting / exposure / atmosphere;
- render / compositing / finishing;
- independent visual critic.

Workers own fidelity of their domain and must not silently substitute primitive placeholder quality for hero-visible assets.

## 4. Blender is an asset-production tool, not a primitive-generator shortcut

Astra may use Blender Python/headless workflows, MCP and procedural generation, but procedural does not mean low-detail.

Hero-visible assets must receive enough geometric and material complexity to survive close cinematic framing.

Primitive cubes/cylinders are acceptable for hidden structure, proxy blocking or early internal previews only.

For final visible assets, use the best available path consistent with the environment and project constraints:

- high-quality procedural Blender modeling;
- Blender-native modeling/sculpting/modifiers;
- physically plausible materials and baked/detail maps;
- approved asset/model sources when explicitly allowed;
- available Blender MCP asset/model-generation capabilities when appropriate.

Do not assume that simply increasing Cycles samples can compensate for weak geometry or weak materials.

## 5. Builder must not grade its own homework

The builder that creates an asset or scene is not the final evaluator.

Use a fresh-context critic whenever supported.

### Photo / frame test

For camera checkpoints and hero frames:

1. render the generated view;
2. pair it with the corresponding real reference frame;
3. normalize presentation where practical: resolution, crop, compression, metadata and filenames;
4. present them blind/shuffled to a fresh critic;
5. ask which one is the real reference and why;
6. convert every visual tell into a concrete work order;
7. send those work orders back to the relevant builder worker;
8. repeat until material visual differences are no longer obvious or a real technical/budget blocker is reached.

The critic should be harsh. “Looks good” is not useful feedback.

## 6. Camera is a measured reconstruction problem

For SOLACE, the cinematic target controls camera choreography.

Known benchmark facts for the first shot:

- first continuous shot: approximately `00:00.000 → 00:13.967`;
- hard cut begins at approximately `00:14.000`;
- source cadence: 30 fps;
- target proof: 14.0 s / 420 frames / 1920×1080 delivery;
- useful active picture is 16:9; do not reproduce player UI / recording borders.

Camera must be solved against source frames, not described as “manually inferred” and accepted without comparison.

Recommended anchor times:

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

At each anchor, compare screen-space positions of stable landmarks such as glazing mullions, library, sofa silhouette, dining table, island, rear windows and tall kitchen units.

## 7. Critique becomes work orders

Every visible mismatch should be expressed as an actionable correction, for example:

```text
OBSERVED TELL:
Sofa reads as three beveled boxes rather than upholstered furniture.

WORK ORDER:
Living-furniture worker: rebuild sofa silhouette with believable cushion deformation, seams, seat depth, arm/back construction and textile response while preserving source-relative dimensions and screen position.
```

Do not respond to criticism with generic “polish more”.

## 8. Internal iteration vs human approval

Internal Astra iteration is allowed and expected for reversible scene-building work.

Human approval remains required before:

- merge;
- destructive overwrite of important source work without a saved version;
- external publication beyond already approved review channels;
- permissions/secrets changes;
- paid services outside the already approved model/tool budget.

Juanma + ChatGPT perform the final human visual sign-off. Astra must not mark a cinematic benchmark as HUMAN PASS.

## 9. Cost discipline

The Matt Shumer workflow is allowed to spend more compute/tokens on the actual photoreal benchmark than the previous POC workflow, because fidelity is now the test.

Still avoid expensive work that does not increase visual fidelity:

- repeating setup checks already proven;
- rebuilding viewers;
- long prose reports;
- re-documenting old gates;
- refining invisible property areas;
- running unrelated product tasks.

Spend the budget on reference analysis, assets, camera, materials, lighting, rendering and critique.

## 10. SOLACE current interpretation

`SOLACE_VIDEO_PROOF_v01` and `v02` are useful historical proofs but are **not accepted photoreal outputs**.

They proved:

- Astra can control Blender;
- the floorplan can become a recognizable spatial blockout;
- a continuous Living → Dining → Kitchen video can be rendered.

They did not prove:

- photoreal fidelity;
- reference-matched camera timing;
- hero-asset quality;
- premium material/light quality;
- blind-test realism.

The next execution must therefore be a reference-first photoreal reconstruction goal, not another infrastructure gate.

## 11. Ship rule

For the SOLACE cinematic benchmark, `SHIP` means:

- authoritative target video used;
- 14-second shot reproduced at correct cadence;
- camera/frame progression recognizably matches source;
- hero-visible architecture and assets no longer read as blockout primitives;
- materials, glazing, vegetation and lighting support a premium architectural image;
- independent critique loop has produced and resolved material work orders;
- final `.blend` and MP4 are versioned and pushed;
- final human visual review remains pending until Juanma + ChatGPT approve it.

## External source note

This LAB treats Matt Shumer's 2026 article as its primary external production-method reference. The article is a workflow guide, not a source of SOLACE ground truth; SOLACE visual truth continues to come from the project-owned/source reference media.