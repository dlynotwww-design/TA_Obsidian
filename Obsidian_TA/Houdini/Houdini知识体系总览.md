# Houdini 知识体系总览

> 本文档整合了 Houdini 文件夹下 11 篇笔记的核心内容，按主题归类梳理，形成完整的知识地图。

---

## 一、Houdini 核心概念与操作

### 1.1 主要模块（网络类型）

| 模块 | 英文名 | 缩写 | 用途 |
|------|--------|------|------|
| 场景 | Scene | OBJ | 对象层级管理 |
| 几何 | Geometry | SOP | 曲面运算操作，几何体编辑（**最核心**） |
| Solaris | Solaris | LOP | 照明/布局操作 |
| 材料 | Materials | MAT | VEX Builder / 材质 |
| Motion FX | Motion FX | CHOP | 通道操作 |
| VEX | VEX Builder | VOP | 可视编程 |
| 输出 | Outputs | ROP | 渲染操作 |
| 任务 | Tasks | TOP | PDG 任务操作 |
| 动力学 | Dynamics | DOP | 动态算子 / 解算 |
| 合成 | Compositing | COP/IMG | 合成操作 |

### 1.2 常用操作

- **移动** `T` / **旋转** `R` / **缩放** `E` / **姿势** `Ctrl+R` / **操纵杆** `Enter`
- **连接节点**：左键从输出拖到输入
- **串联多个节点**：按住 `J`，左键穿过节点
- **插入新节点**：在输出上右键创建
- **插入节点**：左键拖拽连接线
- **断开连接线**：左键选择后摇动节点
- **剪断连接线**：按住 `Y`，鼠标左键穿过
- **复制节点**：`Alt+左键拖拽`
- **引用副本**：`Alt+Shift+Ctrl+左键`
- **添加点节点**：选中连接线后 `Alt+左键`
- **连线圆角优化**：`Shift+S`
- **显示细节面板**：`P`

### 1.3 单位

- **Houdini** 默认单位为**米**
- **UE** 默认单位为**厘米**（需注意转换）

### 1.4 关键名词

- **Voxel**：体素
- **VDB**：稀疏体积数据格式，常用于体积操作
- **HDA (Houdini Digital Asset)**：将节点网络打包成可复用工具，可在任何支持 Houdini Engine 的软件中使用（Maya、3DS Max、UE4/5 等）
- **PDG (Procedural Dependency Graph)**：批量处理与流程优化系统，用于加速输出、占满电脑资源

---

## 二、VEX 语言

VEX（Vector Expressions）是 Houdini 专用的高性能编程语言：

- **语法类似 C 语言**，高性能，直接与 Houdini 内部数据结构交互
- **应用领域**：建模、动画、粒子、物理模拟、着色器编写
- **载体节点**：Wrangle 节点、VOP 节点
- **典型用途**：几何处理（点/线/多边形操作）、自定义着色器、程序化生成

### VEX 学习路径
1. **入门**：B站捷佳系列、Entagma VEX101
2. **中级**：VEX 制作树木 HDA 资产、捷佳 Python 城市
3. **高级**：湖边小屋教程（Houdini 中最复杂的 VEX 教程）

> 💡 可使用 GPT 辅助节点设计及 VEX 编写

---

## 三、程序化建模知识体系

### 3.1 基础建模操作

- 移动、旋转、缩放、阵列、镜像
- 放样（Skin / Sweep）
- 挤出厚度
- 倒角
- Group Node（精确筛选元素）
- **模块化思维**：组件 → 复制到点

### 3.2 程序化核心概念

- **全局变量**：控制参数设置
- **数组筛选 & 参数定义**
- **VOP**：可视化编程（噪波、纹理、属性操作）
- **VEX**：代码级控制
- **算法**：三维波函数坍塌算法
- **Copy Stamp**：传统方法，设定随机种子，但运算量大
- **For Each Loop**：推荐方式（Single Pass、遍历循环、分形）
- **L-System**：植物骨架程序化生成
- **噪波**：Unified Noise，控制散布、置换、纹理

### 3.3 程序化建模案例

| 类型 | 案例 | 知识点 |
|------|------|--------|
| 资产 | 链条制作 | 打包 Asset 工具 |
| 资产 | 石墩资产 | 数字资产完整制作流程 |
| 石头 | 小石头 / 大岩石 | VDB、噪波、置换、泰森多边形、渲染 |
| 建筑 | 残垣断壁 | 程序化建模 + 贴图 + 渲染 |
| 桥梁 | 索桥 / 吊桥 | 曲线、VEX、UE 联动 |
| 管道 | 管道生成 | 曲线路径建模 |
| 城市 | 建筑城市 | 大面积建筑生成 |
| 城墙 | 模块化拼接 | 逻辑介绍、模块化拼接 |
| UV | 拆 UV | 基本节点 + GameDev（现 Lab）工具 |

---

