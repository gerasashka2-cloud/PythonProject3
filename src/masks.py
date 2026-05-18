def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        raise ValueError("Номер карты должен быть 16 цифр")
    card_number = card_number.replace(" ", "")
    card_number = card_number.replace("-", "")
    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return str(masked_card)


# print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    account_str = str(account_number)
    if len(account_str) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")
    masked_account = f"**{account_str[-4:]}"
    return masked_account


# print(get_mask_account("73654108430135874305"))
