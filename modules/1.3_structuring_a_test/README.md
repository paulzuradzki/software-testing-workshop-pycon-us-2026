# Exercise 1.3: Restructure to AAA (8 min)

Goal: take a scrambled test and reorganize it under Arrange / Act /
Assert sections, then write a fresh AAA test from scratch. The
structure makes the intent of each line obvious and makes failures
easier to read on test #500.

## Order to read

1. `AAA_DEMO.py`. The instructor walks through a clean AAA test on a
   profit calculator.
2. `test_aaa_START.py`. Your work, in two short parts:
   - **Part A:** re-order a scrambled test into clean AAA blocks.
     The behavior is right; only the layout is wrong.
   - **Part B:** write a fresh AAA test from scratch using the same
     layout.

## Run

```
cd modules/1.3_structuring_a_test
pytest test_aaa_START.py -v
```

You'll see Part A's test pass (it's correct, just messy) and Part B's
test fail loudly until you fill it in.

## If you finish early (side quests)

- Add a third test that exercises an **empty** cart. What should
  `Cart.total()` return when no items have been added? Pick the
  behavior you want and pin it down with a test.
- Pair up: have a peer scramble one of your AAA tests, then re-order
  it back. Notice how much harder it is to read in scrambled form.