## 四、城市生成

### 4.1 核心目标
快速创造大规模城市背景，重点位置手动布置建筑，简化单体但强调整体丰富性。

### 4.2 城市肌理
- **OSM 路网**：利用 OpenStreetMap 数据生成路网
- **肌理图生成分区**
- **灰度图控制高度分布**

### 4.3 道路生成
- 十字路口红绿灯
- 斑马线

### 4.4 单体建筑模块
- **三段式结构**：首层（3种高度）+ 标准层（1种高度）+ 屋顶（单独设施生成）
- TITAN 项目建筑模块
- 模块列表生成不同肌理

### 4.5 关键教程
- City Building with OSM Data（SideFX 官方）
- TITAN 单体建筑模块组装
- PDG 结合 UE 分区渲染
- Procedural Everything（程序化全世界）

---

## 五、地形与散布

### 5.1 地形系统
- Houdini Terrain 地形系统
- Houdini 17.5 地形与 UE4/UE5 联动
- 地形封装 + 散布制作 + 导入游戏引擎

### 5.2 散布技术
- **Scatter Node**：在表面放置随机点
- 驱动方式：点数、纹理、密度属性
- **属性 VOP**：根据噪波颜色散布
- **程序限定散布条件**：植被分布真实性
- **Attribute Transfer**：基于空间位置传递信息（如树根随山坡变化）

### 5.3 植物
- 棕榈树（SOP 综合 + Copy）
- L-System 植物骨架生成
- SpeedTree 对比：L-System 更适合大批量、不重复的远景树木

---

## 六、古建筑程序化生成（苏式自宅）

### 6.1 整体方法论
> **先逻辑梳理，写注释，再连节点，调参数**

### 6.2 建筑类型
- **屋顶**：硬山、歇山、悬山
- 屋顶瓦片程序化生成
- **门窗**：小扇、大小扇
- **木作装饰**：挂落、美人靠

### 6.3 廊子架构
- 样条线等分 → 地面放点确定柱子位置
- 坡屋顶体量
- 单个构件：柱子、挂落、椽子

### 6.4 中式景观
- 石头堆叠、廊子、亭子、桥

### 6.5 服务内容
- 给定平面范围，基础平面功能
- 完整模型生成，批量修改
- 动画漫游

### 6.6 AI 辅助
- 辅助编程
- 辅助素材批量整理

### 6.7 GH 背景
- 硬山/悬山/歇山纯木构古建筑逻辑梳理
- 程序化地形、竹里建筑屋顶结构
- Kangaroo 力学模拟、RhinoScript

---

## 七、UE 与 Houdini 联动（HDA to UE）

### 7.1 工作流
- **HDA 封装** → Houdini Engine → UE 中调整参数
- UE-HDA 批量复制、动力学解算
- UE-PCG 与 Houdini 协同

### 7.2 关键技术点
- 只输出点，UE 中用模型替换
- Instance Attribute（模型替换、轴心方向）
- 曲线处理（轨道、藤蔓、栏杆、管道、揽绳）
- PCG 植被组团、工厂单体建筑、山体/悬崖

### 7.3 游戏 Pipeline
- 建模 → 高低模 → 烘焙贴图 → 模块化组装 → UE5 PCG
- 封装工具组合，给美术使用，支持多次编辑

---

## 八、招聘技术栈与能力匹配

### 8.1 企业需求方向

| 公司 | 方向 |
|------|------|
| 友塔 | PDG、场景性能优化、TA 写工具给美术、城市建筑 |
| 网易（漫威争锋） | 破损效果 |
| 叠纸 | 程序化地形、PCG 开发 |
| D5 | 素材生成（石头/植物/路灯/桥梁）、智能排布（景观/城市/室内） |

### 8.2 作品集方向
- **UE PCG**：植被组团、工厂单体建筑、山体/悬崖
- **Houdini 地形**
- **Houdini 建筑**：基础形体模块分色、屋顶生成、破碎效果、立面图表、PDG 流程
- **Houdini 工具**：藤蔓、桥梁、悬崖
- **诺亚城市**：场地划分、建筑体量容积率调整
- **PCG 应用报告**：Houdini 与 UE 的优缺点

### 8.3 个人优势
- 多年参数化设计经验
- GH 学习案例（程序化地形、古建筑、Kangaroo、RhinoScript）
- Python 基础
- 诺亚智能设计经验（定容城市、自动立面生成）

---

## 九、核心学习资源索引

