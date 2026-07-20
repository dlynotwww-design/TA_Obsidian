如果你的目标不是**“AI 做 NPC”**，而是希望学习**AI 参与整个 Godot 游戏开发流程（需求→架构→代码→美术→测试→迭代）**，GitHub 上已经出现了一批非常优秀的项目。

下面按照完整开发流程整理。

---

# 一、最推荐（★★★★★）

## 1. Godot AI（目前最成熟）

**GitHub：**

**hi-godot/godot-ai**

> [https://github.com/hi-godot/godot-ai](https://github.com/hi-godot/godot-ai)

特点：

- MCP（Model Context Protocol）
    
- Claude Code
    
- Cursor
    
- Codex
    
- Gemini
    
- ChatGPT
    
- Windsurf
    

全部支持。

它最大的特点不是聊天，而是：

AI 可以直接操作 Godot Editor。

例如：

```
Create a player.

↓

AI

创建 Scene
创建 CharacterBody2D
添加 Collision
添加 Camera
绑定 Script
配置 Input
运行游戏
修复错误
```

甚至可以：

- 创建 Shader
    
- Animation
    
- TileMap
    
- UI
    
- Audio
    
- Particle
    
- Material
    
- Scene Tree
    

几乎整个 Editor 都能控制。([GitHub](https://github.com/hi-godot/godot-ai?utm_source=chatgpt.com "GitHub - hi-godot/godot-ai: Production-grade MCP server and AI tools for the Godot engine. A Snap to install. Totally free and fun. · GitHub"))

---

## 2. Godot AI Builder

GitHub：

HubDev-AI/godot-ai-builder

[https://github.com/HubDev-AI/godot-ai-builder](https://github.com/HubDev-AI/godot-ai-builder)

这是目前最接近

> "一句话生成游戏"

的项目。

它把整个开发拆成六个阶段：

```
① Game Idea

↓

② PRD

↓

③ Architecture

↓

④ Gameplay

↓

⑤ UI

↓

⑥ Polish
```

例如：

```
Make a Vampire Survivor.

↓

AI

写PRD

↓

建立Scene

↓

写Player

↓

Enemy

↓

Weapon

↓

升级

↓

UI

↓

保存系统

↓

自动运行

↓

自动修Bug
```

整个流程基本自动完成。([GitHub](https://github.com/HubDev-AI/godot-ai-builder?utm_source=chatgpt.com "GitHub - HubDev-AI/godot-ai-builder: A Claude Code plugin that generates playable Godot 4 games from natural language prompts. · GitHub"))

---

# 二、AI Coding Workflow（推荐）

## 3. GodotPrompter

GitHub：

jame581/GodotPrompter

[https://github.com/jame581/GodotPrompter](https://github.com/jame581/GodotPrompter)

这个项目不是生成代码。

而是：

给 Claude/Cursor 提供

Godot 专业知识。

例如：

```
State Machine

↓

AI 自动采用 Godot 推荐架构
```

```
Multiplayer

↓

自动使用官方推荐写法
```

包含：

45+ Skills

例如：

- UI
    
- Animation
    
- Shader
    
- Multiplayer
    
- Save
    
- Physics
    
- Optimization
    
- ECS
    
- Procedural Generation
    

非常适合作为 AI Agent 的知识库。([GitHub](https://github.com/jame581/GodotPrompter?utm_source=chatgpt.com "GitHub - jame581/GodotPrompter: Agentic skills framework for Godot 4.x. Domain-specific skills for AI coding agents (Claude Code, Copilot, Gemini, Cursor) · GitHub"))

---

## 4. GDAgent

官网：

[https://gdagent.dev](https://gdagent.dev/)

GitHub：

[https://github.com/gd-agent（持续更新）](https://github.com/gd-agent%EF%BC%88%E6%8C%81%E7%BB%AD%E6%9B%B4%E6%96%B0%EF%BC%89)

特点：

AI Terminal

直接嵌入 Godot。

工作流：

```
Godot

↓

Terminal

↓

Claude

↓

修改Scene

↓

运行

↓

Debug

↓

继续修改
```

减少来回复制粘贴。([GDAgent](https://gdagent.dev/blog/2026-02-17-introducing-gdagent/?utm_source=chatgpt.com "Introducing GDAgent: Bringing AI to the Godot Editor - GDAgent Blog"))

---

# 三、运行时 AI（Runtime）

## Godot LLM

GitHub：

Adriankhl/godot-llm

[https://github.com/Adriankhl/godot-llm](https://github.com/Adriankhl/godot-llm)

不是开发工具。

而是：

游戏里运行 LLM。

例如：

NPC：

```
玩家：

你好。

NPC：

你好旅行者。
```

支持：

- llama.cpp
    
- Embedding
    
- RAG
    
- Vector Database
    

甚至：

```
NPC

↓

记忆玩家

↓

长期记忆

↓

剧情生成
```

适合 RPG。([GitHub](https://github.com/Adriankhl/godot-llm?utm_source=chatgpt.com "GitHub - Adriankhl/godot-llm: LLM in Godot · GitHub"))

---

# 四、完整 AI Workflow

## Aesthetic Engine

官网：

[https://aestheticengine.games](https://aestheticengine.games/)

特点：

真正意义上的

AI Agent Workflow。

整个流程：

```
Idea

↓

PRD

↓

Prompt

↓

生成Scene

↓

运行

↓

观察Runtime

↓

发现Bug

↓

修改

↓

重新运行
```

强调：

Closed Loop

即：

AI

不仅生成，

还能观察游戏运行结果，

然后继续修改。([Aesthetic Engine](https://aestheticengine.games/?utm_source=chatgpt.com "Aesthetic Engine | Aesthetic Engine"))

---

# 五、AI + 项目理解

## Godot Project Scanner

GitHub：

okp74103-ops/godot-ai-workflow-showcase

特点：

很多 AI：

不知道项目结构。

Scanner 会：

```
Project

↓

扫描

↓

JSON

↓

Markdown

↓

AI 阅读

↓

开始修改
```

非常适合：

大型 Godot 项目。([Reddit](https://www.reddit.com/r/u_Affectionate_Quit243/comments/1ud1ou8/i_built_a_godot_project_scanner_to_give_ai_tools/?utm_source=chatgpt.com "I built a Godot project scanner to give AI tools structured project context"))

---

# 六、真正的 AI 自动开发案例

Reddit：

AI Agent Built Tower Defense

流程：

```
Prompt

↓

AI

↓

创建地图

↓

摆Tile

↓

写Enemy

↓

写Tower

↓

写UI

↓

写Upgrade

↓

写Wave

↓

找错误

↓

自动修复

↓

完成
```

几乎没有人工操作。

这是目前比较完整的 AI Agent 实战案例之一。([Reddit](https://www.reddit.com/r/aigamedev/comments/1s48ckl/ai_agent_built_a_complete_tower_defense_in_godot/?utm_source=chatgpt.com "AI agent built a complete tower defense in Godot, placed every tile, wrote every script, even found its own sound effects"))

---

# 七、如果你想学习「完整项目开发」，建议按这个顺序

```text
游戏策划（PRD）
        │
        ▼
Claude / ChatGPT
        │
        ▼
生成 Game Design Doc
        │
        ▼
Godot AI Builder
        │
        ▼
生成 Scene
        │
        ▼
Godot AI
        │
        ▼
编辑 Scene
        │
        ▼
GodotPrompter
        │
        ▼
生成高质量 GDScript
        │
        ▼
Godot LLM
        │
        ▼
NPC / Dialogue / Quest
        │
        ▼
Runtime Test
        │
        ▼
AI 自动 Debug
        │
        ▼
最终游戏
```

---

# 八、我推荐的学习路线（按价值排序）

|项目|推荐指数|学习重点|
|---|---|---|
|Godot AI|⭐⭐⭐⭐⭐|AI 控制 Godot 编辑器、MCP 工作流|
|Godot AI Builder|⭐⭐⭐⭐⭐|从自然语言到完整游戏的六阶段流程|
|GodotPrompter|⭐⭐⭐⭐☆|Godot 专业开发规范与 AI 技能库|
|Godot LLM|⭐⭐⭐⭐☆|NPC、RAG、对话与游戏内 AI|
|Aesthetic Engine|⭐⭐⭐⭐☆|闭环 Agent 开发、运行时观察与迭代|
|Godot Project Scanner|⭐⭐⭐⭐☆|大型项目上下文分析与 AI 协作|

---

**结合你之前的目标（Godot + 独立游戏 + AI 开发）**，我还可以整理一份 **50+ 个 GitHub 开源项目清单**，覆盖完整生产链，包括：

- AI 自动生成游戏（Agent）
    
- AI 美术（ComfyUI、Stable Diffusion、Pixel Art）
    
- AI 动画（Sprite、骨骼、Live2D）
    
- AI 音效与配乐
    
- AI NPC（LLM、RAG、记忆系统）
    
- AI 地图生成（WFC、PCG、Wave Function Collapse）
    
- AI 测试（自动游玩、自动 Bug 检测）
    
- AI 游戏平衡（数值分析、强化学习）
    
- Godot 完整开源游戏（可直接学习项目架构）
    

这套资源基本可以覆盖从创意到发布的完整 AI 游戏开发流程。