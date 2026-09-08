# Source camera measurements — 2026-09-08

Authority: `references/solace/video/VIDEO_REFERENCIA_SOLACE_CINEMATIC_TARGET.mp4`, eight individually inspected extracted stills. Active source crop `[0,156,1990,1120]`, resized 1920×1080. First shot 420 frames at 30 fps. Coordinates below are manual pixel measurements, approximately ±10–20 px; clipped bounds are explicitly incomplete. These are fitting targets, not proof that a camera has already been solved.

The verified plan is `references/solace/HRUOGWHaMAATXEa.jpg` (inspected). `SOLACE-CONCEPT-01-FLOORPLAN.jpg` is corrupt and is already excluded by the source manifest. Plan confirms Living–Dining–Kitchen west-to-east on north social bar, entry behind sofa, courtyard south. Source first shot looks north throughout, not toward courtyard.

| Seconds | Source landmarks, pixels on 1920×1080 |
| --- | --- |
| 0, 2 | Sofa silhouette approximately `[610,650,1320,850]`; doorway outer reveal `[845,380,1085,670]`; dining window `[1280,334,1730,565]`; glazing mullion x ≈ 280,690,716,1117,1520. Nearly identical camera; preserve opening hold. |
| 4 | Sofa `[398,640,1430,945]`; doorway outer `[757,273,1068,648]`; dining window `[1320,215,1870,508]`; glazing mullion x ≈220,1390. Approach still outside/at glazing. |
| 6 | Sofa clipped left `[0,451,1620,948]`; doorway outer clipped top `[647,0,1100,450]`; dining sill starts x1455 at y229. Sofa remains hero, coffee table clips bottom. |
| 8 | Dining tabletop polygon `[(681,575),(1020,527),(1645,872),(910,1005)]`; dining sill `(304,322)→(1168,310)`; kitchen window clipped top `[1310,0,1810,361]`. |
| 10 | Kitchen window clipped top `[506,0,1144,449]`; island tabletop polygon `[(786,623),(1522,544),(1839,591),(1018,750)]`. Left waterfall end visible, stools bottom/right. |
| 12 | Kitchen window `[373,40,1140,550]`; island tabletop polygon `[(237,757),(1373,719),(1685,879),(0,973)]`. Island nearly frontal and fills lower third. |
| 13.8 | Kitchen window `[140,89,860,573]`; tall unit `[876,120,1070,902]`; island right-back `(790,765)`, right-front `(662,945)`. Island exits left as camera tracks right; right wall occupies ~38% of image. |

## Work orders

1. Discard v03 camera curve only, preserve useful v03 assets/materials. Its southward turn at 6.5–9.7 seconds contradicts all source anchors. Its 24 fps /336-frame settings also contradict the 30 fps target.
2. Opening camera must remain nearly still through 2 seconds; push forward 2–6 seconds. Do not move dining into center before 6 seconds. Pan/track east 6–10 seconds. Track right at near-constant rear-wall distance 10–13.8 seconds, gradually flattening yaw toward north. No courtyard reverse angle.
3. Use sofa bounds and doorway/window corners jointly. Existing v02 sofa is centered `(8.85,14.5)`, doorway x9.05 y16.88, dining window x12.16 y16.88, kitchen window x16.30 y16.88. For a 27 mm lens /36 mm sensor and a 3 m sofa, width-derived first guesses for camera y are about 8.4 at 0/2s, 10.3 at 4s, 12.0 at 6s. These are initialization estimates; fit rotation and positions against pixel targets before accepting.
4. At 0–4 seconds, the sofa center remains approximately x960→914. At 6 it is x~810 and clips left. Camera x must stay near sofa axis until 6 seconds, then move east. Fit downward tilt too: source top of sofa travels y650→451 while width more than doubles. A constant look target does not reproduce this.
5. Jointly fit visible geometry and camera. At 12 seconds, rear kitchen window is approximately 767×510 px (aspect 1.50), while existing v02 window is 3.06×1.58 m (aspect 1.94). A near-frontal camera cannot explain this difference. Window needs a taller opening and/or reduced width, constrained by cabinet/window overlap and other anchors. Dining window also appears taller relative to width than existing geometry. Do not distort focal length to compensate.
6. Rear doorway in the source has a wide outer wall recess and a smaller actual door/opening set back within it. Match two planes separately; do not fit the outer 240-px reveal against the inner leaf width.
7. Glazing at 4 seconds has a large central clear route between x~240 and1390. Source does not establish an animated automatic slide. Prefer a credible opening consistent with the camera crossing; avoid arbitrary pane teleportation.
8. For fitting, project actual world corners with Blender camera projection and minimize weighted pixel residuals over all eight anchors. Prioritize rigid architecture over cushions; use soft width/height constraints for upholstered silhouettes. Report residuals, not merely authored keyframes.

No Blender mutation or shared production-script edit performed. Human visual review remains pending.
