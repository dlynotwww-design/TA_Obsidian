---
title: 影视项目UE流程化 - 流程图
date: 2026-07-12
tags:
  - 影视流程
  - UE
  - 流程图
  - TA
aliases:
  - UE影视流程化流程图
---

# 影视项目 UE 流程化 — 流程图

> TA · 制作 · TD 协作全景图 | 基于 [[影视项目UE流程化.canvas]]

---

## 一、总览：全流程管线

```mermaid
graph TB
    A["<b>Phase A</b><br/>UE文件大纲 & 项目结构规划<br/>━━━━━━━━━━━━━━<br/>命名规范 · 目录标准<br/>自动化目录生成"]

    B["<b>Phase B</b><br/>自动化插件 & 工具链<br/>━━━━━━━━━━━━━━<br/>批量导入插件 · 工具开发<br/>底层 API 支持"]

    C["<b>Phase C</b><br/>道具制作管线<br/>━━━━━━━━━━━━━━<br/>贴图/材质/模型规范<br/>自动导入 · 质量检查"]

    D["<b>Phase D</b><br/>角色制作管线 ⭐ TA核心战场<br/>━━━━━━━━━━━━━━<br/>骨骼 · 蒙皮 · 毛发 Groom<br/>解算 CFX · 动画管线"]

    E["<b>Phase E</b><br/>场景制作管线<br/>━━━━━━━━━━━━━━<br/>PCG · 资产库 · 灯光<br/>效果标准 · 后处理"]

    F["<b>Phase F</b><br/>镜头管理 & 资产管线<br/>━━━━━━━━━━━━━━<br/>Shot 组织 · ShotAssets<br/>批量化 · 渲染农场"]

    G["<b>Phase G</b><br/>AI 技术融合<br/>━━━━━━━━━━━━━━<br/>AI生成三视图 · 图生3D<br/>智能场景摆放"]

    H["<b>影视UE管线协作闭环</b><br/>━━━━━━━━━━━━━━<br/>制作 ← TA → TD<br/>持续改进管线"]

    I["<b>VFXAssets & 特效管线</b><br/>━━━━━━━━━━━━━━<br/>Niagara · 特效材质<br/>Shot 关联 · 版本快照"]

    A -->|"大纲结构确立 → 插件开发"| B
    B -->|"工具链就绪 → 道具管线"| C
    C -->|"道具管线 → 角色管线"| D
    D -->|"角色管线 → 场景管线"| E
    E -->|"场景管线 → 镜头管理"| F
    F -->|"传统管线成熟 → AI技术融合"| G
    F -->|"镜头管理 → 协作总结"| H
    G -->|"AI探索 → 协作闭环"| H
    H -->|"VFX管线补充说明"| I

    style A fill:#4a9eff,color:#fff
    style B fill:#a855f7,color:#fff
    style C fill:#f59e0b,color:#fff
    style D fill:#10b981,color:#fff
    style E fill:#06b6d4,color:#fff
    style F fill:#ef4444,color:#fff
    style G fill:#4a9eff,color:#fff
    style H fill:#ef4444,color:#fff
    style I fill:#f59e0b,color:#fff
```

---

---

## 三、Phase B：自动化插件 & 工具链

```mermaid
graph LR
    subgraph B1["🎨 制作 / 美术"]
        direction TB
        B1a["使用批量导入插件<br/>一键导入模型 (.fbx/.abc)<br/>自动导入贴图"]
        B1b["使用效率插件<br/>快速查找/替换资产<br/>批量操作工具"]
        B1c["按规范提交资产<br/>→ 自动归位到正确目录"]
    end

    subgraph B2["⚙️ TA / 流程"]
        direction TB
        B2a["文件批量处理插件<br/>解析命名→匹配目录→导入"]
        B2b["自动赋予材质球信息<br/>贴图名→材质属性映射<br/>批量创建 Material Instance"]
        B2c["自动整理优化文件夹<br/>清理空目录/冗余资产<br/>贴图压缩格式配置"]
    end

    subgraph B3["🔧 TD / 程序"]
        direction TB
        B3a["Console Command 调用<br/>py 命令执行 Python 脚本"]
        B3b["Editor Utility Widget<br/>可视化工具面板"]
        B3c["Python API 集成<br/>unreal.EditorAssetLibrary<br/>命令行批处理/CI-CD"]
    end

    B1 --> B2 --> B3
```

