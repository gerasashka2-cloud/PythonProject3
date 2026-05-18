import pytest


@pytest.fixture
def valid_card_numbers():
    return [
        "1234567812345678",
    ]


@pytest.fixture
def invalid_card_numbers():
    return [
        "1234567",
        "12345678123451234",
        "",
        12345,
    ]


@pytest.fixture
def invalid_input_card_numbers():
    return [
        None,
        "not a valid number",
    ]


@pytest.fixture
def valid_account_number():
    return [
        "12345678901234567890"
    ]


