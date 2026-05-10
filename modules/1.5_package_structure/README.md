# Exercise 1.5: Package Structure (10 min)

Goal: install this exercise as an editable package using `uv pip
install -e .` and run pytest against it. Real Python projects use
this layout: code under `src/`, tests under `test/`, and
`pyproject.toml` declaring the package.

## Order to read

1. `pyproject.toml`. Declares the `converter` package.
2. `src/converter/`. The package source.
3. `test/`. The pytest tests that import from `converter`.

## Run

From this folder:

```
cd modules/1.5_package_structure
uv pip install -e .
pytest -q
```

The `-e .` (editable) install adds `converter` to your venv's
`sys.path` so `from converter.convert_temp import ...` resolves.

## If you finish early (side quests)

- Add a second test file under `test/` and confirm pytest discovers
  it without any config changes.
- Add a new function to `src/converter/` (e.g. kelvin_to_celsius)
  with its own test.
- Remove `__init__.py` and watch the import break.

## Troubleshooting

### `ModuleNotFoundError: No module named 'converter'`

This error means Python can't find the `converter` package when running tests. There are three common causes:

**1. Missing `__init__.py`**

The `src/converter/` directory needs an `__init__.py` file for Python to recognize it as a package. Without it, `import converter` won't work even if the files are there.

```
src/
  converter/
    __init__.py          <-- required
    convert_temp.py
    convert_weight.py
```

See: [Python Packages docs](https://docs.python.org/3/tutorial/modules.html#packages)

**2. Incorrect `packages` in `pyproject.toml`**

With the `src` layout, the hatch build config must point into `src/`:

```toml
# Wrong - would require `from src.converter import ...`
packages = ["src"]

# Correct - makes `converter` the top-level import name
packages = ["src/converter"]
```

See: [Hatch build config: packages](https://hatch.pypa.io/latest/config/build/#packages)

**3. Package not installed in the environment**

The `src` layout deliberately keeps your code off `sys.path`, so you must install the package (in editable mode for development) before tests can import it:

```bash
uv pip install -e .
```

After this, `from converter.convert_temp import ...` resolves. You only need to do this once per environment. Editable installs pick up code changes.
