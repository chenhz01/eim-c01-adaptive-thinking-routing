# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P03 confidence-gated-reasoning-switcher — 自适应思考路由

L0: 信心高就用快模型，信心低才换慢而准的模型。省钱又不掉质量。
L1: 置信度门控：confidence>=hi 用 fast；<=lo 用 slow；中间用 medium。
L2: pick(confidence) 返回模型档位，接在你的模型路由处。
"""

def pick(confidence, hi=0.8, lo=0.4):
    if confidence >= hi: return "fast"
    if confidence <= lo: return "slow"
    return "medium"

def demo():
    print("[P03]", [pick(c) for c in (0.95, 0.6, 0.2)])


if __name__ == "__main__":
    demo()
