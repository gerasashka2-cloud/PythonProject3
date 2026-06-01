import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тестирование правильности маскирования номера карты.
@pytest.mark.parametrize("expected",[
        "1234 56** **** 5678",
])
def test_get_mask_card_number_masking(valid_card_numbers, expected):
    for card_number in valid_card_numbers:
        assert get_mask_card_number(card_number) == expected


# Проверка выброса исключений для номера карты неправильной длины.
@pytest.mark.parametrize("expected_exception", [ValueError])
def test_get_mask_card_number_invalid_length(invalid_card_numbers, expected_exception):
    for card_number in invalid_card_numbers:
        with pytest.raises(expected_exception, match="Номер карты должен быть 16 цифр"):
            get_mask_card_number(card_number)


# Проверка некорректного ввода
@pytest.mark.parametrize("expected_exception", [ValueError])
def test_get_mask_card_number_invalid_input(invalid_input, expected_exception):
    for card_number in invalid_input:
        with pytest.raises(expected_exception,):
            get_mask_card_number(card_number)


# Тест на возврат маски номера счета.
def test_get_mask_account_number(valid_account_number):
    account_number = valid_account_number[0]
    mask = get_mask_account(account_number)
    assert mask == "**7890"


# Проверка обработки некорректных данных.
def test_get_mask_account_number_invalid_account_number():
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр"):
        get_mask_account("124")
