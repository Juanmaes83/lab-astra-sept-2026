# 01 — Current State

Date: 2026-09-07

## Environment verified

- Windows 11 Pro / x64.
- Node / npm available.
- Codex CLI installed and healthy.
- Codex auth mode: ChatGPT.
- `gpt-6-astra` active in Codex CLI on the project owner's machine.
- Blender `5.2.1 LTS` installed.
- `uv` installed and operational.
- One unrelated Cloudflare MCP may still require login/cleanup; it does not block Blender MCP work.

## Astra access verification

Previous 2026-09-04 state was `Astra pending`.

That state is obsolete.

Observed on 2026-09-07:

```text
codex -m gpt-6-astra
```

launches a Codex session whose UI reports `gpt-6-astra` / `gpt-6-astra medium` as active.

### Decision

Use Astra for the active LAB gates, while keeping orchestration/model selection configurable.

No Blender/MCP architecture decision may depend on Astra being the only future model.

## PROJECT-PELU relationship

This repository is formally the **Spatial Production LAB** for PROJECT-PELU F2.

```text
LAB
Astra + Blender + MCP + QA
        ↓
ACCEPTED SPATIAL PACKAGE
        ↓
PROJECT-PELU
SpatialAsset / ViewerAdapter / 360 fallback
```

The repos remain separate.

## Blender MCP state

Source LAB:

`Juanmaes83/blender-mcp` → branch `lab/astra-sept-2026`

Operational state:
- Safe Mode enabled with `BLENDER_MCP_SAFE_MODE=1`;
- 69 Safe Mode tests PASS;
- `MCP for Blender` addon enabled;
- Blender MCP panel connected on port `9876`;
- Codex MCP server registered as `blender-astra-lab`.

## Gate 1 result

**Status: ✅ CLOSED / PASS — 2026-09-07**

### Gate 1A
- scene inspection PASS;
- `Cube`, `Camera`, `Light` reported correctly;
- viewport capture PASS;
- no mutation;
- MCP calls reported SUCCESS / `isError=false`.

### Gate 1B
- created exactly one `LAB_TEST_CUBE`;
- position `(0,4,0)`;
- rotation `(0,0,0)`;
- scale `(1,1,1)`;
- dimensions `2 × 2 × 2 m`;
- pre-existing `Cube`, `Camera`, `Light` unchanged;
- before/after capture PASS;
- no correction required;
- no `.blend` overwritten.

Full textual result:

`evidence/gate-1/gate-1-result.md`

Local Astra evidence paths were reported for Gate 1A and Gate 1B; screenshot binaries still need normal Git upload/push from the local LAB branch so GitHub holds the complete visual record.

## Active branch

`feat/astra-blender-gate-1`

## Next action

Gate 2 is now NEXT: create the smallest useful real-estate spatial slice before starting full SOLACE.

Target Gate 2 loop:

```text
CLEAN/VERSIONED SCENE
→ BOUNDED ARCHITECTURAL BLOCKOUT
→ DIMENSION CHECK
→ CAPTURE
→ VERIFY
→ CORRECT IF NEEDED
→ GLB EXPORT
→ MINIMAL SCENE MANIFEST
```

SOLACE remains blocked until Gate 2 proves that Astra+Blender can generate a reviewable real-estate-relevant asset, not just infrastructure/test geometry.

## Benchmark references

SOLACE / Thomas-Astra reference material remains the first full architectural benchmark after Gate 2. Original binaries can be uploaded manually, with provenance/source manifests committed alongside them.
