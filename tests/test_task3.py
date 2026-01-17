from correct_task3 import average_valid_measurements


def test_typical():
    assert abs(average_valid_measurements([1, 2, 3, None, 4]) - 2.5) < 1e-9


def test_strings_and_floats():
    assert abs(average_valid_measurements(["1.5", 2, "3.5", None]) - ((1.5+2+3.5)/3)) < 1e-9


def test_non_numeric():
    assert average_valid_measurements([None, "a", {}, []]) == 0


def test_empty():
    assert average_valid_measurements([]) == 0


def test_negatives():
    assert abs(average_valid_measurements([-1, -2, -3, None]) + 2.0) < 1e-9
