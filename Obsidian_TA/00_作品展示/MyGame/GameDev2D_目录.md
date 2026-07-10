
# GameCity2D — 2D城市/世界生成与设计系统 — 文档大纲

## 一、游戏案例参考
- 1.1 国外案例（星露谷物语、奥日、The Messenger）
- 1.2 国内案例（风来之国、戴森球计划、小白兔电商、大多数）

## 二、引擎选型
- 2.1 Godot + AI（核心引擎、AI辅助、程序化生成、社区资源、集成方案）
- 2.2 TaptapMaker（定位、优势、限制、使用建议）

## 三、策划设计
- 3.1 玩法设计
  - 核心循环
  - 主要玩法模块（探索、采集/战斗、经营/建造、社交、成长）
  - 地图结构（世界地图 → 主城 → 野外区域 → 隐藏区域）
- 3.2 美术设计方向（像素风、手绘风、矢量扁平风、像素+现代光影）

## 四、美术资源
- 4.1 美术参考平台（Pinterest、ArtStation、DeviantArt、Itch.io）
- 4.2 免费/开源资产网站（OpenGameArt、itch.io、Kenney.nl、Craftpix、Freepik）
- 4.3 AI 资产生成平台（Midjourney、Stable Diffusion、Leonardo.ai、Scenario、Pixelicious）
  - 工作流建议

## 五、程序实现
- 5.1 地形算法
  - 5.1.1 WFC（波函数坍缩）—— 核心思想、应用场景、Godot实现方式
  - 5.1.2 柏林噪声 —— 核心思想、应用场景、Godot实现方式（含代码示例）
- 5.2 Gameplay 系统（角色控制、物品系统、NPC系统、任务系统、时间系统、存档系统）
- 5.3 UI 系统（主菜单、HUD、背包、对话系统、任务面板）
- 5.4 渲染管线（CanvasItem、TileMap、Light2D、Shader、视口分层、渲染顺序管理、性能优化要点）

## 六、开发路线图
- Phase 1：可玩原型（2-4周）
- Phase 2：核心机制（4-6周）
- Phase 3：程序化生成（4-6周）
- Phase 4：美术完善（6-8周）
- Phase 5：打磨上线（4-6周）