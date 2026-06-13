## **3D场景模型制作基本设置和制作规范及参考**

- 使用软件版本

- 3DMAX基本设置

- 导出FBX设置

- UV规范

- 模型制作规范和参考

- 命名规范

- 图层规范(暂无)

- 提交模板（暂无）

- 碰撞和LOD制作（暂无）

- 使用软件版本

1. MAX使用版本：MAX2017（暂定）

2. ZBRUSH版本：ZBrush 4R7（暂定）

3. SP版本：SP2017（暂定）

4. MAX单位设置：CM（厘米）

![](https://cdn-mineru.openxlab.org.cn/result/2026-06-10/9132a1ca-f926-4bce-a9a2-810e657f73e4/5a153b30ea5bee72447cffc2e1342352b541afa37e3f33d9e08f4ae1ebe2f860.jpg)

5. MAX网格设置

![](https://cdn-mineru.openxlab.org.cn/result/2026-06-10/9132a1ca-f926-4bce-a9a2-810e657f73e4/d1755eae307ffc95e8bbf92aae1677e802decfc0ddb0ee4741c21430856ed0c1.jpg)

二、3DMAX基本设置

1. 模型命名和材质球命名需一致

2. 模型坐标需要归到原点且是物件底部

3. 归到原点后模型需要增加“RESET XFORM”

4. 检查ID和光滑组是否正确（光滑组必须与烘焙法线一致）

5. 检查2u是否符合制作规范

6. 多张贴图的单个物体，不能使用多维子材质球，需要一张贴图一个材质球、并且根据模型ID(贴图)吧模型断开

7. 导出时选中所有子模型（或者建组）导出为一个FBX

三、导出FBX设置

1.红框处勾选，箭头处不要勾选，按照这个导出设置导出。

![](https://cdn-mineru.openxlab.org.cn/result/2026-06-10/9132a1ca-f926-4bce-a9a2-810e657f73e4/3703abe923309704135102fd19d4c8630857ec5ef0433f2dc0ea5fec94f68c07.jpg)

2. 贴图导出格式为TGA

- UV规范

1. 第一套UV（albedo）：最大化使用贴图UV，考虑共用和面数，可以适当放大一些贴图细节较多或模型占比较大的面。当然一些背面或底面可以适当缩小UV面积,尽可能的填满。（UV不得出0,1区间）

![](https://cdn-mineru.openxlab.org.cn/result/2026-06-10/9132a1ca-f926-4bce-a9a2-810e657f73e4/fcee23b7683a0236c83b28a2bcf759adb9eed07b30fb1cfbc150d8d413797228.jpg)

2. 第二套UV（Lightmap）：需要全展，不能有任何重叠面，不能浪费UV，UV断开需要在朝下或内侧部分断开，禁止断开朝上或视觉直视点处的线。并且UV间距在512贴图精度上，保持2-4个像素的距离。主要UV边框保持间距4-6个像素。贴图空间实在填不满的，尽量完整的空出右侧区域或下半部分区域，这样引擎再计算烘焙的时候会将其他模型的UV自动化的安排到这个没有填满的区域。

![](https://cdn-mineru.openxlab.org.cn/result/2026-06-10/9132a1ca-f926-4bce-a9a2-810e657f73e4/9b6f391bb502b1c73e6d0a115059eb6798300acd66ed6e196869a00566f2dfc3.jpg)

- 模型制作规范和参考

大方向制作规范：

中模制作:按人比，根据手机游戏大小，适当删掉不必要的细节和结构或合并减少细节结构，使物件更加整体。

高模制作：重点在外轮廓和体块结构上，雕刻大结构、大倒角、结构概括且清晰明了。切勿雕得细碎、过多小细节、生硬和噪点细节。倒角小的话，烘焙不出法线或法线结构过小。

低模：注意面数分配，面数优先外轮廓和大结构，细小结构使用NORMAL MAP表现。布线需要按照结构布线，避免奇怪状的三角面或四边面。

贴图：各通道颜色严格按照PBR参考表输出，上下不得超过20%，切记脏、乱。贴图精度1米对应256像素。

高模制作注意事项

1. 雕刻造型尽量饱满，不要出现结构穿插的过锐结构。
2. 雕刻时，注意结构衔接处需要合理自然，不要生硬。
3. 注意好各体块之间的节奏感，有明确的层次关系。
4. 所有内凹结构，需要增强切斜角度，保证能烘焙到结构饱满的法线。

六、命名规范

1. 资源分类：

① 建筑 build

② 树 tree

③ 石头 stone

④ 草（灌木类）grass

⑤ 地形（地设）terrain
⑥ 通用物件（小环境物件） small

\*其中通用物件、 树、植被、石头、草为通用物件（通用物件命名前缀需要加common标识），原画设计阶段就应该充分考虑资源的复用，也方便模型制作同学拆分制作。避免重复制作近似资源，浪费工作量，增加不必要的包体和消耗。特殊风貌地图资源提前规划好，同样作为通用物件制作，方便其他项目调用素材。

2. MAX模型命名规范：

- 建筑 build

地图命名\_build+编号

例如：墓地场景\_build+编号 :  cemetery\_build\_01  当然也会出现同一张贴图做不同造型的情况，这时候我们只需要在模型编号后面加入 a b c d以此类推字样即可。

假设 墓地场景房子有3种变体，共用了同一张贴图。那么我们场景资源的命名：

cemetery\_build\_01a

cemetery\_build\_01b

cemetery\_build\_01c

- 非建筑类 考虑复用的资源 tree stone grass terrain small

Common\_物件的英文命名+编号

![](https://cdn-mineru.openxlab.org.cn/result/2026-06-10/9132a1ca-f926-4bce-a9a2-810e657f73e4/3d1b78a75b62b1fee67052104c0f63847df2827f0980b73485e7a6b1de180864.jpg)

例如：

图中 a b c d e 是用了相同的材质不同的造型

3. 材质命名规范：

贴图储存格式为TGA，没有Alpha通道的为24位，有Alpha通道的为32位。贴图命名需要对应模型的类型，再此基础上扩展后缀名即可。

Albedo  D

Normal  N

Mask（R（Smooth），G（metallic），B（AO））  M
Emission  E

例如：

模型命名：

Common\_candle\_01a

Common\_candle\_01b

Common\_candle\_01c

贴图命名：

Common\_candle\_01\_d(albedo)

Common\_candle\_01\_n(normal)

Common\_candle\_01\_m(mask)

Common\_candle\_01\_e(emission)