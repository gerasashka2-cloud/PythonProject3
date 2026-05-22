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


@pytest.fixture
def transactions():
    return [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 123456789,
        "state": "EXECUTED",
        "date": "2020-01-01T12:00:00.000000",
        "operationAmount": {
            "amount": "1000.00",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Счет 12345678901234567890",
        "to": "Счет 09876543210987654321"
    },
    {
        "id": 654321098,
        "state": "EXECUTED",
        "date": "2020-02-15T10:00:00.000000",
        "operationAmount": {
            "amount": "5000.00",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 12345678901234567890",
        "to": "Счет 09876543210987654321"
    }
]