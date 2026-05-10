# Exercise 1.2: unittest vs pytest (10 min)

Goal: see the same tests written in both `unittest` (standard
library) and `pytest` style. Run each runner against the same file
and compare what gets discovered.

## Order to read

1. `convert_f_to_c_START.py`. Read the docstring at the top, then
   skim both forms of the test. No code to write.

## Run

```
cd modules/1.2_unittest_and_pytest

# unittest:
python -m unittest convert_f_to_c_START.py

# pytest:
pytest convert_f_to_c_START.py -v
```

Prefix either command with `uv run` if your venv is not activated.

## What to notice

- `unittest` reports 1 test. It only discovers the `TestCase` class.
- `pytest` reports 2 tests. It discovers the function AND the class.

## If you finish early (side quests)

- Add a second test (one function-style, one class-style). Confirm
  pytest finds both but unittest finds only the class one.
- Try `pytest --collect-only` to see what pytest would run without
  running anything.
