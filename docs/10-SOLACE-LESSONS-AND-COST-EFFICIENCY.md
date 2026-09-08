# 10 — SOLACE Lessons and Cost Efficiency

Date established: 2026-09-08

Purpose: preserve confirmed lessons from the SOLACE Astra + Blender benchmark so future sessions improve quality while reducing repeated reasoning, wasted renders and token/credit consumption.

This file is not a chronological log. Chronological details belong in `evidence/runs/`.

Only reusable, evidence-backed lessons belong here.

---

## 1. Current conclusion

The project has now demonstrated two different quality regimes:

### Historical POC regime

`SOLACE_VIDEO_PROOF_v01` / `v02`

Proved:

- Astra can control Blender;
- a floorplan can become a recognizable spatial reconstruction;
- a Living → Dining → Kitchen walkthrough can be rendered.

Failed to prove:

- premium photoreal fidelity;
- source-matched camera timing;
- hero-asset quality;
- premium lighting/material response.

### Reference-first photoreal regime

The later photoreal revisions (`assembly_r06` onward, including `r07`, `r08`, `r09`) produced a materially higher visual-quality level and validated the Matt Shumer reference-first workflow as a stronger production direction.

The quality jump came from changing the process, not merely from increasing render samples.

---

## 2. Confirmed strategic lesson: reference must exist before production

### Failure observed

Earlier runs worked with incomplete or unavailable cinematic reference material and therefore estimated camera, finishes and composition.

### Permanent rule

**DO NOT START A RECONSTRUCTION GOAL UNTIL AUTHORITATIVE REFERENCES ARE LOCALLY/REPOSITORY-AVAILABLE AND IDENTIFIED BY MANIFEST.**

For SOLACE the authority order is:

1. `references/solace/video/VIDEO_REFERENCIA_SOLACE_CINEMATIC_TARGET.mp4`
2. `references/solace/HRUOGWHaMAATXEa.jpg`
3. `references/solace/stills/`
4. other approved SOLACE support references
5. `VIDEO_REFERENCIA_SOLACE_BLENDER_PROCESS.mp4` as process support only
6. previous generated LAB work as implementation history only

The source beats previous generated work when they conflict.

---

## 3. Confirmed lesson: generate fixed visual anchors before camera work

The authoritative target now has fixed 16:9 stills at approximately:

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

Permanent rule:

**SOLVE CAMERA AND VISIBLE COMPOSITION AGAINST FIXED ANCHORS, NOT AGAINST A VERBAL DESCRIPTION OF THE VIDEO.**

This prevents generic trajectories and timing drift.

---

## 4. Confirmed lesson: “technically valid” is not “visually successful”

A `.blend`, GLB or MP4 existing is not a quality milestone by itself.

Earlier POCs were technically valid but visually far below the target.

Permanent rule:

**FILE EXISTENCE IS NEVER THE PHOTOREAL STOP CONDITION.**

Acceptance is based on visible comparison against source references.

---

## 5. Confirmed lesson: procedural does not mean primitive

Earlier work used many simplified cubes, cylinders and low-complexity procedural materials for hero-visible assets.

Increasing Cycles samples cannot turn weak geometry or weak materials into premium archviz.

Permanent rules:

- primitive geometry is acceptable for blocking, hidden support and cheap internal previews;
- hero-visible geometry must survive cinematic framing;
- use Blender-native modeling, modifiers, procedural detail, physically plausible materials, approved assets or available generation capabilities where they materially improve fidelity;
- spend modeling effort according to screen visibility, not property completeness.

---

## 6. Confirmed lesson: camera is a first-class reconstruction problem

Historical v02 used manually inferred timing and a small set of hand-authored camera poses. Visual comparison showed meaningful timing mismatch relative to the target.

Permanent rules:

- use the target cadence: 30 fps;
- first SOLACE shot target: approximately 14.0 s / 420 frames;
- use anchor-frame comparison;
- match stable screen-space landmarks;
- do not invent camera motion merely because it is cinematic;
- do not invent door/glazing animation to accommodate an incorrect camera path.

