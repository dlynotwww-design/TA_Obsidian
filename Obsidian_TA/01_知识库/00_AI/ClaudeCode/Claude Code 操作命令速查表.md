---
created: 2026-06-27
tags:
  - claude-code
  - 速查
  - AI工具
---

# Claude Code 操作命令速查表

## 一、日常高频命令

| 命令 | 作用 |
|------|------|
| `/status` | 查看当前会话配置（模型、目录、Token 用量） |
| `/context` | 查看 Context 用量详情 |
| `/clear` | 清空当前会话，重置对话历史 |
| `/compact` | 压缩当前会话（保留关键上下文，释放 Token） |
| `/cost` | 查看当前会话的 API 费用消耗 |
| `/init` | 扫描当前目录，自动生成 CLAUDE.md 项目记忆文件 |
| `Shift+Tab` | 切换三种工作模式：**Normal / Plan / Auto** |

## 二、模式切换

| 模式 | 快捷键 | 说明 |
|------|--------|------|
| Normal | `Shift+Tab` 切到 Normal | 标准对话模式，边问边做 |
| Plan | `Shift+Tab` 切到 Plan | 先规划再执行，大任务推荐 |
| Auto | `Shift+Tab` 切到 Auto | 全自动模式，Claude 自主决策和操作 |

> **建议**：80% 的任务在 Plan Mode 跑，避免 Auto Mode 直接跑复杂任务导致出错率飙升。

## 三、文件引用

| 操作 | 说明 |
|------|------|
| `@filename.md` | 引用项目中的文件，Claude 会自动读取 |
| `@folder/` | 引用整个目录 |
| `@CLAUDE.md` | 引用项目记忆文件（内联级优先级最高） |
| 拖拽文件到终端 | 自动生成 `@` 引用路径 |

## 四、会话管理

| 命令 | 作用 |
|------|------|
| `/resume` | 恢复上次会话 |
| `/doctor` | 诊断 Claude Code 环境配置问题 |
| `/setup` | 重新运行初始化设置 |
| `/login` | 切换或重新登录 Anthropic 账号 |
| `/logout` | 退出登录 |
| `Ctrl+C` | 中断当前正在执行的命令/循环 |
| `Ctrl+D` | 退出 Claude Code 会话 |
| `Esc` | 退出当前输入（权限确认弹窗等） |

## 五、子代理与多代理协作

| 命令/操作 | 作用 |
|------|------|
| `--agents` 参数 | 启动时指定子代理数量 |
| `/agents` | 查看当前子代理状态 |
| Agent Tool 调用 | 在对话中让 Claude 启动子代理处理并行任务 |

> **Skills 管流程，MCP 管连接，子代理管分工。**

## 六、Skills 管理

| 命令/操作 | 说明 |
|------|------|
| 安装 Skill | 将 Skill 文件夹放入 `.claude/skills/` 目录 |
| 触发 Skill | 说对应关键词，Claude 自动扫描并激活匹配的 Skill |
| 用户级 Skills | `~/.claude/skills/` （全局可用） |
| 项目级 Skills | `<project>/.claude/skills/` （仅当前项目） |

## 七、MCP 服务器

| 命令 | 作用 |
|------|------|
| `/mcp` | 查看已连接的 MCP 服务器列表 |
| `/mcp add` | 添加 MCP 服务器 |
| `/mcp remove` | 移除 MCP 服务器 |
| `/mcp reconnect` | 重连 MCP 服务器 |

## 八、CLAUDE.md 四层记忆

| 优先级 | 位置 | 作用范围 |
|--------|------|----------|
| 最高（就近覆盖） | 内联 `@CLAUDE.md` | 当前对话临时说明 |
| 高 | 子目录 `CLAUDE.md` | 该子目录及下层 |
| 中 | 项目根 `CLAUDE.md` | 整个项目 |
| 低 | `~/.claude/CLAUDE.md` | 所有项目 |

## 九、权限管理

| 命令 | 作用 |
|------|------|
| `/permissions` | 查看/管理权限配置 |
| 对话中按 `A` | 允许当前操作（Allow） |
| 对话中按 `D` | 拒绝当前操作（Deny） |
| 对话中按 `Y` | 始终允许此类操作（Always allow） |

## 十、会话配置

| 命令/参数 | 作用 |
|------|------|
| `--model` | 启动时指定模型 (sonnet/opus/haiku) |
| `--verbose` | 启动时开启详细日志 |
| `--debug` | 启动时开启调试模式 |
| `/config` | 查看/修改配置 |
| `/theme` | 切换终端主题 |
| `/model` | 切换当前会话使用的模型 |

## 十一、急救三步（卡死时用）

| 步骤 | 操作 |
|------|------|
| 1. 中断 | `Ctrl+C` 掐掉正在跑的循环 |
| 2. 清空 | `/clear` 清掉全部历史包袱 |
| 3. 重述 | 基于刚才学到的"它会卡在哪"，把 Prompt 写得更具体 |

## 十二、五大常见错误

| # | 错误 | 解决 |
|----|------|------|
| 1 | Token 烧爆 | 用 `/compact` 或 `/clear` |
| 2 | 没 Plan 直接 Auto | 80% 任务在 Plan Mode 跑 |
| 3 | 没写 CLAUDE.md | 进项目先 `/init` |
| 4 | `@` 错大文件 | `@` 之前确认文件是否真的需要 |
| 5 | 一个对话塞五件事 | 一个 Prompt 一件事 |

---

> 📚 来源：花叔《Claude Code 橙皮书》[GitHub](https://github.com/alchaincyf/claude-code-orange-book)
