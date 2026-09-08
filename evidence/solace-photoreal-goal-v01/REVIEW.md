# SOLACE photoreal goal v01 — review record

HUMAN VISUAL REVIEW: COMPLETED for anchor preflight by explicit owner approval. Final render and encoding completed; see `technical-verification.json` and the final-render run report. Historical critique below is preserved; no later human playback verdict is claimed.

Authority: `references/solace/video/VIDEO_REFERENCIA_SOLACE_CINEMATIC_TARGET.mp4`; first shot 0–13.967s. Floorplan: `references/solace/HRUOGWHaMAATXEa.jpg`. Eight supplied 1080p stills at 0/2/4/6/8/10/12/13.8s; source recording crop x0/y156/w1990/h1120. Previous outputs were implementation history, not visual truth.

Baseline: preserved local `SOLACE_VIDEO_PROOF_v03.blend`, itself derived from v02. Existing envelope and useful details retained; incorrect courtyard-facing camera removed. New scene assemblies were saved separately as r01–r07, never over the historical proofs.

## Workers and corrections

- Reference/camera worker: source pixel landmarks, numerical pose fitting, eight checkpoints and camera-height audit. Physical dimensions remain reconstructed estimates. Pixel targets were manually annotated; the camera was numerically fitted, not claimed as recovered ground-truth intrinsics/extrinsics. Residual files expose fit limitations.
- Living/dining worker: sewn mesh cushions, curved chair backs, wood joinery, sling chair, books and hollow vessels. Later corrections lowered/relaxed backs, moved unrealistic front seams, compressed individual seats and added source-relative coffee accessories.
- Look/exterior worker: warm localized practicals, material detail, real near-pine asset, photographic forest environment. Model import initially grouped three display variants and intruded into dining; corrected to one variant and recaptured before delivery.
- Main builder: shell/window proportions, service passage, kitchen oven position, cabinet/island details, appliance fascia, ceramic/glass/food forms, assembly and finishing.
- Independent fresh-context critic: viewed shuffled, normalized pairs, correctly identified references and returned concrete work orders. Did not inspect builder code.

## Critique history

1. r01 rejected: bright flat illumination; oversized/cropped sofa; sparse procedural forest; missing enclosed kitchen opening; crude props. r02 corrected lighting, geometry, camera depth and introduced a licensed environment.
2. r02 rejected: sofa profile, table/door relationship, exterior, appliance and bread detail. r03 corrected living composition, bookcase extent, chair position, cushion seams, coffee-machine fascia and source-relative props.
3. r03 required further correction: forest bands, uniform seats, narrow/angular dining table. r04–r06 added scanned weave relief, asymmetrical seat compression, wider rounded table, authored pine geometry, corrected instancing and canopy/sky framing.
4. r06 critic judged a serious source-aligned review candidate justified for dining/kitchen, not human PASS. Remaining orders: subdued exterior and enclosed/lower-headed service passage; camera-height discrepancy independently audited. r07 addresses these final orders.

5. r08 constrained the camera to the actual inside-wall bounds through frame 420 and removed a height dip at 6s. The critic accepted the living and endpoint as serious candidates. Ray-cast diagnosis then identified incomplete historical floorboard rows and fern leaves intruding into the entry; r09 completed the affected rows and removed only those generated leaf faces.
6. Full-resolution opening inspection found incorrect facade divisions and weak shelf lighting. r10 projected source-measured mullion pixels onto the existing facade, added coated glazing and adjusted localized lights. r11 attached the new strips to actual shelf undersides. r12 restored chair clearance at 6s and increased the same forest environment's glossy-ray exposure (art-directed, not physically calibrated).
7. The independent critic reviewed r12 opening/6s against source: a serious review candidate is justified, with no new visible clipping or blackout in those previews. Opening reflection composition still differs, chair position is a compromise, sofa proportions and forest proximity remain approximate. This is not human approval or a claim of exact photoreal/source fidelity.

The initial complete 420-frame render and its blend were retained in the ignored local work archive. Corrected final rendering uses a separate `final-frames-r2` directory. All assembly versions r01-r12 remain local; no historical proof was overwritten.

After fetching the new ddc9084 repository policy during this continuation, the corrected render was stopped after nine saved frames. Human anchor approval is now mandatory. See `PREFLIGHT.md`; the requested final MP4 does not exist yet. Render settings in `photoreal_delivery.json` are configuration, not a completion claim.

## Truth and limits

This is reconstructed visualization, not survey/BIM geometry or an exact copy of source assets. Source assets/camera metadata were unavailable beyond the supplied media. The forest is an approximate CC0 environment plus real near geometry, not the exact source forest. Food/labels and some furniture detail remain procedural. Similarity is not established by a file existing or by render completion.

Used external asset licences and source URLs are in `outputs/solace/assets/PROVENANCE.md` and its pine subfolder. Required texture images are packed into the delivered blend. Final technical facts are recorded in `outputs/solace/photoreal_delivery.json`.
