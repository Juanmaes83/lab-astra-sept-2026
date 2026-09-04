# 01 — Current State

Date: 2026-09-04

## Environment verified

- Windows 11 Pro / x64.
- Node `v24.14.1`.
- npm `11.14.1`.
- Codex CLI `0.153.2`.
- Codex Doctor: healthy overall; 0 failures.
- Codex auth mode: ChatGPT.
- Working configured model: `gpt-5.6-sol`.
- MCP servers already detected by Codex; one unrelated Cloudflare MCP may require login/disable cleanup.

## Astra access verification

### Direct OpenAI API
Observed result for `gpt-6-astra`:

```text
404 model_not_found
```

Interpretation: current API project is not provisioned for Astra yet.

### Codex with ChatGPT authentication
Launching Codex with `-m gpt-6-astra` reaches the client UI, but real inference returns:

```text
400 invalid_request_error
The 'gpt-6-astra' model is not supported when using Codex with a ChatGPT account.
```

Interpretation: Astra is not currently usable in this Codex/ChatGPT route either.

## Decision

Do not spend more project time attempting to force rollout access.

Proceed with `gpt-5.6-sol` and keep all orchestration/model selection configurable so Astra can later replace Sol without rebuilding the Blender/MCP/world pipeline.

## Blender MCP state

Source LAB already prepared in:

`Juanmaes83/blender-mcp` → branch `lab/astra-sept-2026`

That branch is based on the September 2026 Blender MCP upstream line and includes the Safe Mode work.

Next integration gate:

```text
CODEX/SOL
→ BLENDER MCP
→ BLENDER
→ READ SCENE
→ CAPTURE SCREENSHOT
→ SMALL CHANGE
→ CAPTURE / VERIFY
```

## Media / benchmark references

SOLACE / Thomas-Astra reference material belongs in this repository as benchmark evidence. Original binaries can be uploaded manually to avoid connector limitations, with a manifest committed alongside them.
