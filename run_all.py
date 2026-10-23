# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""run_all.py — 跑本簇全部组件：逐个执行 selftest.py，全过才算 PASS。

设计要点：子进程隔离（一个组件崩不影响其余）、失败即摘录输出、退出码可被 CI 直接消费。
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    comp = os.path.join(HERE, "components")
    if not os.path.isdir(comp):
        print("[run_all] 缺少 components/ 目录"); return 1
    dirs = sorted(d for d in os.listdir(comp) if os.path.isdir(os.path.join(comp, d)))
    if not dirs:
        print("[run_all] components/ 为空"); return 1
    fails = []
    for d in dirs:
        st = os.path.join(comp, d, "selftest.py")
        if not os.path.exists(st):
            print("FAIL " + d + "  (缺 selftest.py)"); fails.append(d); continue
        r = subprocess.run([sys.executable, st], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=120)
        ok = r.returncode == 0
        print(("PASS " if ok else "FAIL ") + d)
        if not ok:
            fails.append(d)
            tail = ((r.stdout or "") + (r.stderr or "")).strip().splitlines()[-4:]
            for line in tail:
                print("     " + line[:200])
    print("[run_all] %d/%d passed" % (len(dirs) - len(fails), len(dirs)))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
