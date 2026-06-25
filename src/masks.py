import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_hendler = logging.FileHandler("./logs/masks.log" 'w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_hendler.setFormatter(file_formatter)
logger.addHandler(file_hendler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_number_str = str(card_number)
    logger.debug(f"номер карты : {card_number_str}")
    if len(card_number_str) != 16:
        raise ValueError("Номер карты должен быть 16 цифр")
    card_number = card_number.replace(" ", "")
    card_number = card_number.replace("-", "")
    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.debug(masked_card)
    return str(masked_card)


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    account_str = str(account_number)
    logger.debug(account_str)
    if len(account_str) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")
    masked_account = f"**{account_str[-4:]}"
    logger.debug(masked_account)
    return masked_account
