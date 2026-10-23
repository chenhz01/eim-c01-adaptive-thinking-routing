# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P04 cot-compression-router — 自适应思考路由

L0: AI 思考过程很长，传给下一步时又长又费钱。这个工具把中间思考压短，只留关键的。
L1: 保留首步、末步与信息密度最高的 k 步，其余丢弃，按比例压缩 CoT。
L2: compress(steps, keep_ratio) 返回压缩后的步骤列表。
"""

def compress(steps, keep_ratio=0.5):
    if len(steps) <= 2: return list(steps)
    keep = max(2, int(len(steps) * keep_ratio))
    ranked = sorted(range(len(steps)), key=lambda i: len(steps[i]), reverse=True)[:keep-2]
    idx = sorted(set([0, len(steps)-1] + ranked))
    return [steps[i] for i in idx]

def demo():
    s = ["理解题意", "设变量", "列方程", "求解", "检验"]
    print("[P04]", compress(s, 0.6))


if __name__ == "__main__":
    demo()
