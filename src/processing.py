from typing import Dict, List


def filter_by_state(input_list: List[Dict], current_state: str = "EXECUTED") -> List[Dict]:
    """Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению. По умолчанию 'EXECUTED'"""
    output_list = []
    for i in input_list:
        if "state" in i:
            if i["state"] == current_state:
                output_list.append(i)
    return output_list


def sort_by_date(input_list: List[Dict], descending: bool = True) -> List[Dict]:
    """Возвращает новый список, отсортированный по дате"""
    return sorted(input_list, key=lambda x: x["date"], reverse=descending)
