# Houdini 散布系统 — 流程图

> **项目文件**: `D:/TA/Houdini/mcp/MCP.hip`
> **网络路径**: `/obj/scatter_system`

---

## 1. 完整节点管线

```mermaid
flowchart TB
    subgraph Terrain["🏔️ 地形生成"]
        A["<b>ground</b><br/>Grid<br/><i>10×10 · 80×80 res</i>"]
        B["<b>terrain</b><br/>Mountain<br/><i>Simplex noise · H=0.98</i>"]
    end

    subgraph Normal["🧭 法线准备"]
        C["<b>pt_normals</b><br/>Normal SOP<br/><i>Vertex N → Point N</i>"]
    end

    subgraph Scatter["🎲 散布生成"]
        D["<b>scatter_pts</b><br/>Scatter<br/><i>500 pts · seed=42</i>"]
        E["<b>rand_pscale</b><br/>Attr Randomize<br/><i>pscale [0.15, 0.8]</i>"]
        F["<b>rand_color</b><br/>Attr Randomize<br/><i>Cd · blue spectrum</i>"]
    end

    subgraph Source["🔷 源几何体"]
        G["<b>source_torus</b><br/>Torus<br/><i>R=(0.3, 0.1) · 24×16</i>"]
        H["<b>rotate_torus</b><br/>Transform<br/><i>Rotate X = -90°</i>"]
    end

    subgraph Output["📦 复制输出"]
        I["<b>copy_tori</b><br/>Copy to Points<br/><i>Pack & Instance<br/>transform: true</i>"]
    end

    A -->|"网格"| B
    B -->|"置换地形"| C
    C -->|"点法线"| D
    D -->|"散点"| E
    E -->|"随机大小"| F
    F -->|"点属性"| I
    G -->|"Torus"| H
    H -->|"旋转后 Torus"| I

    I --> J["<b>✅ 最终输出</b><br/>500 个 Torus 散布<br/>Y轴对齐法线"]

    style A fill:#4a90d9,color:#fff
    style B fill:#4a90d9,color:#fff
    style C fill:#7b68ee,color:#fff
    style D fill:#e67e22,color:#fff
    style E fill:#e67e22,color:#fff
    style F fill:#e67e22,color:#fff
    style G fill:#27ae60,color:#fff
    style H fill:#27ae60,color:#fff
    style I fill:#e74c3c,color:#fff
    style J fill:#2ecc71,color:#000
```

---

## 2. 属性数据流

散点属性如何被 Copy to Points 消费：

```mermaid
flowchart LR
    subgraph PointAttrs["散点属性（第二输入 → copy_tori）"]
        direction TB
        P["<b>P</b><br/>位置"]
        N["<b>N</b><br/>法线"]
        pscale["<b>pscale</b><br/>统一缩放"]
        id["<b>id</b><br/>唯一标识"]
        Cd["<b>Cd</b><br/>颜色"]
    end

    subgraph CopyConsume["copy_tori 消费方式"]
        direction TB
        P1["📍 确定副本位置"]
        N1["🔄 Z轴对齐 N<br/>旋转匹配"]
        S1["📏 逐副本缩放"]
        I1["🏷️ 实例 ID"]
        C1["🎨 逐实例着色"]
    end

    P --> P1
    N --> N1
    pscale --> S1
    id --> I1
    Cd --> C1
```

---

## 3. Y 轴对齐法线原理

Copy to Points 默认将源几何体 **Z 轴** 对齐法线。Torus 的孔洞沿 Z 轴，需旋转 -90°（X 轴），使 Y 轴换到 Z 方向。

```mermaid
flowchart LR
    subgraph s1["① 原始状态"]
        T1["Torus<br/>平铺 XY 平面<br/>孔洞沿 Z"]
    end

    subgraph s2["② Transform SOP"]
        X["Rotate X = -90°"]
    end

    subgraph s3["③ 旋转后"]
        T2["Torus<br/>Y 轴 → Z 方向<br/>孔洞 → -Y 方向"]
    end

    subgraph s4["④ Copy to Points"]
        C["transform: true<br/>Z 轴对齐 法线 N"]
    end

    subgraph s5["⑤ 最终效果"]
        R["✅ Y 轴 对齐法线<br/>孔洞平行地表"]
    end

    s1 --> s2 --> s3 --> s4 --> s5
```

| 源 Torus 轴 | 旋转后方向 | Copy to Points 映射 |
|:-----------:|:---------:|:------------------:|
| Y 轴 | → Z | → 法线 N ✓ |
| Z 轴（孔洞） | → -Y | → 垂直于法线 |

---

## 4. 管线小结

| # | 节点 | 类型 | 一句话 |
|---|------|------|--------|
| 1 | ground | Grid | 10×10 地面网格 |
| 2 | terrain | Mountain | Simplex 噪声置换 |
| 3 | pt_normals | Normal | 顶点法线 → 点法线 |
| 4 | scatter_pts | Scatter | 500 散点 + pscale/id |
| 5 | rand_pscale | Attr Randomize | pscale 随机 [0.15, 0.8] |
| 6 | rand_color | Attr Randomize | Cd 随机蓝色系 |
| 7 | source_torus | Torus | 源圆环 R=(0.3, 0.1) |
| 8 | rotate_torus | Transform | 旋转 -90° X |
| 9 | copy_tori | Copy to Points | Pack&Instance 输出 |
