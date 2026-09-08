# 07 — Blender + Codex Setup

## Purpose

Connect **GPT-6 Astra in Codex CLI** to the September Blender MCP LAB and prove the first bounded read → act → capture → verify loop.

## Source Blender MCP

Use:

`Juanmaes83/blender-mcp` → branch `lab/astra-sept-2026`

That branch is the technical MCP implementation source. This repository remains the higher-level experiment/orchestration repo.

## Windows prerequisites

Already observed on the project owner's machine:

- Node / npm available.
- Codex CLI installed.
- Codex authenticated through ChatGPT.
- `gpt-6-astra` launches successfully.

Codex npm path previously observed:

```text
C:\Users\temp123\AppData\Roaming\npm\codex.cmd
```

If `codex` is not on PATH in a new PowerShell session:

```powershell
$env:Path += ";C:\Users\temp123\AppData\Roaming\npm"
codex.cmd --version
```

## Clone/update Blender MCP LAB

If not cloned:

```powershell
cd $HOME\Documents
git clone --branch lab/astra-sept-2026 --single-branch https://github.com/Juanmaes83/blender-mcp.git blender-mcp-astra-lab
cd blender-mcp-astra-lab
```

If already cloned:

```powershell
cd $HOME\Documents\blender-mcp-astra-lab
git fetch origin
git checkout lab/astra-sept-2026
git pull --ff-only origin lab/astra-sept-2026
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

The Blender MCP server must appear healthy before mutation tests.

## Launch Astra inside the LAB

Open PowerShell in the orchestration repo:

```powershell
cd $HOME\Documents\ChatGPT\lab-astra-sept-2026
codex -m gpt-6-astra
```

Confirm the session header reports:

```text
model: gpt-6-astra
```

## Gate 1A — Read only

Inside Codex/Astra:

```text
Read AGENTS.md and docs/07-BLENDER-CODEX-SETUP.md first.
Use the configured Blender MCP server.
Inspect the currently open Blender scene. Do not modify anything.
Report all scene objects and their transforms/dimensions when available.
Capture one viewport screenshot.
Verify that the textual scene report matches the screenshot.
Save no destructive changes.
Report exact MCP/tool success or failure.
```

PASS requires:
- MCP call succeeds;
- scene can be inspected;
- viewport capture succeeds;
- report and screenshot are coherent.

## Gate 1B — One bounded mutation

Only after Gate 1A passes:

```text
Create exactly one cube named LAB_TEST_CUBE with dimensions exactly 2m x 2m x 2m.
Do not modify any pre-existing object.
After creation, inspect LAB_TEST_CUBE and verify its dimensions/transforms.
Capture a new viewport screenshot showing the cube.
Compare the new state with the previous read-only capture.
If the dimensions or result are wrong, correct only LAB_TEST_CUBE and recapture.
Report exact success/failure and evidence paths.
```

PASS requires:
- only the bounded object is introduced/changed;
- dimensions are verified as 2 × 2 × 2 m;
- second capture proves the change;
- no unrelated objects were modified.

## Gate 1 evidence

Record evidence in:

```text
evidence/gate-1/
```

Minimum record:
- `00-scene-before.png`
- `01-scene-after.png`
- `gate-1-result.md`

Do not commit a `.blend` file containing secrets/private source material without explicit review.

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

## Model rule

Astra is the current execution model, but the workflow remains model-swappable. A later model change must not require rebuilding the MCP/Blender stack.