---

## 7. Confirmed lesson: use specialized ownership

One agent/context attempting architecture, camera, furniture, materials, vegetation, lighting and critique at once tends to take shortcuts.

When the environment supports workers/sub-agents, split responsibility by domain.

For SOLACE the useful domains are:

- reference analysis;
- camera / lens / timing;
- architecture / openings;
- living assets;
- dining assets;
- kitchen assets;
- materials;
- glazing / exterior / vegetation;
- lighting / atmosphere;
- render / finishing;
- independent critic.

Permanent rule:

**A WORKER OWNS FIDELITY OF ITS DOMAIN; THE MAIN AGENT OWNS ASSEMBLY AND PRIORITIZATION.**

---

## 8. Confirmed lesson: builder and critic must be separated

The Matt Shumer workflow correctly prevents the builder from grading its own homework.

This improved SOLACE because later revisions detected real defects such as:

- final camera entering/clipping facade geometry;
- incomplete flooring near cabinetry;
- vegetation intersecting circulation;
- missing major glazing division;
- weak library lighting.

Permanent rule:

**USE AN INDEPENDENT CRITIC FOR MATERIAL VISUAL TELLS, BUT CONTROL WHEN THE CRITIC IS ALLOWED TO TRIGGER EXPENSIVE REWORK.**

The critic creates work orders; it does not own cost policy.

---

## 9. Cost lesson: strict critique is valuable but can become the largest token loop

Exact Astra token/credit attribution has not been exposed in the available logs, so exact percentages must not be invented.

Observed process, however, shows repeated cycles of:

```text
preview
→ inspect
→ critic
→ correction script
→ new blend revision
→ preview
→ critic
→ correction
```

with revisions progressing through at least r06 → r07 → r08 → r09.

This is likely model/token intensive because each cycle requires visual reasoning, context, diagnosis and code modification.

Permanent rule:

**CRITIQUE SHOULD BE CONSOLIDATED INTO MATERIAL WORK ORDERS RATHER THAN TRIGGERING ONE EXPENSIVE AGENT LOOP PER SMALL DEFECT.**

---

## 10. Cost lesson: render compute and model-token cost are different

Treat them separately.

### Model/token-intensive work

Typically includes:

- reference interpretation;
- visual comparison;
- independent criticism;
- diagnosis;
- correction planning;
- code/script generation.

### Blender/compute-intensive work

Typically includes:

- high-resolution anchor previews;
- high sample counts;
- repeated Cycles renders;
- 420-frame final sequence rendering.

Permanent rule:

**DO NOT CONFUSE CHEAP MODEL ACTIONS WITH CHEAP COMPUTE ACTIONS OR VICE VERSA. RECORD BOTH WHEN AVAILABLE.**

---

## 11. Major efficiency failure: final render started before final visual preflight was closed

A 420-frame, 1920×1080, 30 fps Cycles/OptiX render was started, then the first full-resolution frame revealed a missing glazing division and weak library illumination. The render was paused for correction.

The decision to pause was correct; launching the expensive final render before this check was inefficient.

Permanent rule:

# NO FINAL 420-FRAME RENDER WITHOUT AN APPROVED FINAL ANCHOR PREFLIGHT.

Required preflight must include at least:

- frame 1 / opening glazing composition;
- living hero;
- dining hero;
- kitchen hero;
- end frame 420;
- camera clearance / no clipping;
- key glazing divisions;
- hero lighting;
- visible floor continuity;
- exterior/vegetation clearance.

---

## 12. Human review should be inserted before expensive final rendering

Juanma + ChatGPT can judge whether the visual quality has reached a worthwhile level without consuming Astra credits for further self-review.

Permanent rule:

```text
ASTRA BUILD
→ CHEAP ANCHOR PACK
→ ONE CONSOLIDATED CRITIC PASS
→ ONE CONSOLIDATED CORRECTION PASS
→ HUMAN ANCHOR REVIEW
→ FINAL RENDER
```

