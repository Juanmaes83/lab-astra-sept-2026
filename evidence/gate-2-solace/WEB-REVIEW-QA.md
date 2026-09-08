# Public LAB review deployment

URL: https://solace-lab-review.vercel.app

Candidate evidence commit: 348aba28bd80f6425896b110210798c4fcaba430.
Initial viewer commit: 3e2515beaddcf2e71da3166cb94ce3ee0565c8b5.

Vercel project solace-lab-review, owner juanma-espinosas-projects, connected to Juanmaes83/lab-astra-sept-2026. Production branch feat/astra-blender-gate-1. Git-triggered deployment for 3e2515b reached READY independently of the initial CLI deploy; stable alias updates without merge. Authentication initially failed but the normal device flow completed; no credentials committed.

## Integrity

Final v04 blend opened read-only in Blender 5.2.1 background mode: SOLACE_GATE_2 contains 137 objects, 135 meshes and two cameras. GLB independently parsed: 185324 bytes, 137 nodes. Full candidate file inventory and SHA256 hashes: review-integrity.json. All original Gate 1/2 evidence and four blend versions committed and pushed.

Public HTTP checks for source, top, perspective and GLB all returned 200 and exact SHA256 equality with local originals. Website build serves only an explicit evidence allowlist and locally installed model-viewer 4.3.1. No fabricated API, no fake preview, no external runtime CDN.

## Browser observations

- Public page opened in Chrome through browser tools, correct title and truth/status metadata.
- Source image decoded 680 x 661, top and perspective 1200 x 1200; all loaded.
- Actual GLB emitted loaded status on initial navigation. Cached reload could race the load listener; added a loaded-state check after custom element registration.
- Large inspection mode toggled and closed successfully.
- Orbit drag changed visible camera readout from 35 degrees azimuth / 45 degrees to -20.3 / 32.7.
- Zoom-in button changed distance from 65 m to 52 m.
- Reset invoked; final confirmation recorded in tool session.
- Mobile override 390 x 844: effective content width 375 px, scroll width 375 px, single 347 px comparison column, all images loaded. Override reset afterward.
- No console-breaking error observed. One warning: rAF timed out in updateSource during backgrounded browser control.

## Incomplete screenshot gate

Page.captureScreenshot repeatedly timed out at 5000 ms on the selected Chrome session, including a fresh review tab. A scroll gesture also timed out, while DOM and orbit/zoom controls remained responsive. Windows fallback could not identify a SOLACE-titled target window and no unrelated window was captured. No deployed screenshot file is claimed or fabricated.

BROWSER QA: **FAIL / incomplete screenshot evidence**, despite successful asset, responsive-layout and interaction checks. GLB interactive controls: PASS for orbit, explicit zoom buttons, reset and large mode; wheel/pan not fully verified.

TECHNICAL GATE 2 CANDIDATE: PASS (existing geometry result unchanged).
HUMAN REVIEW: PENDING. No modelling/refinement, materials, PR merge or product handoff performed. Next step: Juanma + ChatGPT visual inspection of the public URL, plus complete deployed screenshot evidence when browser capture is available.
