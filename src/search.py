import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании есть данная строка"""
    filtered_transactions = []
    pattern = re.compile(search, re.IGNORECASE)
    for transaction in data:
        if re.search(pattern=pattern, string=str(transaction.get("description"))):
            filtered_transactions.append(transaction)
    return filtered_transactions


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""
    # Список - сборка из описаний транзакций только выбранных категорий
    filtered_description = [
        transaction.get("description") for transaction in data if transaction.get("description") in categories
    ]
    return dict(Counter(filtered_description))
