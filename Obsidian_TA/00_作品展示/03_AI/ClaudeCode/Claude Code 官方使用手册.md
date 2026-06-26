---
created: 2026-06-27
updated: 2026-06-27
tags:
  - claude-code
  - 参考手册
  - AI工具
source: "https://code.claude.com/docs"
---

# Claude Code 官方使用手册

> 基于 [Anthropic 官方文档](https://code.claude.com/docs) 整理，涵盖 CLI 命令、交互模式、配置设置、Skills 等全部功能。

---

## 一、安装与启动

### 安装

```bash
# macOS / Linux / WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex

# macOS Homebrew（稳定版）
brew install --cask claude-code

# macOS Homebrew（最新版）
brew install --cask claude-code@latest

# Windows WinGet
winget install Anthropic.ClaudeCode
```

### 基本启动

| 命令 | 说明 |
|------|------|
| `claude` | 启动交互式会话 |
| `claude "描述任务"` | 带初始提示启动 |
| `claude -p "查询"` | 非交互打印模式（SDK），执行完退出 |
| `cat file \| claude -p "分析"` | 管道输入 |
| `claude -c` | 继续当前目录最近一次会话 |
| `claude -c -p "查询"` | 继续会话（打印模式） |
| `claude -r "<会话名>" "查询"` | 按 ID 或名称恢复会话 |
| `claude update` | 更新到最新版本 |

---

## 二、CLI 命令全集

### 会话管理

| 命令 | 说明 |
|------|------|
| `claude` | 启动交互式会话 |
| `claude "query"` | 带初始提示启动 |
| `claude -p "query"` | 打印模式（SDK），执行后退出 |
| `claude -c` | 继续当前目录最近会话 |
| `claude -c -p "query"` | 继续会话（打印模式） |
| `claude -r "<session>" "query"` | 按 ID 或名称恢复会话 |
| `claude --resume` | 交互式选择要恢复的会话 |
| `claude --fork-session` | 恢复时创建新会话 ID（与 `--resume` 或 `--continue` 联用） |
| `claude --session-id <uuid>` | 使用指定 UUID 作为会话 ID |

### 认证

| 命令 | 说明 |
|------|------|
| `claude auth login` | 登录 Anthropic 账户 |
| `claude auth login --email` | 预填邮箱 |
| `claude auth login --sso` | 强制 SSO 认证 |
| `claude auth login --console` | 使用 Anthropic Console API 计费 |
| `claude auth logout` | 退出登录 |
| `claude auth status` | 显示认证状态（`--text` 人类可读） |
| `claude setup-token` | 生成长期 OAuth Token（CI/脚本用） |

### 后台会话（Agent View）

| 命令 | 说明 |
|------|------|
| `claude agents` | 打开 Agent View 监控/调度后台会话 |
| `claude agents --json` | 以 JSON 输出活跃会话列表 |
| `claude agents --cwd <path>` | 只显示指定目录下的会话 |
| `claude --bg "任务"` | 以后台模式启动会话，立即返回 |
| `claude --bg --exec 'pytest -x'` | 后台运行 shell 命令 |
| `claude attach <id>` | 接入后台会话 |
| `claude stop <id>` | 停止后台会话（别名 `claude kill`） |
| `claude respawn <id>` | 重启后台会话 |
| `claude respawn --all` | 重启所有运行中的会话 |
| `claude rm <id>` | 从列表移除会话 |
| `claude logs <id>` | 查看后台会话最新输出 |
| `claude daemon status` | 查看后台守护进程状态 |
| `claude daemon stop --any` | 停止守护进程 |

### 配置与诊断

| 命令 | 说明 |
|------|------|
| `claude update` | 更新到最新版 |
| `claude install [version]` | 安装/重装指定版本（`stable`、`latest` 或 `2.1.118`） |
| `claude mcp` | 配置 MCP 服务器 |
| `claude mcp login <name>` | 运行 MCP 服务器 OAuth 认证 |
| `claude mcp logout <name>` | 清除 MCP OAuth 凭据 |
| `claude plugin` | 管理插件（别名 `claude plugins`） |
| `claude project purge [path]` | 清理项目本地数据（`--dry-run` 预览, `-y` 跳过确认） |
| `claude remote-control` | 启动 Remote Control 服务端 |
| `claude auto-mode defaults` | 打印内置 Auto Mode 分类规则 |
| `claude ultrareview [target]` | 非交互式 UltraReview（`--json` `--timeout`） |

---

## 三、CLI 标志（Flags）

### 模型与推理

| Flag | 说明 |
|------|------|
| `--model <model>` | 设置模型：`sonnet`、`opus`、`haiku`、`fable` 或完整 ID |
| `--fallback-model <models>` | 自动回退模型链（逗号分隔） |
| `--effort <level>` | 推理努力程度：`low`、`medium`、`high`、`xhigh`、`max` |
| `--advisor <model>` | 启用服务端顾问工具：`opus`、`sonnet`、`fable` |
| `--max-turns <N>` | 限制 Agent 轮次（打印模式） |
| `--max-budget-usd <amount>` | API 费用上限（美元，打印模式） |

### 权限与安全

| Flag | 说明 |
|------|------|
| `--permission-mode <mode>` | 权限模式：`default`、`acceptEdits`、`plan`、`auto`、`dontAsk`、`bypassPermissions` |
| `--dangerously-skip-permissions` | 跳过权限提示（等同 `--permission-mode bypassPermissions`） |
| `--allow-dangerously-skip-permissions` | 将 `bypassPermissions` 加入模式循环但不立即启用 |
| `--allowedTools "<tools>"` | 无需提示的工具列表 |
| `--disallowedTools "<tools>"` | 拒绝的工具列表 |
| `--tools "<list>"` | 限制可用内置工具（`"Bash,Edit,Read"` / `""` / `"default"`） |
| `--safe-mode` | 禁用所有自定义项（故障排查） |

### 输入输出

| Flag | 说明 |
|------|------|
| `--print` / `-p` | 非交互打印模式 |
| `--output-format <format>` | 输出格式：`text`、`json`、`stream-json` |
| `--input-format <format>` | 输入格式：`text`、`stream-json` |
| `--json-schema <schema>` | 获取符合 JSON Schema 的验证输出 |
| `--verbose` | 详细日志（完整轮次输出） |
| `--debug [categories]` | 调试模式（可选分类过滤 `"api,hooks"`） |
| `--debug-file <path>` | 调试日志写入指定文件 |
| `--replay-user-messages` | 将用户消息回显到 stdout |

### 系统提示

| Flag | 说明 |
|------|------|
| `--system-prompt <text>` | **替换**整个系统提示 |
| `--system-prompt-file <path>` | 从文件**替换**系统提示 |
| `--append-system-prompt <text>` | **追加**到默认系统提示末尾 |
| `--append-system-prompt-file <path>` | 从文件**追加**到系统提示 |
| `--exclude-dynamic-system-prompt-sections` | 将机器特定信息移到首条用户消息（改善缓存复用） |

### 工作目录与会话

| Flag | 说明 |
|------|------|
| `--add-dir <paths>` | 添加额外工作目录 |
| `--worktree` / `-w` | 在隔离 Git Worktree 中启动 |
| `--tmux` | 为 Worktree 创建 tmux 会话 |
| `--name` / `-n <name>` | 设置会话显示名称 |
| `--continue` / `-c` | 继续最近会话 |
| `--resume` / `-r <id>` | 恢复指定会话 |
| `--no-session-persistence` | 禁用会话持久化 |
| `--bare` | 最小模式：跳过自动发现（更快启动） |

### 代理与团队

| Flag | 说明 |
|------|------|
| `--agent <name>` | 指定子代理 |
| `--agents '<json>'` | 动态定义自定义子代理 |
| `--bg` / `--background` | 后台模式启动 |
| `--exec` | 以 PTY 后台运行 shell 命令（配合 `--bg`） |
| `--teammate-mode <mode>` | 队友显示模式：`in-process`、`auto`、`tmux` |

### 远程与跨设备

| Flag | 说明 |
|------|------|
| `--remote` | 在 claude.ai 创建 Web 会话 |
| `--teleport` | 将 Web 会话传送到本地终端 |
| `--remote-control` / `--rc` | 启用 Remote Control（可从手机/app 控制） |

### 自定义与集成

| Flag | 说明 |
|------|------|
| `--settings <file-or-json>` | 加载设置文件或内联 JSON |
| `--setting-sources <list>` | 设置来源：`user`、`project`、`local` |
| `--mcp-config <files>` | 加载 MCP 服务器配置 |
| `--strict-mcp-config` | 仅使用 `--mcp-config` 的 MCP |
| `--plugin-dir <path>` | 从目录加载插件 |
| `--plugin-url <url>` | 从 URL 加载插件 |
| `--disable-slash-commands` | 禁用所有斜杠命令和 Skills |
| `--ide` | 自动连接 IDE |
| `--chrome` / `--no-chrome` | 启用/禁用 Chrome 集成 |
| `--init` | 运行 Setup Hooks |
| `--init-only` | 只运行 Setup Hooks 然后退出 |
| `--from-pr <PR>` | 恢复链接到特定 PR 的会话 |
| `--prompt-suggestions` | 每轮后输出提示建议 |
| `--betas <headers>` | API Beta 头（API Key 用户） |
| `--version` / `-v` | 输出版本号 |
| `--ax-screen-reader` | 屏幕阅读器友好输出 |

---

## 四、交互模式快捷键

### 通用控制

| 快捷键 | 说明 |
|--------|------|
| `Ctrl+C` | 中断运行中的操作；输入为空时退出 |
| `Ctrl+D` | 退出会话（EOF） |
| `Ctrl+L` | 刷新屏幕 |
| `Ctrl+O` | 切换 Transcript 查看器 |
| `Ctrl+R` | 反向搜索命令历史 |
| `Ctrl+G` 或 `Ctrl+X Ctrl+E` | 在默认编辑器打开输入 |
| `Ctrl+B` | 后台化当前运行的任务 |
| `Ctrl+T` | 切换任务列表显示 |
| `Esc` | 中断当前回复（保留已完成的工作） |
| `Esc Esc` | 清空输入草稿 / 打开回退菜单 |
| `Shift+Tab` 或 `Alt+M` | 循环权限模式 |
| `Alt+P` | 切换模型 |
| `Alt+T` | 切换扩展思考模式 |
| `Alt+O` | 切换快速模式 |
| `↑`/`↓` | 导航命令历史 |
| `←`/`→` | 在对话框标签页间切换 |
| `Space`（按住/点击） | 语音输入（需启用） |

### 文本编辑

| 快捷键 | 说明 |
|--------|------|
| `Ctrl+A` | 光标移到行首 |
| `Ctrl+E` | 光标移到行尾 |
| `Ctrl+K` | 删除到行尾 |
| `Ctrl+U` | 删除到行首 |
| `Ctrl+W` | 删除前一个词 |
| `Ctrl+Y` | 粘贴删除的文本 |
| `Alt+Y`（在 `Ctrl+Y` 后） | 循环粘贴历史 |
| `Alt+B` | 光标后移一词 |
| `Alt+F` | 光标前移一词 |
| `Ctrl+V` / `Cmd+V` | 从剪贴板粘贴图片 |

### 多行输入

| 方法 | 快捷键 |
|------|--------|
| 快速转义 | `\` + `Enter` |
| Option 键 | `Option+Enter`（macOS 需配置） |
| Shift+Enter | `Shift+Enter`（iTerm2/WezTerm/Kitty 等原生支持） |
| 控制序列 | `Ctrl+J` |
| 直接粘贴 | 直接粘贴代码块 |

### 快速命令前缀

| 前缀 | 作用 |
|------|------|
| `/` | 命令或 Skill |
| `!` | Shell 模式（直接运行命令，输出加入上下文） |
| `@` | 文件路径引用（自动补全） |

### Transcript 查看器

| 快捷键 | 说明 |
|--------|------|
| `?` | 切换快捷键帮助面板 |
| `{` / `}` | 跳转到上一个/下一个用户提示 |
| `Ctrl+E` | 切换显示全部内容 |
| `[` | 将完整对话写入终端原生滚动缓冲区 |
| `v` | 写入临时文件并在编辑器中打开 |
| `q` / `Ctrl+C` / `Esc` | 退出 Transcript 视图 |

### Vim 编辑模式

通过 `/config` → Editor mode 启用。

| 模式切换 | 按键 |
|----------|------|
| 进入 NORMAL | `Esc` |
| 插入 | `i` / `I` / `a` / `A` / `o` / `O` |
| 可视模式（字符） | `v` |
| 可视模式（行） | `V` |

| NORMAL 模式操作 | 按键 |
|-----------------|------|
| 删除字符/行 | `x` / `dd` / `D` |
| 删除词 | `dw` / `de` / `db` |
| 修改 | `cc` / `C` / `cw` |
| 复制 | `yy` / `yw` / `ye` / `yb` |
| 粘贴 | `p` / `P` |
| 撤销 | `u` |
| 重复 | `.` |

---

## 五、内置命令与 Skills

在输入中键入 `/` 查看所有可用命令。以下为常用命令：

### 会话管理

| 命令 | 说明 |
|------|------|
| `/clear` | 清空当前会话 |
| `/compact` | 压缩会话（保留关键上下文，释放 Token） |
| `/resume` | 恢复之前的会话 |
| `/cost` | 查看当前会话费用 |
| `/context` | 查看 Context 用量 |
| `/status` | 查看会话配置（模型、目录、Token） |
| `/doctor` | 诊断环境配置问题 |
| `/rename` | 重命名会话 |
| `/recap` | 生成会话摘要 |
| `/btw` | 快速侧边提问（不影响主对话历史） |

### 配置与记忆

| 命令 | 说明 |
|------|------|
| `/init` | 扫描项目生成 CLAUDE.md |
| `/config` | 打开设置界面（`/config key=value` 直接修改单项） |
| `/theme` | 切换终端主题 |
| `/model` | 切换模型 |
| `/permissions` | 管理权限 |
| `/terminal-setup` | 配置终端绑定 |
| `/voice` | 配置语音输入 |

### 项目管理

| 命令 | 说明 |
|------|------|
| `/add-dir` | 添加额外工作目录 |
| `/agents` | 查看/管理后台代理 |
| `/todos` | 查看任务列表 |
| `/schedule` | 创建定时例行任务 |
| `/loop` | 循环执行提示 |
| `/mcp` | 管理 MCP 服务器连接 |
| `/plugin` | 管理插件 |
| `/desktop` | 将会话移交到桌面应用 |

### 开发工作流

| 命令 | 说明 |
|------|------|
| `/code-review` | 代码审查 |
| `/review-pr` | 审查 Pull Request |
| `/debug` | 调试辅助 |
| `/ultrareview` | 深度审查 |
| `/workflows` | 查看/管理工作流 |
| `/output-style` | 切换输出风格 |

---

## 六、CLAUDE.md（项目记忆）

### 四层优先级

| 优先级 | 位置 | 作用范围 |
|--------|------|----------|
| **最高**（就近覆盖） | 内联 `@CLAUDE.md` | 当前对话临时说明 |
| **高** | 子目录 `CLAUDE.md` | 该子目录及下层 |
| **中** | 项目根 `CLAUDE.md` | 整个项目 |
| **低** | `~/.claude/CLAUDE.md` | 所有项目 |

### 推荐模板

```markdown
# 项目意图
[一句话定位]。核心用户：[谁]。当前阶段：[原型/内测/上线]。

# 技术栈
- 语言/框架/数据库/部署

# 禁止改动
- 不要修改 `core/` 下的文件
- 不要引入新的全量依赖

# 验收标准
- 改动前跑测试
- 接口变动需同步文档

# 工作流
- 默认 Plan Mode
- 大改动先开 plan.md
```

---

## 七、Skills（自定义技能）

### 目录结构

```
my-skill/
├── SKILL.md       # 触发条件 + 执行说明
├── scripts/       # 可调用脚本
└── references/    # 参考资料、模板
```

### 安装位置

| 级别 | 路径 |
|------|------|
| 用户级 | `~/.claude/skills/` |
| 项目级 | `<project>/.claude/skills/` |

### SKILL.md 模板

```markdown
---
name: my-skill
description: 触发条件描述。关键词：[列表]
---

# 执行步骤
1. 读取 references/template.md
2. 调用 scripts/do-something.py
3. 输出到指定位置
```

---

## 八、MCP（Model Context Protocol）

| 命令 | 说明 |
|------|------|
| `claude mcp` | 打开 MCP 管理面板 |
| `claude mcp login <name>` | OAuth 认证 MCP 服务器 |
| `claude mcp logout <name>` | 清除 OAuth 凭据 |
| `--mcp-config <files>` | 启动时加载 MCP 配置 |
| `--strict-mcp-config` | 仅使用指定的 MCP 配置 |

> **Skills 管流程，MCP 管连接，子代理管分工。**

---

## 九、配置作用域

| 作用域 | 位置 | 影响范围 | 团队共享 |
|--------|------|----------|----------|
| **Managed** | 服务端管理 / plist / 注册表 | 组织全员 | ✓ |
| **User** | `~/.claude/` | 个人，跨所有项目 | ✗ |
| **Project** | `.claude/`（仓库中） | 所有协作者 | ✓（Git 提交） |
| **Local** | `.claude/settings.local.json` | 个人，仅当前项目 | ✗（自动 GitIgnore） |

---

## 十、常用工作模式

| 模式 | 快捷键 | 适用场景 |
|------|--------|----------|
| **Normal** | `Shift+Tab` | 边问边做，标准对话 |
| **Plan** | `Shift+Tab` | 先规划再执行，复杂任务推荐 |
| **Auto** | `Shift+Tab` | 全自动模式，Claude 自主决策 |
| **Accept Edits** | `Shift+Tab` | 自动接受编辑，跳过一次确认 |
| **Bypass Permissions** | 需手动启用 | 跳过所有权限提示（CI/脚本） |

> **建议**：80% 的任务在 Plan Mode 跑。Auto Mode 适合简单明确的任务。

---

## 十一、Shell 模式

以 `!` 开头的输入直接执行 shell 命令，输出加入会话上下文：

```bash
! npm test
! git status
! ls -la
```

- 显示实时进度和输出
- 支持 `Ctrl+B` 后台化长时间命令
- 支持 `Tab` 历史自动补全
- 退出：空提示下按 `Esc`、`Backspace` 或 `Ctrl+U`

---

## 十二、配置环境变量（常用）

| 变量 | 说明 |
|------|------|
| `ANTHROPIC_MODEL` | 设置默认模型 |
| `ANTHROPIC_API_KEY` | API Key（使用 API 计费时） |
| `CLAUDE_CODE_SIMPLE` | 简化模式（等同 `--bare`） |
| `CLAUDE_CODE_SAFE_MODE` | 安全模式 |
| `CLAUDE_CODE_SKIP_PROMPT_HISTORY` | 禁用会话持久化 |
| `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` | 控制提示建议（`true`/`false`） |
| `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` | 禁用后台任务 |
| `CLAUDE_CODE_DEBUG_LOGS_DIR` | 调试日志目录 |
| `CLAUDE_CODE_TASK_LIST_ID` | 命名任务列表路径 |
| `CLAUDE_AX_SCREEN_READER` | 屏幕阅读器模式 |

---

## 十三、急救三步（卡死时用）

| 步骤 | 操作 | 说明 |
|------|------|------|
| **1. 中断** | `Ctrl+C` | 掐掉正在跑的循环 |
| **2. 清空** | `/clear` | 清掉全部历史包袱 |
| **3. 重述** | 重新描述任务 | 基于学到的"它会卡在哪"，Prompt 写得更具体 |

### 五大常见错误

| # | 错误 | 解决 |
|----|------|------|
| 1 | Token 烧爆 | `/compact` 或 `/clear` |
| 2 | 没 Plan 直接 Auto | 80% 任务在 Plan Mode 跑 |
| 3 | 没写 CLAUDE.md | 进项目先 `/init` |
| 4 | `@` 错大文件 | `@` 之前确认是否真的需要 |
| 5 | 一个对话塞五件事 | 一个 Prompt 一件事 |

---

> 📚 **官方文档**：[code.claude.com/docs](https://code.claude.com/docs)
> 📖 **橙皮书**：花叔《Claude Code 完全指南》[GitHub](https://github.com/alchaincyf/claude-code-orange-book)
