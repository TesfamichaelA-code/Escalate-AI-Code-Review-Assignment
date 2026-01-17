from correct_task2 import count_valid_emails


def test_typical():
    inp = [
        "alice@example.com",
        "bob.smith@sub.example.co.uk",
        "carol+tag@gmail.com",
        "invalid@",
        "@nope",
    ]
    assert count_valid_emails(inp) == 3


def test_non_strings():
    inp = ["dave@example.com", None, 123, {"email": "e@example.com"}]
    assert count_valid_emails(inp) == 1


def test_whitespace():
    inp = ["  frank@example.com  ", "george@example.com"]
    assert count_valid_emails(inp) == 2


def test_empty():
    assert count_valid_emails([]) == 0


def test_mixed_invalid():
    inp = ["good+1@test.io", "bad@@test.com", "no-domain@test", "also.good@test-domain.org"]
    assert count_valid_emails(inp) == 2
