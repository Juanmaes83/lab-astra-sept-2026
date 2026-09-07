# 01 — Current State

Date: 2026-09-07

## Environment verified

- Windows 11 Pro / x64.
- Node / npm available.
- Codex CLI installed and healthy.
- Codex auth mode: ChatGPT.
- `gpt-6-astra` now launches successfully in Codex CLI on the project owner's machine.
- One unrelated Cloudflare MCP may still require login/cleanup; it does not block Blender MCP work.

## Astra access verification

Previous 2026-09-04 state was `Astra pending`.

That state is now obsolete.

Observed on 2026-09-07:

```text
codex -m gpt-6-astra
```

launches a Codex session whose UI reports `gpt-6-astra` as the active model.

### Decision

Use Astra for the active LAB gate, while keeping orchestration/model selection configurable.

No Blender/MCP architecture decision may depend on Astra being the only future model.

## PROJECT-PELU relationship

This repository is now formally the **Spatial Production LAB** for PROJECT-PELU F2.

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

Branch existence has been re-confirmed from GitHub.

Current integration gate:

```text
ASTRA
→ BLENDER MCP
→ BLENDER
→ READ SCENE
→ CAPTURE SCREENSHOT
→ SMALL BOUNDED CHANGE
→ CAPTURE / VERIFY
```

Gate evidence template:

`evidence/gate-1/gate-1-result.md`

## Active branch

`feat/astra-blender-gate-1`

## Next action on local Windows machine

Follow `docs/07-BLENDER-CODEX-SETUP.md` and execute Gate 1A read-only first.

SOLACE remains blocked until Gate 1A + Gate 1B are PASS with screenshot/scene evidence.

## Benchmark references

SOLACE / Thomas-Astra reference material remains the first architectural benchmark after Gate 1. Original binaries can be uploaded manually, with provenance/source manifests committed alongside them.