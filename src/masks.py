def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_number = card_number.replace(" ", "")
    card_number = card_number.replace("-", "")
    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[11:-1]}"
    return str(masked_card)


# print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Функция  принимает на вход номер счета и возвращает его маску"""
    account_number = account_number.replace(" ", "")
    account_number = account_number.replace("-", "")
    masked_account = f"**{account_number[-4:]}"
    return str(masked_account)


# print(get_mask_account("73654108430135874305"))
