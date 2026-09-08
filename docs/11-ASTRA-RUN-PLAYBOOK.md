# 11 — Astra Production Run Playbook

Date established: 2026-09-08

Purpose: define the standard operating procedure for future Astra + Blender production sessions so each run inherits prior learning instead of restarting from first principles.

This playbook operationalizes:

- `docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`
- `docs/10-SOLACE-LESSONS-AND-COST-EFFICIENCY.md`
- `templates/ASTRA_RUN_REPORT_TEMPLATE.md`

The workflow remains reference-first:

```text
REFERENCE
→ ASSETS
→ ASSEMBLY
→ CRITIQUE
→ SHIP
```

But execution must also be cost-aware:

```text
LEARNED STATE
→ REUSE
→ TARGETED BUILD
→ CHEAP ANCHORS
→ CONSOLIDATED CRITIQUE
→ CONSOLIDATED FIX
→ HUMAN PREFLIGHT
→ FINAL RENDER
→ MEMORY UPDATE
```

---

## 1. Mandatory session bootstrap

At the beginning of every meaningful Astra production session:

### Read in this order

1. `AGENTS.md`
2. `docs/01-CURRENT-STATE.md`
3. `docs/09-MATT-SHUMER-ASTRA-WORKFLOW.md`
4. `docs/10-SOLACE-LESSONS-AND-COST-EFFICIENCY.md`
5. `docs/11-ASTRA-RUN-PLAYBOOK.md`
6. the latest relevant file under `evidence/runs/`
7. the relevant reference manifest

Do not re-read the entire repository unless a real ambiguity requires it.

### Resume rule

The latest run report is the resume packet.

Use it to determine:

- best current `.blend`;
- best current preview;
- accepted/rejected domains;
- unresolved issues;
- next best action;
- tasks explicitly marked `DO NOT REDO`.

### Hard rule

**DO NOT REPEAT SETUP, GATE 1, GATE 2, TEST-CUBE, VIEWER OR REFERENCE-DISCOVERY WORK THAT THE CURRENT STATE ALREADY MARKS COMPLETE.**

---

## 2. Establish reference authority before touching Blender

For every reconstruction, identify:

- authoritative visual target;
- spatial/topological source;
- fixed anchor stills;
- support-only references;
- previous generated outputs that are not truth.

For SOLACE use `references/solace/REFERENCE-MANIFEST.json`.

If a required authority source is missing, stop before expensive production and report the missing source.

Do not compensate for absent source evidence by silently inventing details.

---

## 3. Classify inherited work before rebuilding

Inspect the best current scene and classify each visible domain:

- `ACCEPTED_REUSE`
- `REUSE_WITH_CORRECTION`
- `REJECT_AND_REBUILD`
- `UNKNOWN_REVIEW_FIRST`

Suggested SOLACE domains:

- camera;
- architecture/openings;
- living hero assets;
- dining hero assets;
- kitchen hero assets;
- floor;
- glazing;
- materials;
- vegetation/exterior;
- lighting;
- render/compositing.

Do not rebuild an accepted domain merely because the new session has fresh context.

---

## 4. Define one human goal, not many user-facing gates

Use `/goal` when available.

The user-facing goal should describe the actual deliverable and visual bar.

Internal workers and iterations are implementation details.

Do not ask Juanma for approval after every reversible change.

There is one planned human economic gate before expensive final rendering:

**FINAL ANCHOR PREFLIGHT.**

Other human intervention is required only for real blockers, irreversible actions, external publication, budget changes or merge.

---

## 5. Fan out only where specialization increases fidelity

When supported, use focused workers rather than one agent owning the entire scene.

Preferred ownership:

1. reference / shot analysis;
2. camera / lens / timing;
3. architecture / openings;
4. living assets;
5. dining assets;
6. kitchen assets;
7. materials;
8. glazing / vegetation / exterior;
9. lighting / atmosphere;
10. render / finishing;
11. independent critic.

Do not fan out trivial work just to create more agents.

Every worker must receive:

- authoritative reference subset;
- accepted inherited state;
- exact visible domain;
- explicit non-goals;
- output path / handoff expectation.

---

## 6. Use screen visibility as the fidelity budget

Production priority is determined by what the target camera sees.

### High fidelity

- hero assets filling meaningful frame area;
- openings/glazing that define composition;
- floor/wall/material surfaces in close view;
- visible vegetation/exterior depth;
- lighting fixtures affecting the shot.

### Medium fidelity

- secondary objects supporting composition;
- background assets with recognizable silhouettes.

