```mermaid
flowchart TB
    A["📎 B站视频链接<br/>BV1xxxxxx"]
    B["🔧 yt-dlp<br/>下载视频信息"]
    C{"🔀 是否有<br/>B站字幕?"}
    D["📥 biliSub<br/>提取字幕"]
    E["🎵 yt-dlp<br/>下载音频"]
    F["🔄 格式转换<br/>json → srt → txt"]
    G["🧠 Faster Whisper<br/>large-v3 + CUDA"]
    H["✅ 字幕文本<br/>(官方字幕)"]
    I["✅ .srt 字幕文本<br/>(Whisper生成)"]
    J["📄 字幕全文 txt<br/>两条路径汇合"]
    K["📄 字幕全文 txt → 输入"]
    L["🤖 Claude / Claudian<br/>智能总结"]
    M["📋 Prompt 模板<br/>Houdini/UE5 技术专家"]
    N["🏷️ AI 自动分类<br/>JSON: type, category, folder"]
    O["📝 Markdown 笔记<br/>YAML + tags + wikilinks"]
    P["📂 Obsidian Vault<br/>自动保存"]
    Q["🔗 双链笔记<br/>[[Attribute]] [[HDA]]"]
    R["📁 按主题归档<br/>Houdini/PCG/城市生成.md"]
    S["📸 自动截图<br/>关键帧 → Assets/"]
    T["🔬 实体抽取<br/>节点/算法/软件 → 知识图谱"]
    A --> B
    B --> C
    C -->|"✅ 有字幕"| D
    C -->|"❌ 无字幕"| E
    D --> F
    E --> G
    F --> H
    G --> I
    H --> J
    I --> J
    J --> K
    K --> L
    L --> M
    L --> N
    M --> O
    N --> O
    O --> P
    P --> Q
    Q --> R
    O --> S
    O --> T
    %% ── 输入层 ──
    %% ── 字幕获取层 ──
    %% ── AI 处理层 ──
    %% ── 输出层 ──
    %% ── 增强模块 ──
    你想搭建的实际上是一个**AI 视频知识库自动化流水线**：
    > B站视频链接 → 自动下载/获取字幕 → 无字幕自动 Whisper 转录 → Claude/Claudian 总结 → 自动生成 Obsidian Markdown → 按主题归档
    这个流程非常适合你现在整理：
    - Houdini 教程
    - UE5 PCG
    - Matrix Awakens 分析
    - GDC 演讲
    - 游戏开发课程
    下面给你一个**Windows 本地可落地方案**。
    ---
    # 一、整体架构
    最终效果：
    输入：
    %% mermaid-flow:pos A=134,200 B=322,200 C=504,200 D=675,255 E=675,145 F=861,255 G=861,145 H=1071,255 I=1071,145 J=1272,200 K=1499,200 L=1746,200 M=2008,255 N=2008,145 O=2274,200 P=2540,310 Q=2797,310 R=3050,310 S=2540,200 T=2540,85
```
https://www.bilibili.com/video/BVxxxx
```

↓

自动执行：

```
B站视频
   |
   |
   +----------------+
   |                |
有字幕             无字幕
   |                |
biliSub/API        Whisper
   |                |
   +-------+--------+
           |
           ↓
       字幕文本
           |
           ↓
     Claude / Claudian
           |
           ↓
    Markdown笔记
           |
           ↓
      Obsidian Vault
           |
           ↓
自动分类保存
```

---

# 二、软件组成

|功能|工具|
|---|---|
|下载B站视频|yt-dlp|
|提取已有字幕|biliSub / bilibili API|
|无字幕识别|Faster Whisper|
|AI总结|Claudian + Claude API|
|知识库|Obsidian|
|自动分类|Python脚本|

---

# 三、目录设计（推荐）

建立你的知识库：

```
Houdini_UE5_Knowledge/

│
├── 00_Inbox
│
├── Houdini
│   ├── SOP
│   ├── VEX
│   ├── HDA
│   ├── PCG
│   └── Terrain
│
├── Unreal
│   ├── PCG
│   ├── Blueprint
│   ├── MassAI
│   └── WorldPartition
│
├── GameDesign
│
├── AI_Tools
│
└── VideoNotes
    ├── Bilibili
    └── Youtube
```

---

# 四、安装环境

## 1. Python

安装：

Python 3.11

检查：

```bash
python --version
```

---

## 2. 安装 yt-dlp

作用：

下载B站视频信息。

```bash
pip install yt-dlp
```

测试：

```bash
yt-dlp --version
```

---

## 3. 安装 Faster Whisper

```bash
pip install faster-whisper
```

如果有 NVIDIA 显卡：

推荐：

```
CUDA
+
large-v3
```

---

# 五、字幕获取逻辑

核心：

先判断：

```
有没有B站字幕？
```

---

## 情况1：有字幕

使用：

biliSub / B站字幕接口

得到：

```
subtitle.json

