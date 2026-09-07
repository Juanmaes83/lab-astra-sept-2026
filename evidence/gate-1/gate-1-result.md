# Gate 1 — Astra → Blender MCP → Capture → Verify

**Status:** NOT RUN YET
**Date:** 2026-09-07
**Branch:** `feat/astra-blender-gate-1`
**Model expected:** `gpt-6-astra`

## Environment

- Codex CLI version: _pending_
- Active model shown by Codex: _pending_
- Blender version: _pending_
- Blender MCP branch/commit: _pending_
- Safe Mode: _pending_
- MCP status: _pending_

## Gate 1A — Read-only

- [ ] Blender scene read succeeds.
- [ ] Existing objects/transforms reported.
- [ ] `00-scene-before.png` captured.
- [ ] Screenshot matches scene report.
- [ ] No mutation occurred.

### Evidence / notes

_pending_

## Gate 1B — Bounded mutation

Expected mutation: create only `LAB_TEST_CUBE`, exactly `2m × 2m × 2m`.

- [ ] Cube created.
- [ ] Name exactly `LAB_TEST_CUBE`.
- [ ] Dimensions verified `2 × 2 × 2 m`.
- [ ] No pre-existing object modified.
- [ ] `01-scene-after.png` captured.
- [ ] Before/after comparison coherent.

### Evidence / notes

_pending_

## Result

**PASS / FAIL:** NOT RUN YET

## Next gate

SOLACE remains BLOCKED until this document is changed to PASS with reviewable evidence.