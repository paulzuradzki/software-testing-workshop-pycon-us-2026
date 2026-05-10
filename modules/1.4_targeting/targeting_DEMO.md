# Exercise 1.4: Run and Target Tests

A cheat sheet for the most common ways to run specific tests with **pytest**.

The module examples assume the working directory is `modules/1.4_targeting/`.

---

## 1.4a: Target a File

Run every test in a single file:

```bash
pytest test_targeting_START.py
```

> **Tip:** pytest auto-discovers files matching `test_*.py` or `*_test.py`.
> Running `pytest` with no arguments collects from the current directory (recursively).

---

## 1.4b: Target a Class

Run only the tests inside a specific test class:

```bash
pytest test_targeting_START.py::TestShoppingCart
```

The `::` separator is called **node id** syntax. It lets you drill into a file.

---

## 1.4c: Target a Function

Run a single standalone test function:

```bash
pytest test_targeting_START.py::test_apply_discount_fifty_percent
```

Run a single method inside a class:

```bash
pytest test_targeting_START.py::TestShoppingCart::test_total
```

---

## 1.4d: Target by Keyword Pattern (`-k`)

`-k` matches against test names using a Python expression:

```bash
# all tests with "discount" in the name
pytest test_targeting_START.py -k "discount"

# discount tests, but NOT the one that raises
pytest test_targeting_START.py -k "discount and not invalid"

# only receipt-related tests
pytest test_targeting_START.py -k "receipt"

# tests in a class OR containing "format"
pytest test_targeting_START.py -k "ShoppingCart or format"
```

> **Key idea:** `-k` matches against the *full node id* so it works on
> function names, class names, and even file path components.

---

## 1.4e: Target by Mark / Tag (`-m`)

Marks are pytest's tagging system. Look in the test file for `@pytest.mark.slow`.

```bash
# only tests marked as slow
pytest test_targeting_START.py -m slow

# everything EXCEPT slow tests
pytest test_targeting_START.py -m "not slow"
```

### Registering Custom Marks

To avoid warnings, register your marks in `pyproject.toml` or `pytest.ini`:

```toml
# pyproject.toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
]
```

---

## 1.4f: Verbosity

```bash
# normal (default): dots for pass, F for fail
pytest test_targeting_START.py

# verbose: one line per test with PASSED/FAILED
pytest test_targeting_START.py -v

# extra verbose: shows full assertion diffs
pytest test_targeting_START.py -vv

# quiet: minimal output
pytest test_targeting_START.py -q
```

---

## Combining Options

All of these flags compose freely:

```bash
# verbose + keyword filter
pytest test_targeting_START.py -k "cart" -v

# mark filter + extra verbose
pytest test_targeting_START.py -m slow -vv

# quiet + stop on first failure
pytest test_targeting_START.py -q -x

# show the full node ids that would run (dry run)
pytest test_targeting_START.py --collect-only
```

---

## Quick Reference Table

| Goal                        | Command                                           |
| --------------------------- | ------------------------------------------------- |
| Run a file                  | `pytest test_file.py`                             |
| Run a class                 | `pytest test_file.py::TestClass`                  |
| Run a function              | `pytest test_file.py::test_func`                  |
| Run a method                | `pytest test_file.py::TestClass::test_method`     |
| Match a keyword             | `pytest -k "keyword"`                             |
| Keyword AND                 | `pytest -k "keyword1 and keyword2"`               |
| Keyword OR                  | `pytest -k "keyword1 or keyword2"`                |
| Keyword NOT                 | `pytest -k "not keyword"`                         |
| Run by mark                 | `pytest -m mark_name`                             |
| Exclude a mark              | `pytest -m "not mark_name"`                       |
| Verbose                     | `pytest -v`                                       |
| Extra verbose               | `pytest -vv`                                      |
| Quiet                       | `pytest -q`                                       |
| Stop at first failure       | `pytest -x`                                       |
| Dry run (collect only)      | `pytest --collect-only`                            |
