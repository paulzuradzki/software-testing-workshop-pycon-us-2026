"""Side quest: pytest.approx for float comparison (~5-10 min).

Optional puzzle for fast finishers. Pairs with Exercise 1.1 (the warm-up
temperature converter), where a float result is compared against an
exact value.

Spec: use `pytest.approx` to assert that two floats are equal within a
small tolerance instead of comparing them with `==`.

Teaser: why does `assert 0.1 + 0.2 == 0.3` fail?

Run from the repo root:

    uv run pytest modules/side_quests/pytest_approx/ -v

The first test below is expected to fail. That failure is the lesson.
The second test has a TODO to complete.
"""



def test_naive_float_equality_fails():
    """Demonstration: equality on floats can lie.

    A single run surfaces the failure. That is the point. The TODO
    test below uses `pytest.approx` to fix the same kind of comparison.
    """
    assert 0.1 + 0.2 == 0.3


def convert_fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


def test_freezing_point_with_approx():
    """100 F should be roughly 37.7778 C.

    Compute the result and assert it is approximately 37.7778 using
    `pytest.approx`. The tolerance should be tight enough to catch a
    bug in the formula and loose enough to ignore float noise.

    Docs: https://docs.pytest.org/en/stable/reference/reference.html#pytest-approx
    """
    result = convert_fahrenheit_to_celsius(100)
    # TODO: replace this with an assertion using pytest.approx.
    raise AssertionError("TODO: assert result is approximately 37.7778 using pytest.approx")
