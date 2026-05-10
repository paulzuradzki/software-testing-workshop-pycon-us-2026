"""Side quest: TDD red-green-refactor on FizzBuzz (~10-15 min).

Optional puzzle for fast finishers. The goal is the rhythm of the cycle.

Spec for `fizzbuzz(n)`:
- Returns "Fizz" when n is divisible by 3.
- Returns "Buzz" when n is divisible by 5.
- Returns "FizzBuzz" when n is divisible by both 3 and 5.
- Returns the number as a string otherwise.
- n is a positive integer.

Red-green-refactor:
1. Red. Write one failing test for the smallest missing behavior.
2. Green. Write the least code that makes it pass. Hard-coding is allowed.
3. Refactor. Clean up duplication once the bar is green.
Then loop. Add the next failing test and repeat.

Run with: pytest modules/side_quests/tdd_cycle/ -v

Resist writing the full implementation up front. Take small bites.
"""


def fizzbuzz(n):
    # TODO: implement one rule at a time, driven by the next failing test.
    ...


def test_first_red():
    # Force this assertion to fail on purpose. That is the red bar.
    # Then change `fizzbuzz` enough to turn it green.
    assert fizzbuzz(1) == "1"


# Add the next failing test below. Suggested order of attack:
#   - one rule at a time
#   - simplest input that exercises the rule
#   - do not anticipate later rules in earlier code
#
# After each green bar, look for duplication and refactor before adding
# the next test. The discipline is the lesson.
