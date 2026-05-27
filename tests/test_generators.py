import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Проверка фильтрации по валюте USD
def test_filter_by_currency(transactions):
    # Проверка фильтрации по валюте USD
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]["id"] == 939719570
    assert usd_transactions[1]["id"] == 142264268

    # Проверка фильтрации по отсутствующей валюте
    eur_transactions = list(filter_by_currency(transactions, "JPY"))
    assert len(eur_transactions) == 0

    # Проверка фильтрации по валюте RUB
    rub_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transactions) == 1
    assert rub_transactions[0]["id"] == 654321098

    # Проверка обработки пустого списка
    empty_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0


def test_transaction_descriptions(transactions):
    # Получаем генератор описаний транзакций
    descriptions = transaction_descriptions(transactions)
    # Преобразуем генератор в список
    descriptions_list = list(descriptions)
    # Проверяем, что второе описание соответствует ожидаемому
    assert descriptions_list[1] == "Перевод со счета на счет"
    assert descriptions_list[2] == "Перевод с карты на карту"

    # Теперь проверим, сколько раз встречается описание "Перевод организации"
    descriptions_list_2 = list(transaction_descriptions(transactions))
    organization_descriptions = [desc for desc in descriptions_list_2 if desc == "Перевод организации"]
    assert len(organization_descriptions) == 2

    # Проверяем, что идентификаторы транзакций с описанием "Перевод организации" соответствуют ожидаемым
    ids = [trans["id"] for trans in transactions if trans["description"] == "Перевод организации"]
    assert ids[0] == 939719570
    assert ids[1] == 654321098

    # Проверка работы с пустым списком
    empty_transactions = []  # Пустой список транзакций
    empty_descriptions = list(transaction_descriptions(empty_transactions))
    assert len(empty_descriptions) == 0
    assert list(transaction_descriptions(empty_transactions)) == []  # Убедимся, что возвращается пустой генератор


def test_card_number_generator():
    # Тестирование генератора на корректное создание номеров карт
    generated_cards = list(card_number_generator(1, 5))
    assert generated_cards == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    # Тестирование генератора с большим диапазоном
    generated_cards_large = list(card_number_generator(9999999999999980, 9999999999999990))
    assert generated_cards_large == [
        "9999 9999 9999 9980",
        "9999 9999 9999 9981",
        "9999 9999 9999 9982",
        "9999 9999 9999 9983",
        "9999 9999 9999 9984",
        "9999 9999 9999 9985",
        "9999 9999 9999 9986",
        "9999 9999 9999 9987",
        "9999 9999 9999 9988",
        "9999 9999 9999 9989",
        "9999 9999 9999 9990",
    ]

    # Проверка на некорректные значения
    with pytest.raises(ValueError):
        list(card_number_generator(0, 5))  # Начальное значение меньше 1

    with pytest.raises(ValueError):
        list(card_number_generator(1, 99999999999999999))  # Конечное значение больше 9999999999999999

    with pytest.raises(ValueError):
        list(card_number_generator(5, 1))  # Начальное значение больше конечного

    # Проверка на крайние значения
    single_card = list(card_number_generator(1, 1))
    assert single_card == ["0000 0000 0000 0001"]

    single_card_max = list(card_number_generator(9999999999999999, 9999999999999999))
    assert single_card_max == ["9999 9999 9999 9999"]
