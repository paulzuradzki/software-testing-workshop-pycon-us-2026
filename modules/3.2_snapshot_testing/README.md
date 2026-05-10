# Exercise 3.2: Snapshot Testing

Hands-on for Part 3 closer.

`compute_invoice` is a branchy function you don't fully understand.
Snapshot test it: capture today's outputs, lock them in, then any
future change that drifts the output fails loudly.

```
# 1. Capture current behavior:
python modules/3.2_snapshot_testing/test_snapshot_START.py

# 2. Paste the printed lines into EXPECTED.
# 3. Run the tests:
pytest modules/3.2_snapshot_testing -q
```

Files:

- `gnarly.py` (read-only). The function under test.
- `test_snapshot_START.py` (your worksheet).

Pointer for the real library: [approvaltests](https://github.com/approvals/ApprovalTests.Python)
on PyPI. We're rolling our own here so the mechanism is visible.
