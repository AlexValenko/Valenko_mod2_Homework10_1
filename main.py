from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    """Печатает в консоль маскированный номер карты и счета"""
    card_number = 7000792289606361  # пример номера карты
    account_number = 73654108430135874305  # пример номера счета

    masked_card = get_mask_card_number(card_number)
    masked_account = get_mask_account(account_number)

    print(f"Маскированный номер карты: {masked_card}")
    print(f"Маскированный номер счета: {masked_account}")


if __name__ == "__main__":
    main()
