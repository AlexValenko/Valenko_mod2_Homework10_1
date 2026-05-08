import json
from typing import Union


def get_fin_transactions(path_json: str) -> Union[list[dict[str, str | dict[str, str]]], list]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(path_json, encoding="utf-8") as file:
            transactions_data = json.load(file)
    except FileNotFoundError:
        print("File not Found")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON data.")
        return []
    if not transactions_data:
        return []

    return transactions_data
