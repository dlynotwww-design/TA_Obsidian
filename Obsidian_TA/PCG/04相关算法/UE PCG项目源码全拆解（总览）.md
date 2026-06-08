---
title: "UE PCG项目源码全拆解（总览）"
source: "https://zhuanlan.zhihu.com/p/1990473018858808349"
author:
  - "[[风中翠竹​电子游戏行业 从业人员]]"
published:
created: 2026-06-09
description: "前言只管开坑，不管填坑，之前开这么多坑有没有好好填啊kusoyarooooooo~！！！ 没错，又来开新坑了，这个坑是用来拆解UE的PCG的项目源码的，出于UE PCG目前已经在5.7达到了预备生产的级别，后续肯定会成为UE的重要…"
tags:
  - "clippings"
---
[收录于 · 计算几何](https://www.zhihu.com/column/c_1933675449441050793)

20 人赞同了该文章

目录

收起

前言

项目架构

核心的类层次

UPCGSubsystem (世界子系统)

UPCGComponent (PCG组件)

UPCGGraph (图资产)

UPCGGraphInstance (图实例)

UPCGNode (图节点)

UPCGPin (引脚)

UPCGEdge (边)

FPCGGraphExecutor (图执行器)

FPCGGraphCompiler (图编译器)

FPCGGraphTask (图任务)

FPCGGraphActiveTask (活跃任务)

IPCGElement (元素接口)

UPCGSettings (设置基类)

UPCGSettingsInterface (设置接口)

UPCGData (数据基类)

FPCGDataCollection (数据集合)

FPCGTaggedData (带标签数据)

UPCGManagedResource (管理资源基类)

UPCGManagedActors (管理Actor)

UPCGManagedComponent (管理组件)

UPCGManagedISMComponent (管理ISM组件)

UPCGProxyForGPUData (GPU数据代理)

节点定义

节点分类和位置

节点定义的标准结构

节点注册和发现

PCG支持的数据类型

1\. 基础数据类型枚举（EPCGDataType）

点数据（Point）

曲线/样条数据（PolyLine/Spline）

表面数据（Surface）

体积数据（Volume）

图元数据（Primitive）

动态网格（DynamicMesh）

静态网格资源（StaticMeshResource）

组合数据（Composite）

空间数据（Spatial）

参数数据（Param/Attribute Set）

2\. 数据类型层次结构

3\. 数据类型操作能力

点数据（Point）操作

空间数据（Spatial）通用操作

表面数据（Surface）操作

体积数据（Volume）操作

样条数据（Spline）操作

组合数据（Composite）操作

## 前言

只管开坑，不管填坑，之前开这么多坑有没有好好填啊kusoyarooooooo~！！！

---

没错，又来开新坑了，这个坑是用来拆解UE的PCG的项目源码的，出于 [UE PCG](https://zhida.zhihu.com/search?content_id=268484026&content_type=Article&match_order=1&q=UE+PCG&zhida_source=entity) 目前已经在5.7达到了预备生产的级别，后续肯定会成为UE的重要功能模块之一，对比 [Houdini](https://zhida.zhihu.com/search?content_id=268484026&content_type=Article&match_order=1&q=Houdini&zhida_source=entity) 有不可替代的优势，为了帮助开发人员能够在实际项目中使用PCG，并且可以对PCG插件进行二次开发，故而写下这个系列，本次系列大概是会填完，不会和之前的很多坑一样半途而废了~(因为有个笨蛋天天催我，受不了了！！)

---

## 项目架构

**项目位于\\Engine\\Plugins\\PCG下。**

**主要需要研究的是\\Engine\\Plugins\\PCG\\Source下面的三个部分，会大概带一下\\Engine\\Plugins\\PCG\\Shaders下面的部分。**

在Source文件夹下面有三个核心模块：

- PCG：核心运行时模块
- PCGEditor：编辑器模块
- PCGCompute：GPU计算模块（依赖ComputeFramework）

## 核心的类层次

### UPCGSubsystem (世界子系统)

*相当于PCG 系统的中央管理器：*

- 组件注册/注销：管理所有 PCG 组件的生命周期
- 任务调度：通过ScheduleComponent()、ScheduleGraph()、ScheduleGeneric()调度执行
- 分区管理：管理APCGPartitionActor和本地组件
- 缓存管理：提供图缓存接口 IPCGGraphCache
- 运行时生成：FPCGRuntimeGenScheduler 管理运行时生成
- 八叉树： [PCGComponentOctree](https://zhida.zhihu.com/search?content_id=268484026&content_type=Article&match_order=1&q=PCGComponentOctree&zhida_source=entity) 用于空间查询

生命周期继承自UTickableWorldSubsystem，每帧调用 Tick()

大部分操作线程安全，使用锁保护

### UPCGComponent (PCG组件)

*附加到 Actor 的组件，是 PCG 的执行入口：*

关键属性：

- GraphInstance：持有的图实例（UPCGGraphInstance）
- GeneratedResources：生成的资源列表（UPCGManagedResource）
- CurrentGenerationTask：当前生成任务ID
- GenerationGridSize：生成网格大小

关键方法：

- Generate() / GenerateLocal()：触发生成
- Cleanup() / CleanupLocal()：清理生成结果
- GetPCGData()：获取组件数据（Actor、Landscape等）

执行状态：FPCGComponentExecutionState 实现 IPCGGraphExecutionState

分区支持：bIsComponentPartitioned 控制是否分区，分区时创建本地组件

### UPCGGraph (图资产)

*PCG 图的定义，包含节点和边。也就是连连看实现啦~*

关键属性：

- Nodes：节点数组
- InputNode / OutputNode：输入/输出节点
- UserParameters：用户参数（FInstancedPropertyBag）
- CookedCompilationData：编译后的数据（用于运行时）

关键方法：

- AddNode() / RemoveNode()：节点管理
- AddEdge() / RemoveEdge()：边管理
- GetNodeGenerationGridSize()：获取节点网格大小

分层生成：bUseHierarchicalGeneration 启用分层生成，HiGenGridSize 定义默认网格

### UPCGGraphInstance (图实例)

*图的实例化，支持参数覆盖。目的是允许同一图在不同组件中使用不同参数*

关键属性：

- Graph：指向的图（UPCGGraphInterface）
- ParametersOverrides：参数覆盖（FPCGOverrideInstancedPropertyBag）

### UPCGNode (图节点)

*图中的节点，连接 Settings 和 Element*

关键属性：

- SettingsInterface：设置接口（ [UPCGSettingsInterface](https://zhida.zhihu.com/search?content_id=268484026&content_type=Article&match_order=1&q=UPCGSettingsInterface&zhida_source=entity) ）
- InputPins / OutputPins：输入/输出引脚数组
- NodeTitle：节点标题

关键方法：

- UpdatePins()：根据设置更新引脚
- GetPassThroughInputPin() / GetPassThroughOutputPin()：禁用时的透传引脚

引脚管理：引脚通过 UPCGPin 对象管理，支持动态类型

### UPCGPin (引脚)

*节点的输入/输出连接点，类似于Houdini节点的多个输入和输出~*

关键属性：

- Properties：引脚属性（FPCGPinProperties）
- Label：引脚标签
- AllowedTypes：允许的数据类型
- PinStatus：状态（Normal/Required/Advanced）
- Usage：用途（Normal/Loop/Feedback）
- Edges：连接的边数组

关键方法：

- AddEdgeTo() / BreakEdgeTo()：连接管理
- IsCompatible()：兼容性检查

### UPCGEdge (边)

*负责节点间的连接，定义数据流向*

关键属性：

- InputPin：上游引脚
- OutputPin：下游引脚

### FPCGGraphExecutor (图执行器)

*图（节点）的编译和执行调度*

关键组件：

- GraphCompiler：图编译器（FPCGGraphCompiler）
- GraphCache：图缓存（FPCGGraphCache）
- Tasks：任务映射（TMap<FPCGTaskId, FPCGGraphTask>）
- TaskOutputs：任务输出（TMap<FPCGTaskId, FOutputDataInfo>）

执行流程：由Schedule()调度图执行，然后Execute()每帧调用执行任务，由ProcessScheduledTasks()处理待执行任务，再有QueueNextTasks()负责队列后续任务。

有如下几个任务状态：

- ScheduledTasks：已调度任务
- ReadyTasks：就绪任务
- ActiveTasks：活跃任务（多线程）
- ActiveTasksGameThreadOnly：主线程任务
- PausedTasks：暂停任务

使用多级锁来保证线程安全~

### FPCGGraphCompiler (图编译器)

*将图（节点）编译为任务列表*

关键方法：

- Compile()：编译图
- GetCompiledTasks()：获取编译后的任务
- CullTasks()：剔除不需要的任务

**编译结果存储在 FPCGGraphCompilerCache 中**

**编译时也有一些优化，但是不重要，这里就不写了~**

### FPCGGraphTask (图任务)

*编译后的单个执行任务*

关键属性：

- Inputs：输入任务列表（FPCGGraphTaskInput）
- Element：执行元素（FPCGElementPtr）
- Node：关联节点
- Context：执行上下文
- ElementSource：元素来源（Trivial/FromNode/FromCookedSettings等）
- PinDependency：引脚依赖表达式

任务输入：FPCGGraphTaskInput 包含：

- TaskId：上游任务ID
- UpstreamPin / DownstreamPin：引脚信息
- bProvideData：是否提供数据
- bIsUsedMultipleTimes：是否被多次使用

### FPCGGraphActiveTask (活跃任务)

*正在执行的任务*

- 关键属性：
- Element：执行元素
- Context：执行上下文（TUniquePtr<FPCGContext>）
- ExecutingTask：执行任务（UE::Tasks::TTask<bool>）
- bIsGameThreadOnly：是否仅主线程

生命周期从 ReadyTasks 移动到 ActiveTasks，执行完成后清理。

***Element 是 PCG 中节点执行逻辑的实现。架构上采用“配置与执行分离”***

***Settings定义节点配置、引脚属性、可序列化属性而Element实现节点的执行逻辑***

### IPCGElement (元素接口)

*节点执行逻辑的抽象接口*

关键方法：

- Initialize()：初始化上下文
- Execute()：执行（可多次调用直到返回true）
- Abort()：中止执行
- IsCacheable()：是否可缓存
- GetDependenciesCrc()：获取依赖CRC

在执行阶段：PreExecute()负责执行前准备，PrepareData()准备数据，ExecuteInternal()核心执行（虚函数），PostExecute()执行后处理。

特殊元素：

- FPCGFetchInputElement：获取输入元素
- FPCGPreGraphElement：图前处理元素
- FPCGGenericElement：通用元素（用于lambda）
- FPCGGridLinkageElement：网格链接元素

### UPCGSettings (设置基类)

*负责节点配置和引脚定义*

关键方法：

- CreateElement()：创建元素（纯虚函数）
- InputPinProperties() / OutputPinProperties()：定义引脚属性
- GetElement()：获取元素（带缓存）

关键属性：

- Seed：随机种子
- bEnabled：是否启用
- CachedOverridableParams：可覆盖参数列表

参数覆盖：支持通过图参数覆盖设置属性。

### UPCGSettingsInterface (设置接口)

*设置的接口抽象，支持节点使用共享设置或实例化设置*

实现类：

- UPCGSettings：直接设置
- UPCGSettingsInstance：设置实例（持有设置引用）

### UPCGData (数据基类)

*所有PCG数据的基类*

关键属性：

- UID：唯一ID
- Crc：CRC校验值
- Metadata：元数据（UPCGMetadata）

关键方法：

- GetOrComputeCrc()：获取或计算CRC
- DuplicateData()：复制数据
- VisitDataNetwork()：访问数据网络

数据类型则通过 GetDataType() 返回类型枚举

### FPCGDataCollection (数据集合)

*节点间传递的数据集合*

关键属性：

- TaggedData：带标签的数据数组（TArray<FPCGTaggedData>）
- DataCrcs：数据CRC数组
- InactiveOutputPinBitmask：非活跃输出引脚位掩码

关键方法：

- GetInputsByPin()：按引脚获取输入
- GetSpatialInputsByPin()：按引脚获取空间数据
- GetAllSettings()：获取所有设置
- GetAllParams()：获取所有参数

### FPCGTaggedData (带标签数据)

*单个数据项的包装*

关键属性：

- Data：数据指针（FPCGDataPtrWrapper）
- Tags：标签集合
- Pin：引脚名称
- bIsUsedMultipleTimes：是否被多次使用
- OriginalIndex：原始索引（用于缓存）

FPCGContext (执行上下文)

Element执行时的上下文信息

关键属性：

- InputData / OutputData：输入/输出数据集合
- ExecutionSource：执行源（IPCGGraphExecutionSource）
- Node：关联节点
- TaskId：任务ID
- CurrentPhase：当前执行阶段
- SettingsWithOverride：带覆盖的设置
- AsyncState：异步状态

关键方法：

- GetInputSettings<T>()：获取输入设置（带覆盖）
- GetSeed()：获取种子
- ScheduleGraph()：调度子图
- StoreInCache() / GetFromCache()：缓存操作

线程安全：支持多线程创建对象（NewObject\_AnyThread()）

### UPCGManagedResource (管理资源基类)

管理PCG生成的资源

关键方法：

- Release()：释放资源
- ReleaseIfUnused()：释放未使用的资源
- MoveResourceToNewActor()：移动到新Actor

关键属性：

- Crc：资源CRC
- bIsMarkedUnused：是否标记为未使用

### UPCGManagedActors (管理Actor)

管理生成的Actor

### UPCGManagedComponent (管理组件)

管理单个组件

### UPCGManagedISMComponent (管理ISM组件)

管理实例化静态网格组件

### UPCGProxyForGPUData (GPU数据代理)

GPU数据的CPU代理，允许CPU节点访问GPU数据，按需回读

关键方法：

- GetCPUData()：获取CPU数据（触发GPU->CPU回读）
- GetElementCount()：获取元素数量（不触发回读）

## 节点定义

Elements和Settings是PCG非常重要的概念。

每个节点通常包含两个类：

1.Settings类：UPCG\[节点名\]Settings

- 继承自 UPCGSettings
- 定义节点配置、引脚属性
- 位置：Public/Elements/\[节点名\].h

2.Element类：FPCG\[节点名\]Element

- 继承自 IPCGElement
- 实现执行逻辑
- 位置：同一头文件中（或单独的命名空间）

### 节点分类和位置

节点的位置都定义在Public/Elements位置下

大致可分为：

1\. 基础点操作节点

2\. 生成器节点

3\. 生成节点（Spawner）

4\. 属性/元数据操作节点（Public/Elements/Metadata/）

5\. 控制流节点（Public/Elements/ControlFlow/）

6\. 输入输出节点（Public/Elements/IO/）

7\. 地形相关节点（Public/Elements/Landscape/)

### 节点定义的标准结构

***典型的节点定义文件结构：***

```cpp
// Public/Elements/PCG[节点名].h

// 1. 枚举定义（如果需要）
UENUM()
enum class EPCG[节点名]Mode : uint8 { ... };

// 2. Settings类定义
UCLASS(BlueprintType, ClassGroup = (Procedural))
class UPCG[节点名]Settings : public UPCGSettings
{
    GENERATED_BODY()
    
public:
    // 节点元信息
    virtual FName GetDefaultNodeName() const override;
    virtual FText GetDefaultNodeTitle() const override;
    virtual EPCGSettingsType GetType() const override;
    
protected:
    // 引脚定义
    virtual TArray<FPCGPinProperties> InputPinProperties() const override;
    virtual TArray<FPCGPinProperties> OutputPinProperties() const override;
    
    // 创建Element
    virtual FPCGElementPtr CreateElement() const override;
    
public:
    // 可配置属性
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = Settings)
    // ... 属性定义
};

// 3. Element类定义
class FPCG[节点名]Element : public IPCGElement
{
protected:
    // 核心执行逻辑
    virtual bool ExecuteInternal(FPCGContext* Context) const override;
    
    // 可选：缓存支持
    virtual bool IsCacheable(const UPCGSettings* InSettings) const override;
    
    // 可选：依赖CRC
    virtual void GetDependenciesCrc(...) const override;
};
```

### 节点注册和发现

节点通过以下方式注册到编辑器：

1. Settings类使用 UCLASS() 宏注册
2. 编辑器扫描 UPCGSettings 的子类
3. 通过反射系统发现所有节点类型
4. 在节点面板中显示

***比如，我现在想创建一个属于我自己的节点，应该怎么创建呢？***

步骤1：创建头文件

在Source/PCG/Public/Elements/目录下创建头文件，例如PCGMyCustomNode.h：

```cpp
// Copyright Epic Games, Inc. All Rights Reserved.
#pragma once

#include "PCGSettings.h"
#include "PCGCommon.h"
#include "Data/PCGPointData.h"  // 根据需要使用

#include "PCGMyCustomNode.generated.h"

// 1. 定义枚举（如果需要）
UENUM()
enum class EPCGMyCustomNodeMode : uint8
{
    ModeA,
    ModeB,
    ModeC
};

// 2. Settings类定义
UCLASS(BlueprintType, ClassGroup = (Procedural))
class UPCGMyCustomNodeSettings : public UPCGSettings
{
    GENERATED_BODY()

public:
    UPCGMyCustomNodeSettings();

    //~Begin UObject interface
    virtual void PostLoad() override;
#if WITH_EDITOR
    virtual void PostEditChangeProperty(FPropertyChangedEvent& PropertyChangedEvent) override;
#endif
    //~End UObject interface

    //~Begin UPCGSettings interface
#if WITH_EDITOR
    // 节点元信息
    virtual FName GetDefaultNodeName() const override { 
        return FName(TEXT("MyCustomNode")); 
    }
    
    virtual FText GetDefaultNodeTitle() const override { 
        return NSLOCTEXT("PCGMyCustomNode", "NodeTitle", "My Custom Node"); 
    }
    
    virtual FText GetNodeTooltipText() const override { 
        return NSLOCTEXT("PCGMyCustomNode", "NodeTooltip", "This is my custom PCG node"); 
    }
    
    virtual EPCGSettingsType GetType() const override { 
        return EPCGSettingsType::PointOps;  // 或 Generic, Spatial, Filter等
    }
    
    virtual FLinearColor GetNodeTitleColor() const override {
        return FLinearColor(0.2f, 0.8f, 0.4f);  // 自定义颜色（可选）
    }
#endif

    // 是否使用随机种子
    virtual bool UseSeed() const override { return true; }  // 如果需要随机性

protected:
    // 定义输入引脚
    virtual TArray<FPCGPinProperties> InputPinProperties() const override {
        TArray<FPCGPinProperties> Pins;
        // 默认输入引脚（点数据）
        Pins.Emplace(
            PCGPinConstants::DefaultInputLabel,  // 引脚名称
            EPCGDataType::Point,                 // 允许的数据类型
            true,                                // 允许多个连接
            true                                 // 允许多个数据
        );
        return Pins;
    }
    
    // 定义输出引脚
    virtual TArray<FPCGPinProperties> OutputPinProperties() const override {
        return Super::DefaultPointOutputPinProperties();  // 默认点数据输出
    }
    
    // 创建Element的工厂方法（必须实现）
    virtual FPCGElementPtr CreateElement() const override;
    //~End UPCGSettings interface

public:
    // 可配置的属性
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = Settings, meta = (PCG_Overridable))
    EPCGMyCustomNodeMode ProcessingMode = EPCGMyCustomNodeMode::ModeA;
    
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = Settings, meta = (PCG_Overridable))
    float CustomParameter = 1.0f;
    
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = Settings, meta = (PCG_Overridable))
    bool bEnableFeature = true;
};

// 3. Element类定义
class FPCGMyCustomNodeElement : public IPCGElement
{
public:
    // 可选：缓存支持
    virtual bool IsCacheable(const UPCGSettings* InSettings) const override {
        return true;  // 如果输出是确定性的
    }
    
    // 可选：依赖CRC（用于缓存）
    virtual void GetDependenciesCrc(const FPCGGetDependenciesCrcParams& InParams, FPCGCrc& OutCrc) const override;

protected:
    // 核心执行逻辑（必须实现）
    virtual bool ExecuteInternal(FPCGContext* Context) const override;
    
    // 可选：执行循环模式（用于按数据缓存）
    virtual EPCGElementExecutionLoopMode ExecutionLoopMode(const UPCGSettings* Settings) const override {
        return EPCGElementExecutionLoopMode::SinglePrimaryPin;  // 或 NotALoop
    }
    
    // 可选：支持基础点数据输入
    virtual bool SupportsBasePointDataInputs(FPCGContext* InContext) const override {
        return true;
    }
};
```

步骤2：创建实现文件

在Source/PCG/Private/Elements/目录下创建实现文件，例如PCGMyCustomNode.cpp：

```cpp
// Copyright Epic Games, Inc. All Rights Reserved.

#include "Elements/PCGMyCustomNode.h"

#include "PCGContext.h"
#include "PCGPin.h"
#include "Data/PCGSpatialData.h"
#include "Data/PCGBasePointData.h"
#include "Helpers/PCGAsync.h"
#include "Helpers/PCGHelpers.h"

#include UE_INLINE_GENERATED_CPP_BY_NAME(PCGMyCustomNode)

#define LOCTEXT_NAMESPACE "PCGMyCustomNode"

// Settings构造函数
UPCGMyCustomNodeSettings::UPCGMyCustomNodeSettings()
{
    // 初始化默认值
    ProcessingMode = EPCGMyCustomNodeMode::ModeA;
    CustomParameter = 1.0f;
    bEnableFeature = true;
}

void UPCGMyCustomNodeSettings::PostLoad()
{
    Super::PostLoad();
    
    // 数据迁移逻辑（如果需要）
}

#if WITH_EDITOR
void UPCGMyCustomNodeSettings::PostEditChangeProperty(FPropertyChangedEvent& PropertyChangedEvent)
{
    Super::PostEditChangeProperty(PropertyChangedEvent);
    
    // 属性改变时的处理逻辑
    const FName PropertyName = PropertyChangedEvent.GetPropertyName();
    if (PropertyName == GET_MEMBER_NAME_CHECKED(UPCGMyCustomNodeSettings, ProcessingMode))
    {
        // 处理模式改变
    }
}
#endif

// 创建Element
FPCGElementPtr UPCGMyCustomNodeSettings::CreateElement() const
{
    return MakeShared<FPCGMyCustomNodeElement>();
}

// Element执行逻辑
bool FPCGMyCustomNodeElement::ExecuteInternal(FPCGContext* Context) const
{
    TRACE_CPUPROFILER_EVENT_SCOPE(FPCGMyCustomNodeElement::Execute);
    
    check(Context);
    
    // 1. 获取Settings
    const UPCGMyCustomNodeSettings* Settings = 
        Context->GetInputSettings<UPCGMyCustomNodeSettings>();
    check(Settings);
    
    // 2. 获取输入数据
    const TArray<FPCGTaggedData> Inputs = 
        Context->InputData.GetInputsByPin(PCGPinConstants::DefaultInputLabel);
    
    // 3. 准备输出
    TArray<FPCGTaggedData>& Outputs = Context->OutputData.TaggedData;
    
    // 4. 处理每个输入数据
    for (const FPCGTaggedData& Input : Inputs)
    {
        if (!Input.Data)
        {
            continue;
        }
        
        // 转换为点数据
        const UPCGSpatialData* SpatialData = Cast<UPCGSpatialData>(Input.Data);
        if (!SpatialData)
        {
            PCGE_LOG(Error, GraphAndLog, 
                LOCTEXT("InvalidInputType", "Input must be spatial data"));
            continue;
        }
        
        const UPCGBasePointData* PointData = SpatialData->ToBasePointData(Context);
        if (!PointData)
        {
            PCGE_LOG(Error, GraphAndLog, 
                LOCTEXT("InvalidPointData", "Unable to convert to point data"));
            continue;
        }
        
        // 5. 创建输出数据
        UPCGBasePointData* OutputPointData = 
            FPCGContext::NewPointData_AnyThread(Context);
        OutputPointData->InitializeFromData(PointData);
        
        const int32 NumPoints = PointData->GetNumPoints();
        OutputPointData->SetNumPoints(NumPoints);
        
        // 6. 处理每个点
        FPCGPointValueRanges OutputRanges(OutputPointData, /*bAllocate=*/false);
        FPCGPointValueRanges InputRanges(PointData, /*bAllocate=*/false);
        
        const int Seed = Context->GetSeed();
        FRandomStream RandomStream(Seed);
        
        for (int32 i = 0; i < NumPoints; ++i)
        {
            // 复制输入点
            OutputRanges.SetFromPoint(i, InputRanges.GetPoint(i));
            
            // 根据Settings进行自定义处理
            FPCGPoint& OutPoint = OutputRanges.GetPoint(i);
            
            switch (Settings->ProcessingMode)
            {
                case EPCGMyCustomNodeMode::ModeA:
                    // 处理模式A
                    OutPoint.Transform.SetLocation(
                        OutPoint.Transform.GetLocation() + 
                        FVector(RandomStream.FRandRange(-1.0f, 1.0f)) * Settings->CustomParameter
                    );
                    break;
                    
                case EPCGMyCustomNodeMode::ModeB:
                    // 处理模式B
                    if (Settings->bEnableFeature)
                    {
                        // 自定义逻辑
                    }
                    break;
                    
                case EPCGMyCustomNodeMode::ModeC:
                    // 处理模式C
                    break;
            }
        }
        
        // 7. 添加到输出
        FPCGTaggedData& Output = Outputs.Emplace_GetRef(Input);
        Output.Data = OutputPointData;
    }
    
    return true;  // 执行完成
}

// 依赖CRC（用于缓存）
void FPCGMyCustomNodeElement::GetDependenciesCrc(
    const FPCGGetDependenciesCrcParams& InParams, 
    FPCGCrc& OutCrc) const
{
    // 调用基类方法
    FPCGCrc Crc;
    IPCGElement::GetDependenciesCrc(InParams, Crc);
    
    // 添加Settings相关的CRC
    if (const UPCGMyCustomNodeSettings* Settings = 
        Cast<UPCGMyCustomNodeSettings>(InParams.Settings))
    {
        // 将Settings的关键属性加入CRC
        Crc.Combine(FCrc::TypeCrc32(Settings->ProcessingMode));
        Crc.Combine(FCrc::TypeCrc32(Settings->CustomParameter));
        Crc.Combine(FCrc::TypeCrc32(Settings->bEnableFeature));
    }
    
    OutCrc = Crc;
}

#undef LOCTEXT_NAMESPACE
```

步骤3：添加到构建系统

在PCG.Build.cs中添加新文件（通常会自动包含，但需确认）：

```cpp
// 通常不需要手动添加，因为使用了通配符
// Public/Elements/*.h
// Private/Elements/*.cpp
```

步骤4：本地化字符串（可选）

如果需要本地化，在Content/Localization/中添加字符串表。

步骤5：编译和测试

1. 编译项目
2. 在PCG图编辑器中查找新节点
3. 测试节点功能

## PCG支持的数据类型

### 1\. 基础数据类型枚举（EPCGDataType）

根据PCGCommon.h中的定义，PCG支持以下数据类型：

### 点数据（Point）

- EPCGDataType::Point - 点数据，PCG的核心数据类型
- 表示：UPCGPointData, UPCGBasePointData
- 用途：存储位置、变换、密度、颜色、种子等属性

### 曲线/样条数据（PolyLine/Spline）

- EPCGDataType::Spline - 样条曲线
- EPCGDataType::LandscapeSpline - 地形样条
- EPCGDataType::PolyLine - 组合类型（Spline | LandscapeSpline）
- 表示：UPCGSplineData, UPCGPolyLineData, UPCGLandscapeSplineData
- 用途：路径、道路、河流等线性特征

### 表面数据（Surface）

- EPCGDataType::Landscape - 地形数据
- EPCGDataType::Texture - 纹理数据
- EPCGDataType::RenderTarget - 渲染目标
- EPCGDataType::VirtualTexture - 虚拟纹理
- EPCGDataType::BaseTexture - 基础纹理（Texture | RenderTarget）
- EPCGDataType::Surface - 组合类型（Landscape | BaseTexture | VirtualTexture）
- 表示：UPCGLandscapeData, UPCGTextureData, UPCGRenderTargetData, UPCGVirtualTextureData
- 用途：地形采样、纹理采样、表面投影

### 体积数据（Volume）

- EPCGDataType::Volume - 体积数据
- 表示：UPCGVolumeData
- 用途：3D空间区域、碰撞体、密度场

### 图元数据（Primitive）

- EPCGDataType::Primitive - 图元数据
- 表示：UPCGPrimitiveData
- 用途：基础几何形状（盒子、球体等）

### 动态网格（DynamicMesh）

- EPCGDataType::DynamicMesh - 动态网格
- 用途：程序化生成的网格几何

### 静态网格资源（StaticMeshResource）

- EPCGDataType::StaticMeshResource - 静态网格资源
- 表示：UPCGStaticMeshResourceData
- 用途：引用静态网格资产

### 组合数据（Composite）

- EPCGDataType::Composite - 布尔运算结果
- 表示：UPCGUnionData, UPCGIntersectionData, UPCGDifferenceData
- 用途：并集、交集、差集等布尔运算

### 空间数据（Spatial）

- EPCGDataType::Spatial - 空间数据（Composite | Concrete）
- 表示：UPCGSpatialData（基类）
- 用途：所有具有空间位置的数据类型的基类

### 参数数据（Param/Attribute Set）

- EPCGDataType::Param - 属性集合
- 表示：UPCGUserParametersData
- 用途：存储元数据属性，不绑定空间位置

其他类型

- EPCGDataType::Settings - 设置数据（隐藏）
- EPCGDataType::Other - 其他类型
- EPCGDataType::ProxyForGPU - GPU代理数据（隐藏）
- EPCGDataType::Any - 任意类型（所有类型的组合）

### 2\. 数据类型层次结构

```
UPCGData (基类)
├── UPCGSpatialData (空间数据基类)
│   ├── UPCGBasePointData (点数据基类)
│   │   ├── UPCGPointData (点数据)
│   │   └── UPCGPointArrayData (点数组数据)
│   ├── UPCGPolyLineData (折线数据基类)
│   │   ├── UPCGSplineData (样条数据)
│   │   └── UPCGLandscapeSplineData (地形样条)
│   ├── UPCGSurfaceData (表面数据基类)
│   │   ├── UPCGLandscapeData (地形数据)
│   │   ├── UPCGTextureData (纹理数据)
│   │   ├── UPCGRenderTargetData (渲染目标)
│   │   └── UPCGVirtualTextureData (虚拟纹理)
│   ├── UPCGVolumeData (体积数据)
│   ├── UPCGPrimitiveData (图元数据)
│   ├── UPCGUnionData (并集)
│   ├── UPCGIntersectionData (交集)
│   ├── UPCGDifferenceData (差集)
│   └── UPCGProjectionData (投影数据)
├── UPCGUserParametersData (参数数据)
├── UPCGResourceData (资源数据基类)
│   └── UPCGStaticMeshResourceData (静态网格资源)
└── UPCGDataPtrWrapper (数据指针包装器)
```

### 3\. 数据类型操作能力

### 点数据（Point）操作

- 创建、变换、复制、过滤
- 属性操作：添加、修改、删除元数据
- 采样：从其他空间数据类型采样点
- 生成：网格、球体、表面采样等

### 空间数据（Spatial）通用操作

- 采样：SamplePoint() - 在给定位置采样点
- 投影：ProjectPoint() - 投影点到表面
- 边界：GetBounds() - 获取边界框
- 密度查询：GetDensityAtPosition() - 查询位置密度
- 转换：ToPointData() - 转换为点数据
- ToBasePointData() - 转换为基础点数据

### 表面数据（Surface）操作

- 地形采样：从Landscape采样高度、法线等
- 纹理采样：从Texture采样颜色、密度
- 表面投影：将点投影到表面
- UV坐标：计算UV坐标

### 体积数据（Volume）操作

- 体素化：将体积转换为体素
- 密度场：查询3D空间中的密度
- 边界检测：检测点是否在体积内

### 样条数据（Spline）操作

- 沿样条采样：在样条上生成点
- 距离查询：查询点到样条的距离
- 切线/法线：获取样条的方向信息

### 组合数据（Composite）操作

- 并集（Union）：合并多个空间数据
- 交集（Intersection）：计算重叠区域
- 差集（Difference）：从一个数据中减去另一个

***实际上，PCG可以具有完整资产生成能力***

几何资产

组件资产

- Spline Component（样条组件）
- Spline Mesh Component（样条网格组件）
- 任意ActorComponent子类

Actor资产

- 任意Actor类型
- 可包含任意组件组合

数据资产

特殊资产

---

大体上，我们就过完了PCG这个插件的基本架构，后面的章节会对具体的常用的节点做出详细的解释，以及算法实现的解释。

还没有人送礼物，鼓励一下作者吧

发布于 2026-01-02 19:47・上海