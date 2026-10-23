# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P02 token-budget-thought-allocator — 自适应思考路由

L0: 一道题里，有的步骤很难、有的很简单。这个工具把'想多久'的额度按难度分给每一步，难的多想、简单的少想。
L1: 按每步不确定性归一化后分配思考预算：uncertainty 越大分配越多 token，总量守恒。
L2: allocate(uncertainties, total_budget) 返回每步预算列表；配合你的生成器逐段限额。
"""

def allocate(uncertainties, total_budget=1000, floor=50):
    """按不确定性比例分配预算，每步至少 floor。"""
    if not uncertainties: return []
    s = sum(uncertainties) or 1.0
    return [max(floor, int(total_budget * u / s)) for u in uncertainties]

def demo():
    print("[P02] budgets:", allocate([0.9, 0.1, 0.5, 0.2], 1000))


if __name__ == "__main__":
    demo()
