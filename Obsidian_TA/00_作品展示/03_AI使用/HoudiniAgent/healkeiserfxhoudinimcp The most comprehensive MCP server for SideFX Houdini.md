---
title: "healkeiser/fxhoudinimcp: The most comprehensive MCP server for SideFX Houdini."
source: "https://github.com/healkeiser/fxhoudinimcp"
author:
published:
created: 2026-07-13
description: "The most comprehensive MCP server for SideFX Houdini. - healkeiser/fxhoudinimcp"
tags:
  - "clippings"
---
[![Houdini](https://camo.githubusercontent.com/8323de711059bfc47c5c59a3545bf15e3600edba801de06c3845d8182b3730c4/68747470733a2f2f63646e2e73696d706c6569636f6e732e6f72672f686f7564696e692f464634373133)](https://camo.githubusercontent.com/8323de711059bfc47c5c59a3545bf15e3600edba801de06c3845d8182b3730c4/68747470733a2f2f63646e2e73696d706c6569636f6e732e6f72672f686f7564696e692f464634373133) [![MCP](https://camo.githubusercontent.com/c25b1f53ae8bb4c8457f723e0c91ca1ac4bd61c58ab2a7ff426092299d563d4d/68747470733a2f2f63646e2e73696d706c6569636f6e732e6f72672f6d6f64656c636f6e7465787470726f746f636f6c2f666666666666)](https://camo.githubusercontent.com/c25b1f53ae8bb4c8457f723e0c91ca1ac4bd61c58ab2a7ff426092299d563d4d/68747470733a2f2f63646e2e73696d706c6569636f6e732e6f72672f6d6f64656c636f6e7465787470726f746f636f6c2f666666666666)

### fxhoudinimcp

The most comprehensive MCP server for SideFX Houdini.  
179 tools across 22 categories, covering every major Houdini context.  

## Table of Contents

## About

A comprehensive [MCP](https://modelcontextprotocol.io/) (Model Context Protocol) server for [SideFX Houdini](https://www.sidefx.com/). Connects AI assistants like Claude directly to Houdini's Python API, enabling natural language control over scene building, simulation setup, rendering, and more.

**179 tools**, **8 resources**, and **6 workflow prompts** out of the box.

## Features

| Category | Tools | Description |
| --- | --- | --- |
| **Graph Intelligence** | 4 | Atomic validated network building, network verification, node doc cards, cook profiling |
| **Documentation** | 2 | Full-text search + page retrieval over Houdini's own shipped manual (version-exact) |
| **Scene Management** | 7 | Open, save, import/export, scene info |
| **Node Operations** | 17 | Create, delete, copy, connect, layout, flags |
| **Parameters** | 11 | Get/set values, expressions, keyframes, spare parameters |
| **Geometry (SOPs)** | 12 | Points, prims, attributes, groups, sampling, nearest-point search |
| **LOPs/USD** | 18 | Stage inspection, prims, layers, composition, variants, lighting |
| **DOPs** | 8 | Simulation info, DOP objects, step/reset, memory usage |
| **PDG/TOPs** | 10 | Cook, work items, schedulers, dependency graphs |
| **COPs (Copernicus)** | 7 | Image nodes, layers, VDB data |
| **HDAs** | 10 | Create, install, manage Digital Assets and their sections |
| **Animation** | 9 | Keyframes, playbar control, frame range |
| **Rendering** | 9 | Viewport capture, render nodes, settings, render launch |
| **VEX** | 5 | Create/edit wrangles, validate VEX code |
| **Code Execution** | 4 | Python, HScript, expressions, env variables |
| **Viewport/UI** | 13 | Pane management, screenshots, status messages, error detection |
| **Scene Context** | 8 | Network overview, cook chain, selection, scene summary, error analysis |
| **Workflows** | 8 | One-call Pyro/RBD/FLIP/Vellum setup, SOP chains, render config |
| **Materials** | 5 | List, inspect, create materials and shader networks |
| **CHOPs** | 4 | Channel data, CHOP nodes, export channels to parameters |
| **Cache** | 4 | List, inspect, clear, write file caches |
| **Takes** | 4 | List, create, switch takes with parameter overrides |

## Architecture

```
flowchart LR
    subgraph Client[" 🤖 AI Client "]
        direction TB
        A1("Claude Desktop")
        A2("Cursor / VS Code")
        A3("Claude Code")
    end

    subgraph MCP[" ⚡ FXHoudini MCP Server "]
        direction TB
        B1("🔧 179 tools")
        B2("📦 8 Resources")
        B3("💬 6 Prompts")
    end

    subgraph Houdini[" 🔶 SideFX Houdini "]
        direction TB
        C1("🌐 hwebserver")
        C2("📡 Dispatcher")
        C3("🎛️ hou.* Handlers")
        C1 --> C2 --> C3
    end

    Client -. "MCP Protocol · stdio" .-> MCP
    MCP -. "HTTP / JSON · port 8100" .-> Houdini

    classDef clientBox fill:#f0f4ff,stroke:#b8c9e8,stroke-width:1px,color:#2d3748,rx:12,ry:12
    classDef mcpBox fill:#eef6f0,stroke:#a8d5b8,stroke-width:1px,color:#2d3748,rx:12,ry:12
    classDef houdiniBox fill:#fff5f0,stroke:#e8c4a8,stroke-width:1px,color:#2d3748,rx:12,ry:12

    classDef clientNode fill:#dbe4f8,stroke:#96b0dc,stroke-width:1px,color:#2d3748,rx:8,ry:8
    classDef mcpNode fill:#d4edda,stroke:#82c896,stroke-width:1px,color:#2d3748,rx:8,ry:8
    classDef houdiniNode fill:#fde4d0,stroke:#e0a87c,stroke-width:1px,color:#2d3748,rx:8,ry:8

    class Client clientBox
    class MCP mcpBox
    class Houdini houdiniBox
    class A1,A2,A3 clientNode
    class B1,B2,B3 mcpNode
    class C1,C2,C3 houdiniNode
```

Uses Houdini's built-in `hwebserver`. No custom socket servers, no rpyc. Uses `hdefereval.executeInMainThreadWithResult()` to safely run `hou.*` calls on the main thread.

## Installation

### Requirements

- **Houdini** 20.5+ (tested on 21.0)
- **Python** 3.10+
- **MCP SDK** (`mcp` package) 1.8+

### 1\. Install the MCP Server

**From PyPI:**

```
pip install fxhoudinimcp
```

**From source:**

```
pip install -e .
```

Or with development dependencies:

```
pip install -e ".[dev]"
```

### 2\. Install the Houdini Plugin

**Option A: Houdini package (recommended)**

1. Copy `houdini/fxhoudinimcp.json` to your Houdini packages directory:
	- Windows: `%USERPROFILE%/Documents/houdiniXX.X/packages/`
		- Linux: `~/houdiniXX.X/packages/`
		- macOS: `~/Library/Preferences/houdini/XX.X/packages/`
2. Edit the JSON file to set `FXHOUDINIMCP` to point to the `houdini` directory in this repo.

**Option B: Manual copy**

Copy the contents of `houdini/` into your Houdini user preferences directory so that:

- `scripts/python/fxhoudinimcp_server/` is on Houdini's Python path
- `python3.Xlibs/uiready.py` auto-starts the server (copy the folder matching your Houdini's Python version)
- `toolbar/fxhoudinimcp.shelf` appears in your shelf

### 3\. Configure Your MCP Client

**Claude Desktop** (`claude_desktop_config.json`):

```
{
  "mcpServers": {
    "fxhoudini": {
      "command": "python",
      "args": ["-m", "fxhoudinimcp"],
      "env": {
        "HOUDINI_HOST": "localhost",
        "HOUDINI_PORT": "8100"
      }
    }
  }
}
```

**Claude Code** (global — available in every project):

```
claude mcp add --scope user fxhoudini -- python -m fxhoudinimcp
```

Or to scope it to a single project, add a `.mcp.json` in the project root:

```
{
  "mcpServers": {
    "fxhoudini": {
      "command": "python",
      "args": ["-m", "fxhoudinimcp"]
    }
  }
}
```

> [!tip] Tip
> If Claude Desktop reports the server as **disconnected**, replace `"python"` with the **full absolute path** to your Python executable. Claude Desktop does not always inherit your system PATH. Find it with:
> 
> ```
> python -c "import sys; print(sys.executable)"
> ```
> 
> Then use the result in your config, e.g. `"command": "C:\\Program Files\\Python311\\python.exe"`. After any config change, fully quit Claude Desktop (system tray → Quit) and relaunch.

## Usage

Launch Houdini normally. The plugin auto-starts once when the UI is ready (controlled by `FXHOUDINIMCP_AUTOSTART` env var). The startup script uses `uiready.py`, which stacks correctly with other Houdini packages. You can also toggle it manually via the **MCP Server** shelf tool.

Startup verifies that Houdini's `mcp.health` endpoint answers from the current Houdini process before printing that the server is ready. If your assistant cannot reach Houdini after an app restart, call `get_houdini_connection_status` for structured diagnostics, then relaunch Houdini or align `FXHOUDINIMCP_PORT` and `HOUDINI_PORT` if another process owns the port.

Once connected, your AI assistant can:

```
"Create a procedural rock generator with mountain displacement"
"Set up a Pyro simulation with a sphere source"
"Build a USD scene with a camera, dome light, and ground plane"
"Create an HDA from the selected subnet"
"Debug why my scene has cooking errors"
```

## Environment Variables

| Variable | Default | Description |
| --- | --- | --- |
| `HOUDINI_HOST` | `localhost` | Houdini host address |
| `HOUDINI_PORT` | `8100` | Houdini hwebserver port |
| `FXHOUDINIMCP_PORT` | `8100` | Port for the Houdini plugin to listen on |
| `FXHOUDINIMCP_AUTOSTART` | `1` | Set to `0` to disable auto-start |
| `FXHOUDINIMCP_AUTO_LAYOUT` | `1` | Set to `0` to disable automatic node layout (preserves manual layouts) |
| `MCP_TRANSPORT` | `stdio` | MCP transport (`stdio` or `streamable-http`) |
| `LOG_LEVEL` | `INFO` | Logging level |

## Development

```
# Install dev dependencies
pip install -e ".[dev]"

# Run linter
ruff check python/

# Run tests
pytest

# Run integration tests inside a real Houdini (requires a license seat;
# uses the newest installed Houdini, override with the HYTHON env var).
# Works on Windows, macOS, and Linux:
python tests/run_integration.py
# Convenience wrappers: tests/run_integration.ps1 / tests/run_integration.sh
```

Unit tests mock `hou` and run anywhere. The integration suite in `tests/integration/` executes all 179 commands against live Houdini via `hython` — including end-to-end user scenarios (procedural modeling, simulation, animation, lookdev) — and prints per-command timing and coverage reports; it is skipped automatically when `hou` is not available. `tests/integration/perf_sweep.py` benchmarks handlers on large scenes, and `python tests/integration/bridge_e2e.py` validates the full HTTP transport (real hwebserver in hython driven by the MCP server's own bridge).

### How It Works

1. **Houdini Plugin** (`houdini/`): Runs inside Houdini's Python environment. Registers `@hwebserver.apiFunction` endpoints that receive JSON commands. Uses `hdefereval.executeInMainThreadWithResult()` to safely execute `hou.*` calls on the main thread.
2. **MCP Server** (`python/fxhoudinimcp/`): A standalone Python process using FastMCP. Exposes 179 tools, 8 resources, and 6 prompts via the MCP protocol. Forwards tool calls to Houdini over HTTP.
3. **Bridge** (`python/fxhoudinimcp/bridge.py`): Async HTTP client that sends commands to Houdini's hwebserver and deserializes responses. Handles connection errors and timeouts.