# Houdini AI Agent — 相关项目与工具

> 更新日期：2026-06-14
> 关联：[[Houdini都市PCG教程资源]] | [[PCG方向TA市场分析与UE项目调研]]

---

## 概述

SideFX 官方目前**尚未发布**原生的 "Houdini Copilot"，但社区已经涌现多个成熟的 AI Agent 项目，主流方案均基于 **MCP（Model Context Protocol）** 协议，将 Claude、GPT、DeepSeek 等 AI 连接到 Houdini 内部，实现自然语言驱动节点创建、VEX脚本生成、HDAs 封装等操作。

---

## 一、Houdini-Agent（社区最完善，开源）

> 目前功能最全的 Houdini 内置 AI Agent，**40+ 工具**，支持多模型

| 项目 | 详情 |
|---|---|
| **作者** | Kazama-Suichiku |
| **地址** | [github.com/Kazama-Suichiku/Houdini-Agent](https://github.com/Kazama-Suichiku/Houdini-Agent) |
| **要求** | Houdini 20.5+（测试至21.0+），Python 3.9+ |
| **支持模型** | DeepSeek V4、OpenAI GPT-5.x、Claude、Gemini、Ollama（本地）、OpenRouter |

### 三种工作模式

| 模式 | 说明 |
|---|---|
| **Agent（智能体）** | AI 全权控制，自动规划、调用工具、检查结果、迭代直至完成任务 |
| **Ask（问答）** | 只读模式，仅回答问题，不执行任何修改操作 |
| **Plan（计划）** | AI 先生成 DAG 流程图形式的执行计划 → 用户确认 → 逐节点执行 |

### 核心能力

| 工具类别 | 具体功能 |
|---|---|
| **节点操作** | 创建/修改/删除节点，连接节点，设置参数 |
| **VEX/Python 执行** | 实时编写并执行 VEX 或 Python 代码 |
| **场景管理** | 查看场景树、修改参数、捕捉视口截图 |
| **网络整理** | NetworkBox 打包、节点注释、颜色标记 |
| **语义搜索** | 用自然语言搜索节点（"给我找一个噪波节点"） |
| **性能分析** | 监控节点性能瓶颈 |
| **持久记忆** | 场景记忆、对话记忆，HSM 层次化状态机 |

### 与 PCG 的结合场景

```
自然语言描述 → AI Agent → Houdini 节点网络
     ↓
"生成一个带有随机窗户的建筑生成器"
     ↓
AI 自动创建 Attribute Create + PolyExtrude + Copy to Points + HDA 封装
```

---

## 二、fxhoudinimcp（MCP 服务器，168个工具）

> 最全面的 MCP 方案，Claude Desktop / Claude Code 即可直接控制 Houdini

| 项目 | 详情 |
|---|---|
| **作者** | healkeiser |
| **PyPI** | [pypi.org/project/fxhoudinimcp](https://pypi.org/project/fxhoudinimcp/) |
| **介绍** | [lobehub.com/mcp/healkeiser-fxhoudinimcp](https://lobehub.com/mcp/healkeiser-fxhoudinimcp) |
| **要求** | Houdini 20.5+，Python 3.10+ |
| **工具数** | **168 个工具** + 8 个资源 + 6 个工作流模板 |

### 覆盖范围

| 模块 | 工具数 |
|---|---|
| SOP（几何体操作） | 大量 |
| LOP / USD | 含完整 USD 管线 |
| DOP（动力学） | 物理模拟 |
| PDG / TOP | 分布式任务调度 |
| COP（2D图像） | 纹理处理 |
| HDA 管理 | 创建/封装/导出 |
| VEX 执行 | 实时代码运行 |
| 动画 / 渲染 | KineFX、Mantra、Redshift |
| 视口 / 缓存 | 视口控制、PBC 缓存 |

### 架构

```
Claude Desktop / Claude Code
      ↕ MCP 协议
fxhoudinimcp (MCP Server)
      ↕ hwebserver (Houdini 自带 WebSocket)
Houdini (hou.* API)
```

---

## 三、Houdini MCP Server（另一个 MCP 方案）

| 项目 | 详情 |
|---|---|
| **地址** | [himcp.ai/server/houdini-mcp-server-l5r](https://himcp.ai/server/houdini-mcp-server-l5r) |
| **通信** | TCP Socket，端口 9876 |
| **覆盖** | SOP / DOP / COP / CHOP / VOP / LOP / ROP 全上下文 |

---

## 四、Synapse Houdini

| 项目 | 详情 |
|---|---|
| **PyPI** | [pypi.org/project/synapse-houdini](https://pypi.org/project/synapse-houdini/5.3.0/) |
| **工具数** | 43 个 MCP 工具 |
| **特色** | 持久项目记忆、WebSocket 通信、**人机协同阀门**（INFORM / REVIEW / APPROVE / CRITICAL） |
| **其他** | RAG 文档路由、确定性执行 |

### 人机协同阀门

| 级别 | 说明 |
|---|---|
| INFORM | 通知用户但不需确认 |
| REVIEW | 执行前需审阅 |
| APPROVE | 需用户明确批准 |
| CRITICAL | 高敏操作需额外确认 |

---

## 五、Radu Cius — Houdini AI Assistant（独立开发中）

> Senior Houdini Artist & TD，2026 年持续开发中

| 项目 | 详情 |
|---|---|
| **内容** | Houdini AI Assistant |
| **Gumroad** | [rart.gumroad.com/l/HoudiniAIAssistant](https://rart.gumroad.com/l/HoudiniAIAssistant) |
| **测试** | 已测试 GPT-5.5 API，3D 理解 + 程序化推理 + 模拟工作流 |

### 子功能

| 模块 | 说明 |
|---|---|
| **Animation Maker** | 文字→角色动画（KineFX，BVH 导入+重定向） |
| **HDA Architect** | 自然语言→程序化生成器（输入"小行星生成器"自动创建） |
| **GPT-5.5 测试结果** | 能理解程序化逻辑，将 3D 思路拆解为节点网络 |

---

## 六、Bria AI — Houdini 原生生成式 AI（商业）

| 项目 | 详情 |
|---|---|
| **地址** | [tipranks.com 报道](https://www.tipranks.com/news/private-companies/bria-targets-vfx-workflows-with-native-generative-ai-integration-for-houdini) |
| **平台** | 基于 Houdini **Copernicus**（图像节点网络） |
| **节点数** | 13 个原生节点 |
| **特点** | 授权数据训练，可溯源，适合商业项目 |

---

## 七、Houdini 中国区 — AI 功能介绍

八方在线（SideFX 中国区代理）官方介绍中提及的 Houdini AI 特性：

| 特性 | 说明 |
|---|---|
| **AI 增强程序化建模** | DeepSeek、Claude 集成 |
| **智能合成数据生成** | 特斯拉地形生成、Amazon Robotics 机器人抓取数据 |
| **AI 优化实时动力学** | Muscles & Tissue（OTiS 求解器，比 Vellum 快 3倍） |
| **Neural Point Surface** | 点云→Mesh 神经网络重建 |
| **TOPs ML 管线** | 在 TOPs 中嵌入机器学习推理 |

---

## 八、使用场景对比

| 工具 | 适合谁 | 上手难度 | PCG价值 | 推荐度 |
|---|---|---|---|---|
| **Houdini-Agent** | 想在 Houdini 内有完整 Agent 体验的 TA | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **fxhoudinimcp** | 已用 Claude Code / Desktop 想控制 Houdini | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Houdini MCP Server** | 需要轻量 MCP 连接的开发者 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Synapse Houdini** | 需要严格审批流程的团队 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Radu AI Assistant** | 对文字→动画/HDAs 生成感兴趣的 | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Bria AI** | 商业影视项目 | ⭐ | ⭐⭐ | ⭐⭐ |

---

## 九、工作流示例：用 AI Agent 做都市 PCG

```
场景：用自然语言生成一个城市方块建筑群

输入：
"创建一个城市街区生成器，每个街区随机高度8-30层，
  顶层有随机屋顶样式，给建筑物侧面添加随机窗户"

流程（Houdini-Agent 或 fxhoudinimcp）：

Step 1: AI 创建 Grid → Attribute Randomize（高度）→ PolyExtrude
Step 2: AI 分析结果 → "屋顶太平，需要变体"
Step 3: AI 添加 Labs Building Generator → 配置窗户参数
Step 4: AI 添加 Copy to Points → 随机旋转散布
Step 5: AI 封装为 HDA → 暴露高度/密度/窗户密度参数
Step 6: 完成，一个可复用的城市建筑生成器就绪
```

---

## 十、学习资源

| 资源 | 地址 |
|---|---|
| Houdini-Agent 官方文档 | [GitHub README](https://github.com/Kazama-Suichiku/Houdini-Agent) |
| fxhoudinimcp 安装 | `pip install fxhoudinimcp` |
| B站 Houdini AI 助手介绍 | [BV1eqP2zEEhG](https://www.bilibili.com/video/BV1eqP2zEEhG/) |
| SideFX 论坛讨论 | [sidefx.com/forum/topic/103071](https://www.sidefx.com/forum/topic/103071/) |
| Houdini 22 HIVE 大会 | 2026.6.17-18 伦敦，官方直播 6.22 |

---

## 小结

当前 Houdini AI Agent 生态：

| 状态 | 说明 |
|---|---|
| ✅ **已可用** | 3 个 MCP 方案（fxhoudinimcp、Houdini MCP、Synapse）均可直接用 Claude 控制 Houdini |
| ✅ **已可用** | Houdini-Agent 提供完整的 Houdini 内嵌 AI Agent 体验 |
| 🔄 **开发中** | Radu Cius 的 Houdini AI Assistant（文字→HDAs） |
| 🔄 **期待中** | SideFX 官方是否推出原生 Copilot（社区已多次呼吁） |
| ✅ **商业可用** | Bria AI for Houdini（Copernicus 原生节点） |
