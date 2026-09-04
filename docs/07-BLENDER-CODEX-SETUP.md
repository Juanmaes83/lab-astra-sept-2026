# 07 — Blender + Codex Setup

## Purpose

Connect the current Codex model to the September Blender MCP LAB without depending on Astra rollout.

## Source Blender MCP

Use:

`Juanmaes83/blender-mcp` → branch `lab/astra-sept-2026`

That branch is the technical MCP implementation source. This repository remains the higher-level experiment/orchestration repo.

## Windows prerequisites already verified

- Node / npm available.
- Codex CLI installed.
- Codex Doctor healthy.
- ChatGPT auth configured.
- Current working model: `gpt-5.6-sol`.

## Clone Blender MCP LAB

```powershell
cd $HOME\Documents
git clone --branch lab/astra-sept-2026 --single-branch https://github.com/Juanmaes83/blender-mcp.git blender-mcp-astra-lab
cd blender-mcp-astra-lab
```

## Install/update Blender addon

```powershell
uv run blender-mcp install-addon
```

Then in Blender:

1. `Edit -> Preferences -> Add-ons`;
2. enable `MCP for Blender`;
3. in 3D View press `N`;
4. open `MCP for Blender`;
5. start the MCP server.

## Safe Mode

```powershell
$env:BLENDER_MCP_SAFE_MODE="1"
```

## Register MCP in Codex

```powershell
codex mcp add blender-astra-lab --env BLENDER_MCP_SAFE_MODE=1 -- uv --directory "$HOME\Documents\blender-mcp-astra-lab" run blender-mcp
```

Check:

```powershell
codex mcp list
```

## Launch with current available model

```powershell
codex -m gpt-5.6-sol
```

Inside Codex, inspect MCP status and run the first read-only test:

```text
Inspect the currently open Blender scene. Do not modify anything. Report scene objects, then capture a viewport screenshot and verify what you see.
```

If that passes, run one bounded mutation:

```text
Create one cube exactly 2m x 2m x 2m named LAB_TEST_CUBE. Do not modify any other object. Inspect the scene, capture a screenshot, verify the cube and dimensions, and report exact tool success/failure.
```

## Gate

Do not start SOLACE until:

```text
READ SCENE
+ SCREENSHOT
+ ONE CHANGE
+ SCREENSHOT
+ VERIFICATION
```

all succeed reliably.

## Astra later

When access is actually enabled, replace only the model selection and rerun the same health checks. Do not rebuild the MCP stack merely because the model changes.
