# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""selftest: demo 可跑 + 输出含组件标识 + 与 golden_output.txt 快照一致。"""
import io, os, sys, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import impl

CID = "P02"

def main():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        impl.demo()
    out = buf.getvalue()
    assert out.strip(), "demo 无输出"
    assert ("[" + CID + "]") in out, "输出未含组件标识 " + CID
    gp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "golden_output.txt")
    if os.path.exists(gp):
        golden = open(gp, encoding="utf-8").read()
        assert out == golden, "输出与快照不一致（行为漂移）"
    print("[selftest] PASS " + CID + " (" + str(len(out)) + " bytes)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
