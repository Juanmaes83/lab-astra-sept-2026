# LAB spatial review viewer

Public review: https://solace-lab-review.vercel.app

Static comparison and actual GLB inspection using pinned `@google/model-viewer` 4.3.1 (https://modelviewer.dev/). No APIs, credentials, CDN runtime dependency, mocks or product integration.

Run `npm ci`, `npm run build`, `npm run serve` for local review. Build copies original evidence files unchanged into dist and bundles the installed browser viewer. Only allowlisted assets are served; blend checkpoints and internal scripts are not exposed by the site.

Vercel project: `solace-lab-review`, team `juanma-espinosas-projects`. Linked GitHub repository: Juanmaes83/lab-astra-sept-2026. Production branch: `feat/astra-blender-gate-1`. Pushing this branch updates the stable review URL via Git integration, without merging the LAB PR. Keep HUMAN REVIEW PENDING until explicit owner acceptance.

Future gates: update the evidence paths and metadata, build, push, inspect the deployed page and controls, capture review evidence, then request human review. A CLI READY message alone is not browser QA.