### Proxy / low fidelity allowed

- hidden rooms;
- invisible structure;
- distant unseen property areas;
- geometry outside the shot unless required for lighting/reflection.

Never spend premium tokens on invisible perfection.

---

## 7. Camera workflow

For cinematic reconstruction, camera is measured work.

For SOLACE:

- 30 fps;
- approximately 14.0 s;
- 420 frames;
- anchor references near 0, 2, 4, 6, 8, 10, 12, 13.8 seconds.

### Camera procedure

1. solve lens/FOV and camera height against source;
2. solve anchor poses against stable screen-space landmarks;
3. verify passage/clearance through architecture;
4. interpolate smoothly;
5. preview anchors;
6. inspect frame 1 and final frame explicitly;
7. perform clearance/ray checks where geometry proximity is uncertain.

### Known early checks

- facade clipping;
- wall/glazing collision;
- invented opening/door movement;
- timing drift;
- wrong focal length compensated with wrong camera position.

Do not start final rendering until camera clearance is closed.

---

## 8. Asset / material workflow

Primitive proxies may exist internally but are not acceptable final hero assets.

Before marking a visible domain ready, inspect:

- silhouette;
- proportion;
- edge treatment;
- material response;
- texture/roughness variation;
- contact with floor/walls;
- source-relative position;
- behavior under final lighting.

Do not attempt to solve geometry weakness with render samples.

---

## 9. Lighting / atmosphere workflow

Match the source photographic relationship before polishing.

For SOLACE the established target language is:

- warm premium interior;
- cooler/darker natural exterior;
- readable forest depth;
- believable glazing/reflection/transmission;
- controlled exposure;
- architectural light contribution;
- contact shadows and material separation.

Anchor previews must be judged under representative final lighting, not neutral clay only, before final approval.

---

## 10. Cheap anchor stage

Before any full cinematic render, produce a low-to-moderate cost anchor pack.

For SOLACE include at minimum:

```text
frame 1
frame 61
frame 121
frame 181
frame 241
frame 301
frame 361
frame 415
frame 420
```

Use enough quality to judge:

- composition;
- camera;
- asset silhouettes;
- materials;
- lighting;
- visible technical defects.

Do not spend final-render sampling budget on this stage.

---

## 11. Independent critic policy

The critic is valuable but must be cost-controlled.

### Use one consolidated critic pass per anchor stage

The critic receives the target/reference anchor and generated anchor.

It identifies material visual tells and groups them by responsible domain.

### Critic output format

```text
TELL
WHY IT BREAKS FIDELITY
SEVERITY: BLOCKER / HIGH / MEDIUM / LOW
RESPONSIBLE DOMAIN
WORK ORDER
```

### Cost rule

Do not immediately open a new expensive build loop for every LOW/MEDIUM tell.

Aggregate findings first.

Prioritize:

1. blockers;
2. camera/composition errors;
3. hero geometry/material errors;
4. lighting/exterior errors;
5. only then minor polish.

---

## 12. One consolidated correction pass

After critic findings:

1. deduplicate related tells;
2. identify root causes;
3. send grouped work orders to relevant workers;
4. apply corrections in one coordinated pass;
5. regenerate the anchor pack once.

A second internal correction round is allowed only if a blocker remains clearly visible.

Do not enter an unbounded critic/fix loop.

If remaining differences are aesthetic rather than blocking, route them to human anchor review.

---

## 13. Mandatory human anchor preflight

Before a 420-frame / final cinematic render, stop and make the current anchor pack accessible to Juanma + ChatGPT.

Human review answers one question:

> Is this visual state strong enough to justify the expensive full render?

Possible decisions:

- `APPROVE FINAL RENDER`
- `ONE CONSOLIDATED CORRECTION REQUIRED`
- `STOP / STRATEGY CHANGE`

### Astra must not spend final-render compute before this approval

unless Juanma explicitly waived the preflight for that run.

This is a cost gate, not a return to micro-management.

---

## 14. Final render policy

After human anchor approval:

1. freeze the approved scene revision;
2. save/version the final `.blend`;
3. verify textures/assets are available or packed as required;
4. run final technical preflight;
5. start one final sequence render;
6. do not stop it for cosmetic LOW-severity critic findings;
7. stop only for genuine technical corruption/blocking errors;
8. encode and verify final MP4;
9. save technical manifest.

For SOLACE expected review delivery remains:

- 1920×1080;
- 30 fps;
- approximately 14 s;
- 420 frames;
- premium Blender render appropriate to available hardware.

---

