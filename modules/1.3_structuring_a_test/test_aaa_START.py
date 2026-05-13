"""Exercise 1.3: Restructure a test into Arrange-Act-Assert.

Two short parts. The function under test is small so the focus stays
on test structure rather than cart logic.

Run from the repo root:

    pytest modules/1.3_structuring_a_test/test_aaa_START.py -v

- Part A: re-order the scrambled test below into clean AAA blocks.
  The behavior is correct; only the layout is wrong. The test passes
  scrambled, and it should still pass once the order is fixed.
- Part B: write a fresh AAA test from scratch using the same layout.

The same AAA shape shows up in the ToDoTracker tests in 2.1+.
"""


class Cart:
    def __init__(self) -> None:
        self.items: list[float] = []

    def add_item(self, price: float) -> None:
        self.items.append(price)

    def total(self) -> float:
        return sum(self.items)


# ---------- Part A: re-order into Arrange / Act / Assert blocks -------------
#
# This test passes today, but the steps are interleaved. Move the lines
# so the test reads top-to-bottom as:
#
#     # Arrange   (set up inputs and the expected result)
#     # Act       (one call to the code under test)
#     # Assert    (one or more assertions on the result)
#
# Do not change values; only re-order. Drop the "_is_scrambled" suffix
# from the function name once the layout is settled.


def test_cart_total_two_items_is_scrambled():
    cart = Cart()
    cart.add_item(1.50)
    expected_total = 2.25
    cart.add_item(0.75)
    actual_total = cart.total()
    assert actual_total == expected_total


# ---------- Part B: write this test from scratch ----------------------------
#
# Add 10.00, 5.50, and 4.50 to a Cart, then assert the total is 20.00.
# Use the same Arrange / Act / Assert layout from Part A.


def test_cart_total_three_items():
    # Arrange
    # TODO: build a Cart, add 10.00, 5.50, 4.50; set expected_total = 20.00

    # Act
    # TODO: call cart.total() and capture the result in actual_total

    # Assert
    # TODO: assert actual_total == expected_total
    raise AssertionError("TODO: implement the AAA test for a 3-item cart")
