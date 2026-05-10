"""Solution for Exercise 1.3 (Restructure a test into AAA).

Part A: the scrambled test is now in proper AAA order.
Part B: the from-scratch test is filled in.
"""


class Cart:
    def __init__(self) -> None:
        self.items: list[float] = []

    def add_item(self, price: float) -> None:
        self.items.append(price)

    def total(self) -> float:
        return sum(self.items)


def test_cart_total_two_items():
    # Arrange
    cart = Cart()
    cart.add_item(1.50)
    cart.add_item(0.75)
    expected_total = 2.25

    # Act
    actual_total = cart.total()

    # Assert
    assert actual_total == expected_total


def test_cart_total_three_items():
    # Arrange
    cart = Cart()
    cart.add_item(10.00)
    cart.add_item(5.50)
    cart.add_item(4.50)
    expected_total = 20.00

    # Act
    actual_total = cart.total()

    # Assert
    assert actual_total == expected_total
