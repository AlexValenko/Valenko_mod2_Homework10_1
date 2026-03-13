from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Маскирует цифры номера карты и разделяет их на блоки по 4 цифры"""
    card_number_str = str(card_number).strip()
    masked_card = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
    return masked_card


def get_mask_account(account_number: Union[str, int]) -> str:
    """Скрывает номер счета кроме последних 4 цифр"""
    account_number_str = str(account_number).strip()
    masked_account = "**" + account_number_str[-4:]
    return masked_account
