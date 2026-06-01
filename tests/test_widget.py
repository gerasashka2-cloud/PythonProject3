import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    """ Функция тестирования ввода сценариев функции mask_account_card """
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert mask_account_card("Счет 35383033474447898560") == "Счет **8560"
    assert mask_account_card("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"
    assert mask_account_card("Maestro 1234567890123456") == "Maestro 1234 56** **** 3456"
    assert mask_account_card("Unknown format") == "Неизвестный формат"
    assert mask_account_card("Счет 12345") == "Номер счета должен содержать 20 цифр"


def test_get_date():
    """ Функция тестирования ввода сценариев функции get_date """
    assert get_date("2024-03-11T02:26:18.671407") == "2024-03-11"
    assert get_date("2024-03-11T02:26:18.671407") == "2024-03-11"
    assert get_date("2024-03-11T02:26:18.671407") == "2024-03-11"
    assert get_date("2024-03-11T02:26:18.671407") == "2024-03-11"
    with pytest.raises(ValueError):
        get_date("")
        