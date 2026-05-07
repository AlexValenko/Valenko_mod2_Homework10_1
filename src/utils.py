import json
import os

def get_fin_transactions(path_json) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(path_json, encoding='utf-8') as file:
            transactions_data = json.load(file)
    except FileNotFoundError:
        print("File not Found")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON data.")
        return []
    except TypeError:
        print("Object of type set is not JSON serializable.")
        return []
    if not transactions_data or type(transactions_data) != list:
        return []

    return transactions_data


path_file_transactions = os.path.join(os.path.dirname(os.getcwd()),'data/operations.json')
second_operation = get_fin_transactions(path_file_transactions)
print(second_operation)
