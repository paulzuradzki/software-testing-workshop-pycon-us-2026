# Exercise 1.4: Targeting tests (7 min, instructor demo)

Goal: see the most useful pytest invocation patterns for selecting
WHICH tests to run. Instructor-led demo with no code to write. The
instructor will demo each form below.

## Order to read

1. `targeting_DEMO.md`. The cheat sheet with all targeting forms.
   Skim this first.
2. `test_targeting_DEMO.py`. The tests the instructor runs against.

## Forms shown during the demo

```
pytest -k <substring>                         # by name substring
pytest -m <marker>                            # by marker tag
pytest path/to/file.py::TestClass::test_name  # by exact path
pytest --lf                                   # only last-failed
pytest -x                                     # stop on first failure
pytest -v / -vv                               # verbosity
```

## If you want to practice on your own

After the demo, pick any module in this repo and try each targeting
form. There is no graded exercise for this section.