---

## 四、Phase C：道具制作管线

```mermaid
graph LR
    subgraph C1["🎨 制作 / 美术"]
        direction TB
        C1a["<b>贴图</b><br/>命名规范 · 位数规定<br/>尺寸合理控制"]
        C1b["<b>材质</b><br/>Opaque / Masked<br/>/ Translucent<br/>使用母材质创建实例"]
        C1c["<b>模型</b><br/>Maya 制作规范<br/>面数控制 · 布线优化<br/>UV 展开"]
    end

    subgraph C2["⚙️ TA / 流程"]
        direction TB
        C2a["<b>贴图处理</b><br/>规则化自动导入<br/>命名→自动匹配材质槽位<br/>自动设置压缩 & sRGB"]
        C2b["<b>材质自动生成</b><br/>_BC→BaseColor<br/>_N→Normal<br/>_RMA→Roughness/Metallic/AO"]
        C2c["<b>模型管线</b><br/>Maya自动导出脚本<br/>UE自动导入+目录归位<br/>→ 一键式道具导入管线"]
    end

    subgraph C3["🔧 TD / 程序"]
        direction TB
        C3a["<b>优化 & 质量</b><br/>面数合理性布局<br/>LOD链自动生成<br/>碰撞体自动生成"]
        C3b["UE精度问题处理<br/>浮点精度(大世界)<br/>法线/切线导入问题"]
        C3c["资产合规自动检查<br/>命名校验 · 贴图尺寸告警<br/>面数超标告警"]
    end

    C1 --> C2 --> C3
```

---

## 五、Phase D：角色制作管线 ⭐ TA 核心战场

```mermaid
graph LR
    subgraph D1["🎨 制作 / 美术"]
        direction TB
        D1a["<b>贴图 & 材质</b><br/>UDIM多象限贴图<br/>Skin/Eye/Hair/Cloth<br/>角色母材质模板"]
        D1b["<b>模型 & 骨骼</b><br/>Maya制作→自动导出<br/>骨骼信息正确对应<br/>蒙皮修型信息带入"]
        D1c["<b>毛发 Groom</b><br/>Groom制作<br/>材质球效果测试<br/>毛发动态测试"]
    end

    subgraph D2["⚙️ TA / 流程"]
        direction TB
        D2a["<b>材质方案</b><br/>毛发材质球测试<br/>规则化自动生成材质<br/>皮肤SSS配置"]
        D2b["<b>骨骼 & 动画</b><br/>骨骼验证工具<br/>插件导入骨骼+蒙皮<br/>镜头动画自动化处理"]
        D2c["<b>解算 CFX & 毛发</b><br/>解算导入方案设计<br/>合并骨骼模型<br/>Groom缓存导入"]
    end

    subgraph D3["🔧 TD / 程序"]
        direction TB
        D3a["骨骼映射验证<br/>Maya→UE 自动检测<br/>DeltaMorph/BlendShape"]
        D3b["动画自动化<br/>Sequencer批量导入<br/>IK Rig 重定向<br/>Modular Character"]
        D3c["物理 & 渲染优化<br/>Physics Asset自动生成<br/>Chaos Cloth布料<br/>Groom LOD/剔除"]
    end

    D1 --> D2 --> D3
```

---

## 六、Phase E：场景制作管线

