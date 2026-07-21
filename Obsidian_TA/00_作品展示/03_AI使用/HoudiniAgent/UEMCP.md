**Unreal Engine 5.8（UE 5.8）最新 MCP（Model Context Protocol）功能介绍**（实验性特性）。

### 什么是 MCP？
**MCP（Model Context Protocol）** 是一个开放标准协议（详见 modelcontextprotocol.io），允许 AI 代理（LLM 系统，如 Claude Code、Cursor 等）通过本地 HTTP 连接直接与 Unreal Editor 交互。


它将 Unreal Engine 的各种功能暴露为 **Tools**（工具函数）、**Resources**（只读资源）和 **Prompts**（提示模板），让 AI 能真正“理解”引擎和你的项目，并帮助你自动化操作。

Unreal MCP 在 UE 5.8 中以**实验性插件**形式内置，直接嵌入 Editor 进程中运行（无需额外服务器）。AI 可以：
- 生成/修改资产（Blueprints、材质、网格、关卡等）
- 放置 Actor、配置灯光、创建材质实例
- 运行自动化测试、优化任务
- 扩展引擎功能
- 进行场景构建、程序化生成等

**核心优势**：AI 成为真正的“协作者”，支持自然语言驱动编辑器操作。

### 主要特性
- **内置 Toolsets**：暴露核心系统（如 ActorTools、SceneTools、MaterialInstanceTools、ObjectTools 等），覆盖 Blueprints、资产、关卡、材质、网格等。
- **Toolset Registry**：插件系统，支持开发者轻松用 **Python** 或 **C++** 自定义 Toolset（推荐 Python，门槛低）。
- **安全与同步**：工具调用在游戏线程串行执行，避免冲突；默认仅本地连接（127.0.0.1），无远程认证。
- **兼容性**：支持 Claude Code、Cursor、VS Code、Gemini 等 MCP 兼容 AI 客户端。
- **扩展性**：易于添加自定义工具，未来会持续迭代（当前许多功能仍不完整，API 可能变化）。

**注意**：这是实验特性，**不建议用于生产/发货项目**，使用时需谨慎。

### 如何快速启用（Setup）
1. **启用插件**：Edit → Plugins → 搜索 “Unreal MCP” 启用（会自动启用 Toolset Registry），重启 Editor。
2. **配置自动启动**：Edit → Editor Preferences → General → Model Context Protocol → 开启 **Auto Start Server**（默认端口 8000，URL `/mcp`）。
3. **生成客户端配置**：在 Editor 控制台输入：
   ```
   ModelContextProtocol.GenerateClientConfig ClaudeCode   # 或 All（支持多个）
   ```
   这会在项目根目录生成 `.mcp.json` 文件。
4. **连接 AI**：从项目根目录启动你的 AI 客户端（如 Claude Code），即可交互。
   - 测试提示示例：“What actors do I have selected?” 或 “What are a few things you can do in Unreal?”

**可选**：启用 Terminal 插件，在 Editor 内直接运行 AI CLI，实现全流程一体化。

### 自定义扩展
- **Python Toolset**：放在插件的 `Content/Python/` 下，继承 `unreal.ToolsetDefinition`，用 `@toolset_registry.tool_call` 装饰函数。
- **C++ Toolset**：继承 `UToolsetDefinition`，用 `UFUNCTION(meta = (AICallable))`。
- 修改后运行 `ModelContextProtocol.RefreshTools` 刷新。

### 更多资源
- 官方文档：Unreal MCP in Unreal Editor（Epic Developer Community）。
- UE 5.8 发布公告：重点介绍了此 AI 集成特性。

MCP 是 UE 5.8 中 AI 驱动开发的重要里程碑，能显著提升迭代效率。如果你需要具体教程、自定义工具示例或设置帮助，可以提供更多细节！