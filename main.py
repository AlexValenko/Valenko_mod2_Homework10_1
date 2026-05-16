from src.masks import get_mask_account, get_mask_card_number
from src.utils import get_fin_transactions

# Тестовая функций для модуля src/masks.py
def main_masks() -> None:
    """Печатает в консоль маскированный номер карты и счета"""
    card_number = 7000792289606361  # пример номера карты
    account_number = 73654108430135874305  # пример номера счета

    masked_card = get_mask_card_number(card_number)
    masked_account = get_mask_account(account_number)

    print(f"Маскированный номер карты: {masked_card}")
    print(f"Маскированный номер счета: {masked_account}")

# Тестовый запуск функции get_fin_transactions из модуля src/utils.py
if __name__ == "__main__":
    # Нормальная работа
    example_transactions = get_fin_transactions('data/operations.json')
    print(example_transactions[1])
    # Файл поврежден
    get_fin_transactions('tests/tests_data/invalid_file.json')