```mermaid
graph LR
    subgraph E1["🎨 制作 / 美术"]
        direction TB
        E1a["<b>快速搭建</b><br/>PCG技术运用<br/>植被自动散布<br/>场景制作插件"]
        E1b["<b>灯光</b><br/>基础标准灯光布置<br/>Directional/Sky/点光源<br/>Lumen动态GI"]
        E1c["<b>效果</b><br/>场景效果打磨<br/>后处理调色<br/>雾效/天气"]
    end

    subgraph E2["⚙️ TA / 流程"]
        direction TB
        E2a["<b>资产库</b><br/>搭建与管理<br/>标签与分类体系<br/>Perforce/内部工具"]
        E2b["<b>插件体系</b><br/>PCG插件配置<br/>地形工具集成<br/>批量替换工具"]
        E2c["<b>效果标准</b><br/>审核标准确立<br/>灯光预设<br/>后处理LUT方案"]
    end

    subgraph E3["🔧 TD / 程序"]
        direction TB
        E3a["PCG Framework 配置<br/>Custom PCG Node 开发"]
        E3b["基础灯光系统<br/>灯光预设脚本<br/>TOD系统"]
        E3c["资产库软件架构<br/>数据库+标签检索<br/>缩略图+版本管理<br/>入库→检索→使用→反馈"]
    end

    E1 --> E2 --> E3
```

---

## 七、Phase F：镜头管理 & 资产管线

```mermaid
graph LR
    subgraph F1["🎨 制作 / 美术"]
        direction TB
        F1a["<b>镜头结构</b><br/>EP→SC→镜头号<br/>每镜头含:<br/>Ani / VFX / CFX"]
        F1b["<b>组织方式</b><br/>ep01_sc01_c001<br/>总序列+子轨道<br/>层级化管理"]
    end

    subgraph F2["⚙️ TA / 流程"]
        direction TB
        F2a["<b>ShotAssets管理</b><br/>Ani/Cfx/Vfx<br/>按镜头独立存放"]
        F2b["命名与镜头号一致<br/>版本管理 v001/v002<br/>跨镜头资产引用规则"]
        F2c["发布/审核状态标记<br/>→ 镜头管理工具+规范"]
    end

    subgraph F3["🔧 TD / 程序"]
        direction TB
        F3a["<b>批量化 & 自动化</b><br/>批量创建Sequence<br/>批量导入Ani/Cfx/Vfx<br/>批量渲染设置"]
        F3b["Shot与ShotAssets同步<br/>版本对比&回滚<br/>EP/SC批量操作"]
        F3c["渲染农场集成<br/>Movie Render Queue<br/>批量提交"]
    end

    F1 --> F2 --> F3
```

---

## 八、Phase G：AI 技术融合

```mermaid
graph LR
    subgraph G1["🤖 AI应用 #1"]
        direction TB
        G1a["<b>生成三视图</b><br/>概念图/文字描述<br/>→ 自动生成<br/>正/侧/后视图"]
        G1b["辅助建模师<br/>快速理解设计意图<br/>减少前期沟通成本"]
    end

    subgraph G2["🤖 AI应用 #2"]
        direction TB
        G2a["<b>图片生成模型资产</b><br/>参考图片→3D模型<br/>适用于:<br/>道具/建筑/植被"]
        G2b["输出初步模型<br/>→美术精修调整<br/>Image-to-3D<br/>Text-to-3D"]
    end

    subgraph G3["🤖 AI应用 #3"]
        direction TB
        G3a["<b>智能场景摆放</b><br/>场景语义自动排布<br/>植被群落生态关联<br/>建筑/道路合理性"]
        G3b["PCG+AI混合方案<br/>强化学习场景布局<br/>LLM理解场景描述<br/>→自动生成"]
    end

    G1 --> G2 --> G3
```

---

## 九、影视UE管线协作闭环

