"""AAA_DEMO.py

The filename does not start with "test_", so pytest skips it during
auto-discovery. Pass the path to run it.

Works (explicit path):
    $ pytest AAA_DEMO.py
    # or:  uv run pytest AAA_DEMO.py

Skipped under auto-discovery:
    $ pytest
    # or:  uv run pytest

Auto-discovery picks up `test_aaa_START.py` because the filename
starts with `test_`. AAA_DEMO.py is left out.
"""


class ProfitReport:
    """Profit calculator."""

    def __init__(self, sales_data: list[dict], cost_data: list[dict]):
        self.sales_data = sales_data
        self.cost_data = cost_data

    def calculate_profit(self):
        total_sales = 0
        total_cost = 0
        sold_items = set()
        for sale in self.sales_data:
            total_sales += sale["unit_price"] * sale["qty"]
            sold_items.add(sale["item"])
        for cost in self.cost_data:
            if cost["item"] in sold_items:
                total_cost += cost["unit_cost"] * sale["qty"]

        return total_sales - total_cost

    def display_report(self):
        print(f"Net profit is: {self.calculate_profit()}")


def main():
    sales = [{"item": "foo", "unit_price": 7, "qty": 2}]
    costs = [
        {"item": "foo", "unit_cost": 5},
        {"item": "bar", "unit_cost": 3},
    ]
    report = ProfitReport(sales, costs)
    report.display_report()


def test_ProfitReport_calculate_profit():
    # Arrange
    sales = [{"item": "foo", "unit_price": 7, "qty": 2}]
    costs = [
        {"item": "foo", "unit_cost": 5},
        {"item": "bar", "unit_cost": 3},
    ]
    report = ProfitReport(sales, costs)
    expected_profit = 4

    # Act
    result_profit = report.calculate_profit()

    # Assert
    assert result_profit == expected_profit, (
        f"Expected profit: {expected_profit}. Received: {result_profit}"
    )


if __name__ == "__main__":
    main()
