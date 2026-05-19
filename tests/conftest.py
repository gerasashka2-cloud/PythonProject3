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
def valid_account_number():
    return [
        "12345678901234567890",

    ]


@pytest.fixture
def data():
    return [
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def invalid_data():
    return [
        {'date': 'invalid-data-format'},
    ]


@pytest.fixture
def invalid_input():
    return [
        None,
        "not a number",
    ]