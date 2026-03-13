from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(user_card_data: str) -> str:
    '''Принимает данные счета или карты и маскирует номер'''
    user_data_list = user_card_data.split()
    if user_data_list[0] == "Счет" or len(user_data_list[-1]) == 20:
        result = " ".join(["Счет ", get_mask_account(user_data_list[-1])])
    elif len(user_data_list[-1]) == 16:
        user_data_list[-1] = get_mask_card_number(user_data_list[-1])
        result = " ".join(user_data_list)
    else:
        result = "Некорректный номер счета или карты"
    return result
