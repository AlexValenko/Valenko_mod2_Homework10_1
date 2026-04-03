from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_card_data: str) -> str:
    """Принимает данные счета или карты и маскирует номер"""
    if not user_card_data:
        return "Некорректный номер счета или карты"
    user_data_list = user_card_data.split()
    # If the first word is "Счет" and the last word contains 20 digits
    if user_data_list[0] == "Счет" and len(user_data_list[-1]) == 20:
        result = " ".join(["Счет", get_mask_account(user_data_list[-1])])
    elif len(user_data_list[-1]) == 16:
        user_data_list[-1] = get_mask_card_number(user_data_list[-1])
        result = " ".join(user_data_list)
    else:
        # If the data is incorrect
        result = "Некорректный номер счета или карты"
    return result


def get_date(time_iso: str) -> str:
    """Возвращает ДД.ММ.ГГГГ из формата ISO"""
    if not time_iso or time_iso[10] != "T":
        return "Некорректный формат даты"
    date_and_time = time_iso.split("T")
    date_list = date_and_time[0].split("-")
    return ".".join(date_list[::-1])
