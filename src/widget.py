from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(user_card_data: str) -> str:
    """Принимает данные счета или карты и маскирует номер"""
    user_data_list = user_card_data.split()
    # If the first word is "Счет" or the last word contains 20 digits
    if user_data_list[0] == "Счет" or len(user_data_list[-1]) == 20:
        result = " ".join(["Счет ", get_mask_account(user_data_list[-1])])
    elif len(user_data_list[-1]) == 16:
        user_data_list[-1] = get_mask_card_number(user_data_list[-1])
        result = " ".join(user_data_list)
    else:
        # If the data is incorrect
        result = "Некорректный номер счета или карты"
    return result


def get_date(time_iso: str) -> str:
    """Возвращает ДД.ММ.ГГГГ из формата ISO"""
    date_and_time = time_iso.split("T")
    date_list = date_and_time[0].split("-")
    return ".".join(date_list[::-1])
