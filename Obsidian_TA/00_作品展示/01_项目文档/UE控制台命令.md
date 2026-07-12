## UE控制台命令

▼ r.Shadow.Virtual.Enable 

■ 1为启用虚拟阴影贴图

▼ r.ForceLOD 0 

■ 强制LOD 0

▼ r.RayTracing.shadows 

- 光追阴影开关，0关闭，1打开

▼ r.RayTracing.culling 

- 光追阴影剔除范围，范围1-3, 1剔除最少

▼ r.RayTracing.Geometry.InstancedStaticMeshes.Culling 

- 影响绘制的Foliage光追阴影（0解决拉远消失的问题）

r.Shadow.DistanceScale=2 

- 默认为1,2可以增加阴影绘制距离

▼ r.Shadow.Virtual.UseFarShadowCulling 0 

- 使非Nanite几何体的远距离阴影方式与Nanite相同

▼ r.RayTracing.NormalBias 

- 提高可以解决光追植物黑斑阴影问题

▼ r.RayTracing.Nanite.Mode 1 

- 默认是0，解决光追阴影模型下Nanite的三角形黑斑问题

▼ r.Shadow.Virtual.NormalBias 1 

- 法线偏移：有些低模型的阴影会有锯齿，默认值是0.5，提高就可以解决模型上的阴影锯齿

▼ r.RayTracing.Shadows.EnableTwoSidedGeometry 0 

- 模型转换成Nanite表面出现错误的阴影

▼ 阴影剔除（非nanite几何体）

▼ r.Shadow.Virtual.UseFarShadowCulling 

- 关闭非nanite几何体的远阴影剔除，0为关闭，1为开启。

▼ r.Shadow.RadiusThreshold 

- 阴影面积阈值剔除，为非nanite几何体的阴影设置一个面积阈值，小于某个值的时候，就关闭阴影。默认0.03，越小，剔除的越少。如果是0，就关闭

▼ r.Streaming.PoolSize 

- 当你的场景稍微复杂一些的时候，默认纹理流送池就会被挤爆，导致部分贴图加载成很小的lod，画面会糊。默认有1G显存分配给了纹理流送池，不够用的时候可以手动调大。比如，r.Streaming.PoolSize 4096，就可以分配4G显存给纹理流送池。这个参数吧，量力而行就可以了。当然，懒人最爱用的是r.Streaming.PoolSize 0，可以设置纹理流送池无上限。


## - UE5 控制台命令汇总-渲染（一）

UE5 控制台命令汇总-渲染（一）ue5...

- 抗锯齿 (TAA) 将使边缘更平滑，减少渲染中的锯齿线。

- r.TemporalAASamples=32
(值越高边缘越平滑，但会增加 GPU 负载。)

- r.TemporalAACurrentFrameWeight=0.1
(控制时间性抗锯齿的混合权重。值越低，重影越少，但可能会出现闪烁。)

2. 屏幕空间反射 (SSR) 将提供更清晰、更细致的反射。

- r.SSR.Quality=4
(屏幕空间反射的最高质量。)

- r.SSR.HalfResSceneColor=0
(禁用半分辨率渲染以获得更好的清晰度。)

3. 阴影将变得更清晰、更逼真，并具有更远的绘制距离和更高的分辨率。

- r.ShadowQuality=5 (最高阴影质量。)

- r.Shadow.MaxResolution=4096
(提高阴影分辨率以获得更清晰的阴影。)

- r.Shadow.DistanceScale=2 (增加阴影绘制距离。)

4. 环境光遮蔽 (AO) 将改善缝隙和物体之间的阴影，使光照看起来更自然。

- r.AmbientOcclusionLevels=3 (定义AO的级别数。)

diusScale=2.0
(更宽的环境光遮蔽半径，使缝隙中的阴影更柔和。)

5. 纹理设置将使你的纹理显得更清晰，尤其是在从一定角度或远处观看时。

- r.Streaming.MipBias=-3
(强制使用更高分辨率的 Mipmap。)

- r.MaxAnisotropy=16
(最大化各向异性过滤，使倾斜角度的纹理更清晰。)

6.光照质量和全局光照将确保逼真的光照和反射，尤其是在使用 Lumen 的情况下。

- r.LightingDetailMode=2 (启用完整的光照细节。)

- r.HZBOcclusion=1
(启用高质量的基于地平线的环境光遮蔽。)

- r.VolumetricFog=1
(启用体积雾，以获得更好的光照效果。)

- r.Lumen.Reflections.HitLighting=1
(确保Lumen反射包含命中光照，从而使反射表面上的光照更准确。)

- r.Lumen.Reflections.HierarchicalScreenTraces
(为Lumen反射启用分层屏幕追踪，提高场景中反射的精度和质量。)

### 7. 景深

- r.DepthOfFieldQuality=4 (启用高质量的景深。)

### 8. 运动模糊

- r.MotionBlurQuality=4
(最大化运动模糊质量，以获得更平滑的过渡。)

9. 后期处理效果，如泛光、景深和运动模糊，将具有更高的质量和更具电影感的画面。

- r.PostProcessAAQuality=6
(提高后期处理中的抗锯齿质量。)

- r.BloomQuality=5
(最高的泛光质量，用于电影级光照。)

10. 屏幕百分比提升超采样，以获得更高的像素密度和更清晰的图像。

- r.ScreenPercentage=200
(将渲染分辨率提升至 200% 以进行超采样。根据性能进行调整。)

11. 光线追踪（如果支持）可以进一步提升反射、阴影和全局光照质量。

• r.RayTracing.Reflections=1 

(启用光线追踪反射，对于支持的硬件，它比屏幕空间反射更准确。)

• r.RayTracing.Shadows=1 

(启用光线追踪阴影，提高阴影的精度和柔和度。)

• r.RayTracing.GlobalIllumination=1 

(启用光线追踪全局光照，以获得更逼真和动态的光照。)

### 12. 虚拟纹理

• r.VirtualTextures=1 

(启用虚拟纹理以便更好地管理大型纹理的内存。)

• r.VT.TileSize=128 

(增加图块大小以获得更清晰的纹理。)

### 13. 帧率 (可选)

• t.MaxFPS=60 or t.MaxFPS=120 

(调整最大帧率以平衡质量和性能。)