↓

subtitle.srt

↓

txt
```

---

## 情况2：没有字幕

自动：

```
下载音频

↓

Whisper

↓

srt
```

---

# 六、自动流程脚本结构

创建：

```
BiliNoteAI/

│
├── main.py
│
├── downloader.py
│
├── subtitle.py
│
├── whisper.py
│
├── claude.py
│
└── organizer.py

```

---

# 七、核心流程代码逻辑

## main.py

```python
url=input("请输入B站链接:")


# 1 获取字幕

subtitle=get_subtitle(url)


# 2 如果没有字幕

if subtitle is None:

    audio=download_audio(url)

    subtitle=whisper(audio)


# 3 AI总结

note=claude_summary(subtitle)


# 4 保存Obsidian

save_note(note)

```

---

# 八、Whisper部分

例如：

whisper.py

```python
from faster_whisper import WhisperModel


model=WhisperModel(
    "large-v3",
    device="cuda",
    compute_type="float16"
)


def transcribe(file):

    segments,info=model.transcribe(
        file
    )


    text=""

    for s in segments:

        text+=s.text+"\n"


    return text

```

---

# 九、Claude / Claudian 自动总结

这里分两种。

---

## 方案A（推荐）：Obsidian Claudian插件

流程：

```
字幕txt

↓

放入Inbox

↓

Claudian读取

↓

生成笔记
```

Prompt：

保存为模板：

```
你是一名Houdini和UE5技术专家。

请整理这个视频字幕：

输出：

# 视频标题

## 核心目标

## 技术架构

## 节点流程

## Houdini节点

## UE5模块

## 参数说明

## 可复现项目

## 官方文档

## 我的学习笔记

添加：

#Houdini
#UE5
#PCG

输出Markdown。
```

---

## 方案B：Claude API自动化

Python：

```python
import anthropic


client=anthropic.Anthropic(
api_key="你的key"
)


message=client.messages.create(
model="claude-sonnet",
messages=[
{
"role":"user",
"text":subtitle
}
]
)

```

---

# 十、自动保存到Obsidian

例如：

视频：

```
Houdini程序化城市道路生成
```

自动生成：

```
Houdini/
 └── PCG/
     |
     └── Houdini程序化城市道路生成.md
```

Markdown：

```markdown
---
title:Houdini程序化城市道路生成
tags:
 - Houdini
 - PCG
 - Road
source:
 - Bilibili
---

# 核心内容

...

# 节点流程

Curve

↓

Resample

↓

Sweep

↓

Output


# 相关知识

[[Attribute]]
[[Copy To Points]]
[[HDA]]

```

---

# 十一、自动分类（AI判断）

让 Claude 返回：

```json
{
"type":"Houdini",
"category":"PCG",
"folder":"Houdini/PCG"
}
```

Python：

自动移动：

```
Houdini/PCG
```

---

# 十二、最终使用体验

以后你只需要：

运行：

```
BiliNoteAI.exe
```

输入：

```
BV1xxxxxx
```

10分钟后：

你的 Obsidian：

```
Houdini
 ├── PCG
 │    ├── 城市生成.md
 │    ├── 道路算法.md
 │
Unreal
 ├── MassAI
 │    └── NPC系统.md

```

---

# 十三、针对你的方向，我建议增加两个模块

因为你研究的是 **Matrix Awakens 类 PCG**，建议增加：

## 1. 自动截图模块

视频关键帧：

```
00:10 Houdini节点

00:30 UE PCG Graph

01:20 City Generator
```

自动截图：

保存：

```
Assets/
 ├── screenshot01.png
 ├── screenshot02.png
```

Markdown引用：

```markdown
![[screenshot01.png]]
```

---

## 2. 技术实体抽取

AI自动生成：

```
节点：

- Attribute Wrangle
- Copy To Points
- RBD Material Fracture


算法：

- WFC
- L-System
- Shape Grammar


软件：

- Houdini
- Unreal Engine
```

形成知识图谱。

---

## 最终推荐技术栈

如果按你的学习方向：

```
Bilibili
    |
yt-dlp
    |
biliSub
    |
Faster Whisper
    |
Claude / Claudian
    |
Obsidian
    |
Git版本管理

```

这是目前非常接近 **个人 AI 游戏开发研究数据库** 的搭建方式。

下一步可以进一步做成：  
**“输入一个 B 站 / YouTube 链接，自动生成带截图、节点图、Mermaid流程图、Obsidian双链的 Houdini/UE5 学习笔记机器人”。**




