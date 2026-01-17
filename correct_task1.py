def calculate_average_order_value(orders):
    """Return the average `amount` for orders that are not cancelled.

    Rules:
    - Ignore orders with status == "cancelled".
    - Skip orders with missing or non-numeric `amount` values.
    - If there are no valid (non-cancelled and numeric) orders, return 0.
    - Raise TypeError if `orders` is not a list.
    """
    if not isinstance(orders, list):
        raise TypeError("orders must be a list of order dicts")

    total = 0.0
    count = 0

    for order in orders:
        if not isinstance(order, dict):
            continue
        if order.get("status") == "cancelled":
            continue
        amount = order.get("amount")
        try:
            total += float(amount)
            count += 1
        except (TypeError, ValueError):
            continue

    if count == 0:
        return 0

    return total / count
