import logging
from typing import Union

masks_logger = logging.getLogger("masks_logger")
masks_file_handler = logging.FileHandler(filename="logs/log_masks.log", mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s:%(filename)s:%(levelname)s:%(message)s")
masks_file_handler.setFormatter(file_formater)
masks_logger.addHandler(masks_file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Маскирует цифры номера карты и разделяет их на блоки по 4 цифры"""
    masks_logger.debug("Function get_mask_card_number starting...")
    card_number_str = str(card_number).strip().replace(" ", "")
    if len(card_number_str) < 12:
        masks_logger.error("Некорректный номер карты")
        return "Некорректный номер карты"
    masked_card = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
    masks_logger.debug(f"The card {masked_card} successfully masked")
    return masked_card


def get_mask_account(account_number: Union[str, int]) -> str:
    """Скрывает номер счета кроме последних 4 цифр"""
    masks_logger.debug("Function get_mask_account starting...")
    account_number_str = str(account_number).strip().replace(" ", "")
    if len(account_number_str) < 6:
        masks_logger.error("Некорректный номер счета")
        return "Некорректный номер счета"
    masked_account = "**" + account_number_str[-4:]
    masks_logger.debug(f"The account {masked_account} successfully masked")
    return masked_account
