# 04 — Benchmarks and QA

## Benchmark A — SOLACE

Purpose: prove that Astra + Blender can reconstruct a specific premium architectural cinematic reference, not merely create a plausible walkthrough.

Primary external methodology:

- Matt Shumer — https://somethingbig.ai/3d-worlds
- LAB adaptation — `docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`

## Available SOLACE reference types

- verified floorplan / concept plan;
- supplied visual stills / boards where available;
- authoritative cinematic target video;
- Blender/process support video;
- existing historical blockout and video proofs.

Authoritative cinematic target:

`references/solace/video/VIDEO_REFERENCIA_SOLACE_CINEMATIC_TARGET.mp4`

Process support only:

`references/solace/video/VIDEO_REFERENCIA_SOLACE_BLENDER_PROCESS.mp4`

## First production slice

Living + Dining + Kitchen.

Target first continuous shot:

```text
approximately 00:00.000 → 00:13.967
hard cut at approximately 00:14.000
30 fps
14.0-second / 420-frame review target
1920×1080 delivery
```

## Historical proof status

### G0 — Agent runtime
PASS.

### G1 — Blender connectivity
PASS.

### G2 — Bounded closed loop
PASS.

### G3 — SOLACE spatial blockout
PASS as a spatial capability proof.

### Previous visual proof v01/v02
Produced, but **NOT ACCEPTED** as photoreal cinematic reconstruction.

Do not repeat G0–G3 unless a real regression appears.

## Active benchmark — Photoreal reconstruction

The active benchmark is no longer a chain of user-facing micro-gates.

Run one production goal:

```text
REFERENCE
→ SPECIALIZED ASSETS
→ ASSEMBLY
→ RENDER
→ INDEPENDENT CRITIQUE
→ WORK ORDERS
↺
→ SHIP
→ HUMAN REVIEW
```

## Reference fidelity dimensions

The final human review considers at least:

### 1. Camera / choreography
- source timing;
- camera height;
- lens / FOV;
- path;
- yaw / pitch;
- easing;
- framing progression;
- correct temporal handoff Living → Dining → Kitchen.

### 2. Spatial / architectural fidelity
- visible wall/opening relationships;
- glazing location and proportions;
- ceiling/floor relationships;
- library / doorway / rear-window placement;
- dining and kitchen adjacency;
- island/window/tall-unit relationships.

### 3. Hero asset fidelity
Hero-visible objects must not read as crude blockout primitives.

Priority:
- living sofa + cushions;
- coffee table / chair;
- built-in library;
- dining table + chairs + pendant;
- kitchen island;
- cabinetry / appliances / worktops;
- glazing / frames.

### 4. Materials
- timber character and variation;
- plaster / wall response;
- stone;
- fabric;
- metal;
- glazing;
- physically plausible roughness/specular behavior;
- appropriate microdetail / imperfections.

### 5. Exterior / vegetation
- visible forest/courtyard depth;
- believable foliage silhouette and density;
- no empty generic background;
- exterior color/brightness relationship consistent with source.

### 6. Lighting / atmosphere
- warm premium interior;
- cooler/darker exterior;
- depth and contact shadows;
- controlled highlights;
- realistic light falloff;
- integrated architectural lighting;
- no flat ambient wash.

### 7. Render / finishing
- sufficient sampling/denoising for evaluation;
- no obvious geometry clipping;
- no temporal flicker that masks comparison;
- no invented object motion unsupported by source;
- final grade/contrast adequate for source comparison.

## Camera frame checkpoints

Use source-matched checkpoint renders around:

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

Compare stable screen-space landmarks at each checkpoint.

A camera path is not accepted simply because it is smooth.

## Independent critic rule

The builder must not be the final evaluator of its own render.

When supported, a fresh-context critic should receive a blind/shuffled pair:

- real source frame;
- generated render of the same checkpoint.

Normalize crop/resolution/compression where practical and remove metadata/filename clues.

Ask one hard question:

> Which image is the real reference, and what visual tells reveal the generated one?

Every tell becomes a concrete work order owned by the relevant specialist.

Examples:

```text
TELL:
Dining chairs read as beveled blocks.

WORK ORDER:
Dining worker: rebuild chair silhouette, seat/back thickness, frame geometry and material response to match the source at 8–10 s.
```

```text
TELL:
At 6 s the sofa leaves frame too early.

WORK ORDER:
Camera worker: retime/reposition the 4–8 s segment using the real 6 s frame as the screen-space anchor.
```

## Production stop rule

Astra may internally iterate without human approval for reversible Blender work.

Do not stop because:
- a render completed;
- a video file exists;
- the builder says it is good;
- an average similarity description sounds positive.

Stop when:
- major tells have been resolved enough to produce a serious human-review candidate; or
- a real technical/policy/budget blocker needs human intervention.

## Human visual QA rule

Final benchmark acceptance remains manual:

```text
ASTRA CANDIDATE
+ SOURCE SIDE-BY-SIDE
+ CRITIC HISTORY / MATERIAL WORK ORDERS
+ JUANMA REVIEW
+ CHATGPT REVIEW
= ACCEPTED / REJECTED
```

No agent may self-mark `HUMAN PASS`.

## Benchmark B — Torrevieja / Costa Blanca

Deferred while SOLACE photoreal reconstruction is the active benchmark.

When resumed, retain the existing fidelity principle:

High fidelity for identity-defining geography; coherent approximation for secondary structure; procedural plausibility only where it does not undermine recognizability.