## 15. Post-render review policy

Astra verifies technical integrity only:

- frame count;
- duration;
- decode;
- missing frames;
- gross corruption;
- obvious geometry failure introduced during render.

Astra does not self-award `HUMAN PASS`.

Final visual judgment belongs to Juanma + ChatGPT.

Do not start another expensive correction/render cycle automatically after final delivery unless a technical blocker makes the deliverable unusable.

---

## 16. Run memory protocol

At the end of every meaningful run:

### A. Create run report

Use:

`templates/ASTRA_RUN_REPORT_TEMPLATE.md`

Save under:

`evidence/runs/`

### B. Update lessons only when confirmed

Update:

`docs/10-SOLACE-LESSONS-AND-COST-EFFICIENCY.md`

only when the run produced a reusable, evidence-backed lesson.

### C. Update this playbook only when workflow changes

Do not rewrite the playbook every session.

Update it when a new rule changes future execution order, validation, cost control or handoff.

### D. Update current state when needed

Update `docs/01-CURRENT-STATE.md` when the best accepted scene/output or active blocker materially changes.

### E. Leave a resume packet

The run report must state:

- current best scene;
- current best preview/render;
- what is accepted;
- what is unresolved;
- what must not be redone;
- next best action.

---

## 17. Documentation cost limit

Documentation should save future tokens.

Therefore:

- do not paste full terminal transcripts;
- do not repeat unchanged strategy text;
- link to existing docs instead;
- record root causes, fixes and decisions;
- keep run reports operational;
- promote a lesson once, then reference it.

A run report that costs more to read than the context it replaces has failed its purpose.

---

## 18. Token / compute accounting

When usage metrics are available, record exact values by phase.

When unavailable, record qualitative intensity only.

Never invent token counts.

At minimum distinguish:

### Model/token work
- reference reasoning;
- visual critique;
- planning;
- scripting;
- correction reasoning.

### Blender/compute work
- preview rendering;
- baking;
- simulation if any;
- final rendering;
- encoding.

After each run ask:

> Which expensive operation created the largest visible quality gain?

and:

> Which expensive operation could have been prevented by an earlier check?

These answers belong in the run report.

---

## 19. SOLACE known preflight checklist

Before the next expensive SOLACE final render verify:

### References
- [ ] target video present
- [ ] valid floorplan present
- [ ] anchor stills present
- [ ] correct authority order understood

### Camera
- [ ] frame 1 matches opening composition broadly
- [ ] living timing/composition aligned
- [ ] dining timing/composition aligned
- [ ] kitchen timing/composition aligned
- [ ] frame 420 clean
- [ ] no facade/wall clipping
- [ ] no invented architectural animation

### Geometry/materials
- [ ] hero sofa no longer reads as primitive proxy
- [ ] dining hero assets credible
- [ ] kitchen island/cabinetry credible
- [ ] floor continuity complete
- [ ] important glazing mullions/divisions present

### Exterior
- [ ] vegetation does not intersect circulation/openings
- [ ] forest/exterior depth readable
- [ ] glazing relationship believable

### Lighting
- [ ] library lighting readable
- [ ] warm interior / cooler exterior relationship present
- [ ] exposure controlled

### Cost gate
- [ ] consolidated critic pass completed
- [ ] consolidated correction applied
- [ ] human anchor review received
- [ ] explicit approval to start final render

---

## 20. Standard future run shape

```text
BOOTSTRAP FROM MEMORY
↓
READ LATEST RUN REPORT
↓
REFERENCE AUTHORITY CHECK
↓
CLASSIFY INHERITED DOMAINS
↓
TARGETED BUILD / REUSE
↓
CHEAP ANCHOR PACK
↓
ONE CONSOLIDATED INDEPENDENT CRITIC
↓
ONE CONSOLIDATED CORRECTION
↓
UPDATED ANCHOR PACK
↓
JUANMA + CHATGPT HUMAN PREFLIGHT
↓
ONE FINAL FULL RENDER
↓
TECHNICAL VERIFY
↓
SHIP CANDIDATE
↓
RUN REPORT + LESSON DELTA + RESUME PACKET
```

This is the default until evidence supports a better workflow.

---

## 21. Definition of process improvement

The system is learning when a new Astra session can begin by reading a small set of persisted files and then:

- avoid a previously known failure;
- reuse a previously accepted asset/state;
- skip a redundant experiment;
- reduce critic loops;
- avoid a wasted final render;
- reach equal or better visual quality with less model effort or compute.

That is the operational meaning of learning for this LAB.