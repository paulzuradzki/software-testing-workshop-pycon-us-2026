"""A function with branchy logic. Full understanding is not required.

That is the point of snapshot testing.

Pricing rules:

- Tier discount: silver 5%, gold 10%, platinum 15%.
- Bulk discount: 20+ items adds 5%.
- Coupon NEW10: extra 10% off, but only on subtotals over $50.
- Tax: 8.875% on the post-discount subtotal,
  except silver/gold/platinum customers are tax-exempt below $25.
"""

from __future__ import annotations


def main():
    # This is just one manual test example
    # How do we cover compute invoice with tests so we can update it more safely?
    invoice_data = {
        "quantity": 100,
        "price": 10,
        "customer_type": "silver",
        "coupon_code": None,
    }

    result = compute_invoice(*invoice_data.values())
    print(result)  # 979.88


def compute_invoice(quantity, price, customer_type, coupon_code=None):
    subtotal = quantity * price

    tier = {"silver": 0.05, "gold": 0.10, "platinum": 0.15}.get(customer_type, 0)
    if quantity >= 20:
        tier += 0.05
    discount = subtotal * tier

    sub_after = subtotal - discount

    if coupon_code == "NEW10" and sub_after > 50:
        sub_after *= 0.90

    if customer_type in {"silver", "gold", "platinum"} and sub_after < 25:
        tax = 0
    else:
        tax = sub_after * 0.08875

    return round(sub_after + tax, 2)


if __name__ == "__main__":
    main()
