# Exercise 2.3: Parameterized tests (12 min)

Goal: take a single test with multiple inline assertions and convert
it into a parameterized test using `@pytest.mark.parametrize`.
Parametrization gives each case its own test ID and isolates
failures.

## Order to read

1. `test_convert_c_to_f_DEMO.py`. The instructor walks through this
   first. Same shape as your starter, exercising the inverse C→F
   function so the F→C table is still yours to fill in.
2. `test_convert_f_to_c_START.py`. Your work. The docstring at the
   top has the hint and the parameter table.

## Run

```
cd modules/2.3_parameterized_tests
pytest test_convert_f_to_c_START.py -v
```

After parametrization, each tuple in your table should appear as its
own test ID in the verbose output.

## If you finish early (side quests)

- Parametrize a round-trip identity: `F → C → F` should equal the
  original input. You will need a Celsius-to-Fahrenheit function.
- Add `pytest.param(..., id="name")` to give each case a custom name
  in the output.
- Try parameterizing across two parameters at once (e.g. multiple
  conversion functions × multiple inputs).

## unittest equivalent

If you're writing `unittest`-style tests, the analogous pattern is
[`subTest`](https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests):

```python
class TestF2C(unittest.TestCase):
    def test_known_values(self):
        cases = [(32, 0), (212, 100), (-40, -40)]
        for fahrenheit, celsius in cases:
            with self.subTest(fahrenheit=fahrenheit):
                self.assertEqual(convert_f_to_c(fahrenheit), celsius)
```

Each iteration reports as its own failure. `parametrize` is the
pytest idiom; both solve the same problem.