```mermaid
graph TB
    subgraph CL["🔄 核心协作循环"]
        direction LR
        M["🎨 <b>制作 / 美术</b><br/>━━━━━━━━━━<br/>按规范制作资产<br/>使用TA工具导入<br/>场景搭建&灯光<br/>镜头组织&提交<br/><br/>📦 产出: 影视资产 & 镜头"]

        T["⚙️ <b>TA / 流程</b><br/>━━━━━━━━━━<br/>制定命名规范&标准<br/>开发自动导入/材质插件<br/>搭建资产库&分类<br/>设计镜头管理流程<br/>效果标准&灯光预设<br/>AI技术方案验证<br/><br/>📦 产出: 工具+规范+标准"]

        D["🔧 <b>TD / 程序</b><br/>━━━━━━━━━━<br/>底层API&脚本开发<br/>批量化处理工具<br/>性能优化&质量检查<br/>资产合规自动校验<br/>CI/CD管线集成<br/>骨骼/蒙皮数据验证<br/>渲染农场对接<br/><br/>📦 产出: 稳定运行的管线系统"]
    end

    CORE["<b>核心循环</b><br/>TA提供规范工具 → 制作按规范执行 → TD底层保障 → TA迭代优化 → 持续改进"]

    M --> CORE
    T --> CORE
    D --> CORE
    CORE --> M
    CORE --> T
    CORE --> D

    style M fill:#4a9eff,color:#fff
    style T fill:#10b981,color:#fff
    style D fill:#a855f7,color:#fff
    style CORE fill:#ef4444,color:#fff
```

---

## 十、VFXAssets & 特效管线

```mermaid
graph TB
    subgraph VFX["✨ VFX 管线"]
        direction TB
        V1["<b>VFXAssets 目录</b><br/>独立的VFX资产目录<br/>Niagara粒子系统<br/>贴图/材质/网格体"]
        V2["<b>特效管线接入</b><br/>项目→类型→名称 三级目录<br/>Niagara命名规范<br/>VFX贴图自动压缩<br/>专用母材质模板<br/>(Additive/Translucent/Modulate)"]
        V3["<b>与 Shot 关联</b><br/>Shot→VFX轨道引用VFXAssets<br/>同一特效多镜头复用<br/>资产版本快照<br/>已锁定镜头不受迭代影响"]
    end

    V1 --> V2 --> V3

    style V1 fill:#f59e0b,color:#fff
    style V2 fill:#f59e0b,color:#fff
    style V3 fill:#f59e0b,color:#fff
```

---

## 十一、完整协作关系图

```mermaid
graph TB
    subgraph ROLES["👥 三角色协作模式"]
        direction LR
        ARTIST["🎨 <b>制作/美术</b><br/><i>使用者</i><br/>我来做资产"]
        TA["⚙️ <b>TA/流程</b><br/><i>工具提供者</i><br/>我来建管线"]
        TD["🔧 <b>TD/程序</b><br/><i>保障者</i><br/>我来保证管线稳定"]
    end

    subgraph FLOW["📋 管线阶段"]
        direction TB
        PA["Phase A: 大纲 & 结构"]
        PB["Phase B: 插件 & 工具"]
        PC["Phase C: 道具管线"]
        PD["Phase D: 角色管线 ⭐"]
        PE["Phase E: 场景管线"]
        PF["Phase F: 镜头管理"]
        PG["Phase G: AI融合"]
    end

    CLOSURE["🔄 协作闭环 → 持续改进"]

    ARTIST --> FLOW
    TA --> FLOW
    TD --> FLOW
    FLOW --> CLOSURE
    CLOSURE -.->|"迭代反馈"| ARTIST
    CLOSURE -.->|"迭代反馈"| TA
    CLOSURE -.->|"迭代反馈"| TD

    style ARTIST fill:#4a9eff,color:#fff
    style TA fill:#10b981,color:#fff
    style TD fill:#a855f7,color:#fff
    style CLOSURE fill:#ef4444,color:#fff
```

---

> [!note] 与 Canvas 的关系
> 本笔记是基于 [[影视项目UE流程化.canvas]] 的 Mermaid 流程图版本。
> Canvas 中的分组结构、文本内容和连线关系均已转换为流程图形式。
>
> - **总览图**：展示 Phase A→G + 协作闭环 + VFX 的完整链路
> - **各 Phase 详图**：展示每个阶段三角色的具体分工
> - **协作闭环**：展示 TA↔制作↔TD 的持续改进循环
