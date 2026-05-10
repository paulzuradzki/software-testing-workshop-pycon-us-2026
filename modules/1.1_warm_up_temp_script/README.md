# Exercise 1.1: Fahrenheit to Celsius warm-up (8 min)

Goal: write your first pytest assertion. Translate the formula
`C = (F - 32) * 5/9` into a test that would catch a wrong
implementation.

## Order to read

1. `convert_c_to_f_DEMO.py`. The instructor walks through this first.
   It shows what a tested Celsius-to-Fahrenheit function looks like
   when complete.
2. `convert_f_to_c_START.py`. Your work. The function is already
   implemented. Replace the `NotImplementedError` with real
   assertions on at least 2-3 input/output pairs.

## Run

```
cd modules/1.1_warm_up_temp_script
pytest convert_f_to_c_START.py -v
```

## If you finish early (side quests)

- Add tests for negative temperatures and the freezing point (32°F →
  0°C, -40°F → -40°C, 0°F → ~-17.78°C).
- Break a working assertion on purpose (e.g. expect `100` instead of
  `37.78` for `100°F`). Run pytest, read the failure, then fix it.
  Failure messages are part of the value of a test. Get used to
  reading them early.

A `pytest.approx` side quest pairs with this exercise once we have
introduced pytest in 1.2; see `modules/side_quests/pytest_approx/`
after Part 1.
