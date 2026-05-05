from masks import get_mask_account, get_mask_card_number

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
    if any(card in arg for card in ["MasterCard", "Visa", "Maestro"]):
        card_number = arg[-16:].strip()
        masked_card = get_mask_card_number(card_number)
        return f"{arg[0:-16]}{masked_card}"
    elif "Счет" in arg:
        account_number = arg.split()[1]
        masked_account = get_mask_account(account_number)
        return f"{arg[0:-20]}{masked_account}"
    else:
        return "Неизвестный формат"  # Обработка других случаев


for data in input_data:
    print(mask_account_card(data))


def get_date(date: str) -> str:
    """ Функция возвращает строку с датой в формате ДД.ММ.ГГГГ """
    return f"{date[8:10]}-{date[5:7]}-{date[0:4]}"


print(get_date("2024-03-11T02:26:18.671407"))
