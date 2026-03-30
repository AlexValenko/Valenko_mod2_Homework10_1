def filter_by_state(input_list: list, current_state: str = "EXECUTED") -> list:
    """Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению. По умолчанию 'EXECUTED'"""
    output_list = []
    for i in input_list:
        if "state" in i:
            if i["state"] == current_state:
                output_list.append(i)
    return output_list


def sort_by_date():
    """Возвращает новый список, отсортированный по дате"""
    pass
