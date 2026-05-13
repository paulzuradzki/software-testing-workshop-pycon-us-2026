"""Exercise 1.4: Run and Target Tests

Use this file to practice targeting specific tests with pytest.
See targeting_DEMO.md for a cheat sheet of invocation methods.

Exercises:
    1.4a - Run all tests in this file
    1.4b - Run only the tests inside TestShoppingCart
    1.4c - Run a single test function
    1.4d - Run tests matching a keyword pattern (e.g. "discount")
    1.4e - Run only tests tagged with a custom mark
    1.4f - Run tests with increased verbosity
"""

import pytest

# ─── Source Code ────────────────────────────────────────────


class ShoppingCart:
    """A simple shopping cart."""

    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float, qty: int = 1):
        self.items.append({"name": name, "price": price, "qty": qty})

    def remove_item(self, name: str):
        self.items = [item for item in self.items if item["name"] != name]

    @property
    def total(self) -> float:
        return sum(item["price"] * item["qty"] for item in self.items)

    @property
    def item_count(self) -> int:
        return sum(item["qty"] for item in self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0


def apply_discount(price: float, percent: float) -> float:
    """Apply a percentage discount to a price."""
    if percent < 0 or percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)


def format_receipt_line(name: str, price: float, qty: int) -> str:
    """Format a single receipt line."""
    return f"  {name:<20} {qty:>3} x ${price:<8.2f} ${price * qty:>8.2f}"


# ─── Test Class ─────────────────────────────────────────────


class TestShoppingCart:
    def test_add_item(self):
        cart = ShoppingCart()
        cart.add_item("notebook", 12.99)
        assert cart.item_count == 1

    def test_add_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item("notebook", 12.99)
        cart.add_item("pen", 1.50, qty=3)
        assert cart.item_count == 4

    def test_remove_item(self):
        cart = ShoppingCart()
        cart.add_item("notebook", 12.99)
        cart.add_item("pen", 1.50)
        cart.remove_item("notebook")
        assert cart.item_count == 1

    def test_total(self):
        cart = ShoppingCart()
        cart.add_item("notebook", 12.99, qty=2)
        cart.add_item("pen", 1.50, qty=3)
        assert cart.total == 30.48

    def test_empty_cart(self):
        cart = ShoppingCart()
        assert cart.is_empty()
        assert cart.total == 0


# ─── Test Functions ─────────────────────────────────────────


def test_apply_discount_fifty_percent():
    assert apply_discount(100.00, 50) == 50.00


def test_apply_discount_zero():
    assert apply_discount(49.99, 0) == 49.99


def test_apply_discount_full():
    assert apply_discount(49.99, 100) == 0.00


def test_apply_discount_invalid_raises():
    with pytest.raises(ValueError):
        apply_discount(100.00, -10)


def test_format_receipt_line_contains_name():
    line = format_receipt_line("notebook", 12.99, 2)
    assert "notebook" in line


def test_format_receipt_line_contains_total():
    line = format_receipt_line("notebook", 12.99, 2)
    assert "25.98" in line


# ─── Marked / Tagged Tests ─────────────────────────────────


@pytest.mark.slow
def test_bulk_cart_performance():
    """A test marked as @pytest.mark.slow for targeting with -m."""
    cart = ShoppingCart()
    for i in range(1000):
        cart.add_item(f"item_{i}", price=1.00)
    assert cart.item_count == 1000
    assert cart.total == 1000.00


@pytest.mark.slow
class TestCartStress:
    def test_add_and_remove_many(self):
        cart = ShoppingCart()
        for i in range(500):
            cart.add_item(f"item_{i}", price=2.00)
        for i in range(250):
            cart.remove_item(f"item_{i}")
        assert cart.item_count == 250
