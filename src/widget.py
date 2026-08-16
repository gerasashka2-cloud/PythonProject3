import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

input_data = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]


def mask_account_card(arg: str) -> str:
    """Проверяем, является ли аргумент номером карты или счета"""
    # Используем регулярное выражение для поиска номеров карт
    card_number_match = re.search(r'\d{16,19}', arg)
    if "Счет" in arg:
        account_number = arg.split()[1]
        if len(account_number) != 20:
            return "Номер счета должен содержать 20 цифр"
        masked_account = get_mask_account(account_number)
        return f"{arg[0:-20]}{masked_account}"
    elif card_number_match:
        card_number = card_number_match.group()[-16:]  # Извлекаем последние 16 цифр
        masked_card = get_mask_card_number(card_number)
        return f"{arg[0:card_number_match.start()]}{masked_card}"

    else:
        return "Неизвестный формат"  # Обработка других случаев

for data in input_data:
    print(mask_account_card(data))


def get_date(date_string: str) -> str:
    """
    Функция принимает строку с датой и временем в формате
    ISO 8601 и возвращает дату в формате DD-MM-YYYY.
    """
    if not date_string:
        raise ValueError("Строка не может быть пустой")
    try:
        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")  # Форматирование даты в DD-MM-YYYY
    except ValueError:
        raise ValueError("Неверный формат даты")


print(get_date("2024-03-11T02:26:18.671407"))
