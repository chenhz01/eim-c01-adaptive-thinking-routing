# P02 · token-budget-thought-allocator

> 机制簇：**自适应思考路由** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
一道题里，有的步骤很难、有的很简单。这个工具把'想多久'的额度按难度分给每一步，难的多想、简单的少想。

**L1 · 机制本质**
按每步不确定性归一化后分配思考预算：uncertainty 越大分配越多 token，总量守恒。

**L2 · 怎么用上**
allocate(uncertainties, total_budget) 返回每步预算列表；配合你的生成器逐段限额。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P02] budgets: [529, 58, 294, 117]
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 批量/多轮推理、成本敏感、延迟可调的 agent 循环（先草稿再决定是否深想）。 |
| **不该用** | 答案唯一且必须精确的算术/取数场景；硬实时不允许二次调用的链路。 |
| **常见误用** | 把「多份草稿一致」当成「答案正确」——一致只说明模型自信，不说明它对。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P01` no-think-draft-agreement-router · `P03` confidence-gated-reasoning-switcher · `P04` cot-compression-router
- 本仓是 **P02 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P02-token-budget-thought-allocator/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P02 · token-budget-thought-allocator © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](NOTICE)。