### 9.1 SideFX 官方（最重要）
- [SideFX 官网教程](https://www.sidefx.com/tutorials/)
- [Simon 系列教程](https://www.sidefx.com/tutorials/author/Simon_V/)（游戏流程重点）
- [HDA to UE 官方](https://www.youtube.com/watch?v=WjdgHCAgrBM&list=PLXNFA1EysfYkc2-O6qaQj5t0Km9W8CjEl)
- [City Building with OSM Data](https://www.youtube.com/watch?v=FQ_DKhSyelY&list=PLXNFA1EysfYkFzKS--S3_3393X2z1F_e0&index=1)
- [Procedural Everything](https://www.youtube.com/watch?v=xy6dewe8XBw)
- [Favela Dystopia 大型贫民窟](https://www.sidefx.com/tutorials/favela-dystopia-creating-vast-environments/)
- [官方 to UE PCG](https://www.youtube.com/watch?v=4LDVt2RBywU&list=PLXNFA1EysfYmttAEPvIlJDWGgTRhx0OFS&index=1)

### 9.2 TITAN 系列课程（Simon 主讲，极度推荐）
- [B站整理链接](https://www.bilibili.com/video/BV1om421K7aA/)
- 单体建筑模块组装、轨道、藤蔓、平台、栏杆、散布盒子、布料解算、列车碰撞特效、揽绳、管道

### 9.3 Houdini Kitchen 系列
- [官网](https://www.houdinikitchen.net/)：14 个全面入门教程
- 涵盖：Network/Node → Transform → Geometry Primitives → VOPs → Merge → Scatter → Group → HDA → Attribute Transfer → Volumes/VDB → Lines/Curves → Copy Stamp & For Each → UV → L-Systems

### 9.4 橘柚系统教程（B站 o橘柚o）
- 入门基础：Houdini18 官方入门 → CG猎人 → Entagma
- 基础案例：Rohan Dalvi 系列（Rocket Bus、浮空岛、各种案例）
- 程序化建模：棕榈树、矿物分型、有机几何、蛋糕建模、陨石资产
- 游戏 Pipeline：Mixtraining、Simon 系列、UE4/U3D 写实赛车游戏
- 地形系统、L-System、VOP/Mantra 程序化纹理
- VEX：入门（捷佳）→ 中级（树木HDA、Python城市）→ 高级（湖边小屋）
- Python、PDG、USD/Solaris

### 9.5 国内资源
- [VFX FORCE](https://www.vfxforce.cn/)：各类 CG 资源
- [AboutCG](https://www.aboutcg.org/)：付费课程
- [特效向](https://iiivfx.com/archives/tag/mianfei)
- [Houdini Foundations 中文翻译](https://houdini-foundations.readthedocs.io/zh-cn/latest/views/overview/index.html)
- B站 up：houdini666、爱情吃豆腐干

### 9.6 国际平台
- [CGCircuit](https://www.cgcircuit.com/)：Houdini 专门课程
- [Rebelway](https://www.rebelway.net/learn)：影视特效（免费工程文件）
- Udemy、Pluralsight、CGMA、LinkedIn Learning、Gumroad

### 9.7 社区
- Reddit: r/Houdini
- Houdini Artists Facebook Group
- Gnomon School、Vancouver Film School

---

## 十、推荐学习路线

### 阶段一：快速入门
1. Houdini18 官方入门教程（UI、基础操作、属性、Copy、VOP/VEX 入门）
2. CG猎人 B站基础教程（特别是 For 循环讲解）
3. Houdini Kitchen Tutorials 1-7（节点、变换、几何、VOP、散布、Group）

### 阶段二：游戏流程
1. Simon 系列教程（GameDev / Lab 工具、HDA 导入 UE）
2. UE-HDA 联动官方教程
3. 写实赛车游戏教程（17小时完整流程）

### 阶段三：专项深入
1. **城市生成**：OSM 数据 → 路网 → 建筑模块 → PDG
2. **地形散布**：Terrain 系统 → Scatter → 属性控制
3. **VEX**：捷佳入门 → 树木 HDA → 湖边小屋
4. **古建筑**：GH 逻辑 → Houdini 程序化屋顶/廊子/构件

### 阶段四：工具化
1. HDA 封装（数字资产制作）
2. PDG 批量处理
3. 封装工具给美术使用

---

## 附：源文件索引

| 原文件 | 核心内容 |
|--------|----------|
| [[01_招聘技术栈梳理]] | 岗位技术需求、能力匹配、作品集规划 |
| [[02_官方课程]] | SideFX 官方教程索引、TITAN 系列、游戏流程 |
| [[03_城市生成]] | OSM 路网、建筑模块、城市肌理 |
| [[04_框架整理]] | 知识框架、模块体系、学习资源汇总 |
| [[05_houdinikitchen]] | Houdini Kitchen 14 个教程详解 |
| [[06_VEX]] | VEX 语言学习路线与案例 |
| [[07_橘柚]] | 橘柚系统化入门教程指南（SOP→VEX→Python→PDG） |
| [[08_程序化建模案例]] | 建模+程序化案例合集 |
| [[09_学习资源]] | 学习平台与社区资源 |
| [[10_苏式自宅]] | 古建筑程序化生成（GH+Houdini） |
| [[11_操作及名词解释]] | 基础操作、网络类型、名词概念 |