Not:

```text
critic → fix → critic → fix → final render → critic → abort → fix → final render ...
```

The Matt workflow remains authoritative for quality, but human review becomes the economic gate before expensive final sequence rendering.

---

## 13. Human review is not a regression to micro-gates

The project previously suffered from too many tiny infrastructure gates.

The new human review rule is different.

There should be one economically meaningful review point:

**FINAL ANCHOR PACK BEFORE FULL RENDER.**

Internal reversible production iterations remain autonomous.

Do not ask Juanma to approve every material, script or camera edit.

---

## 14. Reuse accepted work instead of rebuilding

The photoreal workflow should inherit accepted geometry/material/camera components from the best current revision.

Permanent rule:

Before rebuilding any domain, classify its inherited state:

- `ACCEPTED_REUSE`
- `REUSE_WITH_CORRECTION`
- `REJECT_AND_REBUILD`
- `UNKNOWN_REVIEW_FIRST`

Never rebuild from zero merely because a new Astra session started.

---

## 15. Every expensive run must produce operational memory

Astra does not become reliably more efficient across sessions unless the process knowledge is externalized.

Permanent rule:

Every meaningful run must create/update:

1. a chronological run report using `templates/ASTRA_RUN_REPORT_TEMPLATE.md`;
2. this lessons file when a reusable lesson is confirmed;
3. `docs/11-ASTRA-RUN-PLAYBOOK.md` when the standard workflow changes;
4. `docs/01-CURRENT-STATE.md` when the active project state materially changes.

This is how the project “learns”.

---

## 16. Documentation must not become a new token sink

The learning system exists to save tokens, not consume them.

Permanent rules:

- run reports are concise and factual;
- do not narrate every command;
- preserve only decisions, errors, fixes and reusable learnings;
- promote repeated lessons to the playbook once;
- do not rewrite the same historical explanation every session;
- future Astra sessions read the latest relevant run report instead of replaying full history.

---

## 17. Known SOLACE error patterns to check early

Before future final renders, explicitly inspect:

### Camera
- facade / wall clipping at start or end;
- trajectory timing drift;
- wrong lens compensated by bad camera placement.

### Architecture
- missing glazing mullions/divisions;
- opening conditions inconsistent with source;
- camera-visible facade/wall discontinuities.

### Interior
- incomplete floor rows;
- primitive hero furniture;
- weak library/architectural lighting;
- kitchen island/window relationships.

### Exterior
- vegetation entering doors/circulation;
- insufficient forest depth;
- unrealistic glazing/exterior relationship.

### Rendering
- high-cost full render started before anchor approval;
- excessive samples used to compensate for modeling/material problems.

---

## 18. Efficiency target for future SOLACE-style projects

The preferred future pattern is:

```text
1. PREPARE REFERENCES ONCE
2. EXTRACT / MANIFEST ANCHORS ONCE
3. LOAD BEST KNOWN PLAYBOOK + LAST RUN REPORT
4. REUSE ACCEPTED BASE
5. FAN OUT ONLY WHERE NEEDED
6. BUILD / CORRECT VISIBLE DOMAINS
7. RENDER CHEAP ANCHORS
8. CONSOLIDATED INDEPENDENT CRITIC
9. ONE CONSOLIDATED CORRECTION PASS
10. HUMAN ANCHOR REVIEW
11. ONE FINAL FULL RENDER
12. RECORD RUN + PROMOTE NEW LEARNING
```

The aspiration is not zero iteration. It is **high-information iteration**.

---

## 19. What success means for process learning

A future run is more efficient when it can truthfully say:

- I did not repeat environment setup;
- I did not rediscover reference authority;
- I reused accepted scene work;
- I checked known failure patterns before render;
- I consolidated criticism;
- I avoided an unnecessary full render;
- I left a resume packet for the next session.

Every successful expensive run should make the next run cheaper, faster or visually stronger.