# C01 · Adaptive Thinking Routing

> **机制簇**：自适应思考路由 ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：4
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
让 AI 别每次都「想很久」。简单问题直接答，难问题才深想——又快又省钱。

**L1 · 机制本质**
按难度/置信度动态分配推理预算：先出低成本草稿，若与高成本答案一致则直通（draft-agreement），否则升级到深思路径。

**L2 · 怎么用上**
Router 决定 think / no-think；预算分配器切 token；置信闸决定是否升级。三件可独立替换。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c01-adaptive-thinking-routing.git && cd eim-c01-adaptive-thinking-routing
python run_all.py        # 跑全簇 4 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p01-no-think-draft-agreement-router/impl.py        # 看 demo 输出
python components/p01-no-think-draft-agreement-router/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P01` | no-think-draft-agreement-router | 用草稿一致性分数做路由：先取若干快速草稿，若多数草稿相互一致(agreement>=阈值)则 skip_think，否则 think。 | `components/p01-no-think-draft-agreement-router/` |
| `P02` | token-budget-thought-allocator | 按每步不确定性归一化后分配思考预算：uncertainty 越大分配越多 token，总量守恒。 | `components/p02-token-budget-thought-allocator/` |
| `P03` | confidence-gated-reasoning-switcher | 置信度门控：confidence>=hi 用 fast；<=lo 用 slow；中间用 medium。 | `components/p03-confidence-gated-reasoning-switcher/` |
| `P04` | cot-compression-router | 保留首步、末步与信息密度最高的 k 步，其余丢弃，按比例压缩 CoT。 | `components/p04-cot-compression-router/` |

### 深度文档状态（v1.1.0，四件已全部升级）

本簇四个组件的 README 已全部升级到 **2 万字以上**的深度文档，
每个组件都附带一个可复跑的基准脚本，文档中所有结论性数字都可由该脚本复现。
**四个组件的 headline 结论全部是负面结论，并且都写在正文而非附录里**——
这是本家族的评测协议要求的：没有负对照的性能声称不算证据。

| ID | 深度文档字数 | headline 结论（负面，已写在正文） | 独立仓 |
|---|---|---|---|
| `P01` | 21,446 | 一致性分数在多数配置下弱于「直接深思」的朴素基线 | `eim-p01-no-think-draft-agreement-router` |
| `P02` | 21,742 | 饱和收益下按难度比例分配 **4.006**，输给均匀的 4.621（−13.3%）；理论最优给最难一步 **0** 预算 | `eim-p02-token-budget-thought-allocator` |
| `P03` | 24,295 | 把置信度换成随机数后机制仍花掉 **66.6%** 的成本；坏信号比不用信号贵 **149%** | `eim-p03-confidence-gated-reasoning-switcher` |
| `P04` | 23,472 | 当长度与重要性无关时 **0.437**，输给随机抽样的 0.508，且花得更多 | `eim-p04-cot-compression-router` |

共享的三条判据（四份文档各自独立地收敛到同一组结论）：

1. **零信息基线是必查项。** 把输入信号换成随机数再跑一次；
   若机制仍能给出体面的读数，那么体面的读数就不能证明它有输入信息。
   P03 测得结构占 66.6%，P04 测得有偏抽样会输给无偏抽样。
2. **公平口径才可比。** 先锁定质量目标再比成本。
   P02 与 P03 都因此发现：收益主要由任务分布决定，与机制的精巧程度关系不大。
3. **静默失败比性能损失更贵。** 四个组件合计抓出 6 处静默行为：
   P03 的 `pick(nan)` 走中档、P04 的非幂等与 `keep_ratio` 两端不兑现、
   P02 的 floor 破预算。它们都不抛异常、不告警，只在事后才被发现。

## 该用 / 不该用 / 常见误用

**该用**
有成本压力、问题难度分布宽（客服分流、批量抽取、混合工作负载）；要求 p95 延迟可控。

**不该用**
问题几乎全难（一次深想比两段更省）；对错误零容忍且没有可兜底的验证器。

**常见误用（这条最重要）**
把「草稿与深思一致」当成「答案正确」。一致性只是低成本信号，不是正确性证明。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C01 · Adaptive Thinking Routing © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
