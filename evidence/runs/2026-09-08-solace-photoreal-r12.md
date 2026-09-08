# Run report — SOLACE photoreal r12

## 1. Identity

2026-09-08; SOLACE first continuous shot. Codex main builder plus specialized workers; active model identity not independently established here. Branch `feat/astra-blender-gate-1`. Session inherited 24187eb; safely synchronized new policy through ddc9084. End commit: the commit containing this report. Goal remains incomplete pending human preflight and final render.

## 2. Starting state

Inherited r09, useful v03-derived architecture/assets and source-fitted camera. Sources: `references/solace/REFERENCE-MANIFEST.json`. No previous report existed under `evidence/runs/`. Historical v01/v02/v03 retained. Reuse: camera, kitchen, dining, floor and forest after earlier fixes. Correct: opening mullions/library lighting. No domain rebuilt wholesale.

## 3–5. Attempt, process and files

Continued the existing reference reconstruction, not an infrastructure test. `correct_photoreal_r10.py` projected source opening divisions onto the existing facade, changed coated glazing and library lighting; r11 attached strips to actual shelf undersides; r12 restored 6s chair clearance and balanced glossy environment exposure. Versioned assemblies r01–r12 remain in ignored `outputs/solace/photoreal-work/`.

Final scene: `outputs/solace/SOLACE_PHOTOREAL_GOAL_v01.blend`; nine packed textures; 1920×1080, 30fps, 420 frames, Cycles OPTIX, adaptive 64–256 samples with denoising. Re-render script: `render_photoreal.py`. Encoding/technical verification script prepared but not executed: `verify_photoreal_delivery.ps1`.

Evidence: `evidence/solace-photoreal-goal-v01/PREFLIGHT.md`, nine r12 previews, one full-resolution opening, `REVIEW.md`. Asset licences: `outputs/solace/assets/PROVENANCE.md` and pine subfolder. Original downloaded packages remain local; used textures are packed.

## 6–8. Problems, root causes, fixes and critic

- Opening had wrong mullion positions: inherited geometry did not match measured source pixels. Projected source divisions to facade in r10; critic confirms alignment materially improved.
- New LED strips initially crossed shelves: incorrect hardcoded heights. Read actual shelf geometry, corrected undersides in r11; critic confirms attachment.
- Moving armchair helped opening but obstructed 6s foreground: cross-anchor composition conflict. Restored accepted 6s location in r12, retaining opening compromise.
- Reflection strength did not match reflection composition: same replacement HDRI cannot reproduce exact source surroundings. Glossy-ray exposure improved intensity only; PARTIAL, explicitly art-directed.
- Earlier camera/floor/vegetation fixes and full critique history: see `REVIEW.md`. No new blackout/clipping at inspected r12 anchors. Agent critic is not human approval; final sequence continuity remains unverified.

## 9. Result

Best scene is r12 in the requested v01 blend. Independent critic: serious review candidate with limitations. Human review: PENDING. No corrected MP4 exists. Prior complete 420-frame r09 sequence retained in `photoreal-work/final-frames/`; prior final blend archived as `pre-opening-final.blend`. Corrected full render paused after nine frames in `final-frames-r2/`.

## 10–13. Cost, learning and deltas

The full render started under the previously loaded strategy, before this turn fetched new policy commits. Fetch revealed ddc9084 requiring explicit human preflight; safe fast-forward changed documentation only, then own render PID was stopped. Approximately 168 seconds produced nine corrected frames; interrupted work after frame9 is not quantified. All files retained.

Goal tool reported cumulative 274,306 tokens at resumption, status usageLimited; this is not per-phase billing or a current model identity assertion. Preview/critic/correction model cost not separately exposed. Repeated small critic loops were expensive; no further aesthetic loops authorized before human review. Final compute ~18s/frame on this configuration, approximately two hours for an uninterrupted sequence.

Existing lessons/playbook already cover premature rendering and critique consolidation; no new permanent rule or workflow rewrite is needed. Current-state document updated. Do not confuse saved final settings with completed final output.

## 14. Resume packet

- READ FIRST: AGENTS, current state, docs09/10/11, this report, reference manifest.
- BEST: requested photoreal v01 blend = r12, packed, ready for render. PREVIEW: PREFLIGHT.md. No accepted final video.
- DO NOT REDO: setup, gates, reference discovery, camera solving, whole-house modeling, previous resolved floor/fern/clearance defects, viewer work.
- NEXT: Juanma + ChatGPT review anchors and explicitly approve final render or request one consolidated correction.
- AFTER APPROVAL: resume corrected frames10–420 without overwriting nine existing frames; render same frozen scene/settings, encode using prepared verifier, inspect technical integrity, commit/push, no merge.
- BLOCKER: mandatory human preflight decision, not Blender or MCP failure.
