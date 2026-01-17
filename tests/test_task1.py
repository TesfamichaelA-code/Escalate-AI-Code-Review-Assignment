from correct_task1 import calculate_average_order_value


def test_typical():
    inp = [
        {"amount": 100, "status": "completed"},
        {"amount": 200, "status": "shipped"},
        {"amount": 50, "status": "cancelled"},
    ]
    assert calculate_average_order_value(inp) == 150.0


def test_invalid_amounts():
    inp = [
        {"amount": "100", "status": "completed"},
        {"amount": None, "status": "completed"},
        {"amount": "abc", "status": "completed"},
    ]
    assert calculate_average_order_value(inp) == 100.0


def test_non_dicts():
    inp = [
        {"amount": 10, "status": "completed"},
        "notadict",
        {"amount": 20, "status": "completed"},
    ]
    assert calculate_average_order_value(inp) == 15.0


def test_all_cancelled():
    inp = [
        {"amount": 10, "status": "cancelled"},
        {"amount": 20, "status": "cancelled"},
    ]
    assert calculate_average_order_value(inp) == 0


def test_empty():
    assert calculate_average_order_value([]) == 0


def test_mixed():
    inp = [
        {"amount": 10, "status": "completed"},
        {},
        {"amount": 5, "status": "cancelled"},
        {"amount": "5.5", "status": "processing"},
    ]
    assert abs(calculate_average_order_value(inp) - 7.75) < 1e-9
