from typing import Any, Dict, Generator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Generator[dict[str, Any], Any, None]:
    """ Функция фильтрует транзакции по заданной валюте """
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code:
            yield transaction


def transaction_descriptions(list_transactions: List[Dict[str, Any]]) -> Generator[Any, Any, None]:
    """ Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди """
    for transaction in list_transactions:
        yield transaction.get('description', 'Нет описания')  # Возвращаем описание или сообщение по умолчанию


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор card_number_generator,
    который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X— цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001
    до 9999 9999 9999 9999.
    """
    if not (1 <= start <= 9999999999999999):
        raise ValueError("Начальное значение должно быть в диапазоне от 1 до 9999999999999999")
    if not (1 <= end <= 9999999999999999):
        raise ValueError("Конечное значение должно быть в диапазоне от 1 до 9999999999999999")
    if start > end:
        raise ValueError("Начальное значение не может быть больше конечного")
    for number in range(start, end + 1):
        number_str = f"{number:016d}"
        formatted_card = ' '.join(number_str[i:i + 4] for i in range(0, 16, 4))
        yield formatted_card
