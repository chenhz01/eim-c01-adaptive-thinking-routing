# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P01 no-think-draft-agreement-router — 自适应思考路由

L0: AI 有时不用细想也能答对。这个工具帮它先给个快速草稿，草稿够确定就跳过深度思考，省电省钱。
L1: 用草稿一致性分数做路由：先取若干快速草稿，若多数草稿相互一致(agreement>=阈值)则 skip_think，否则 think。
L2: route(drafts) 返回 'skip_think'/'think'，把它接在推理循环最前面即可。
"""

def agreement(drafts):
    """drafts: list[str] 快速草稿。返回最大簇占比。"""
    if not drafts: return 0.0
    # 用首 12 字符做粗糙归并（参考实现，真实场景换语义相似度）
    keys = [d.strip()[:12].lower() for d in drafts]
    from collections import Counter
    top = Counter(keys).most_common(1)[0][1]
    return top / len(keys)

def route(drafts, threshold=0.75):
    a = agreement(drafts)
    return ("skip_think" if a >= threshold else "think"), round(a, 3)

def demo():
    print("[P01] agree-high:", route(["42", "42", "42", "41"]))
    print("[P01] agree-low :", route(["42", "blue", "17", "cat"]))


if __name__ == "__main__":
    demo()
