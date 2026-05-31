import re

def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
     и возвращает список словарей, у которых в описании есть данная строка"""
    filtered_transactions = []
    pattern = re.compile(search, re.IGNORECASE)
    for transaction in data:
        if re.search(pattern=pattern, string=transaction.get('description')):
            filtered_transactions.append(transaction)
    return filtered_transactions


