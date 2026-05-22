import pandas as pd
import csv

def get_transaction_from_csv(path_csv: str) -> list:
    """Функция для считывания финансовых операций из CSV-файла, принимает путь к файлу CSV в качестве аргумента.
    Возвращает список словарей с транзакциями в приведенном виде."""
    transactions_data = []
    try:
        with open(path_csv, 'r', encoding='utf-8') as csv_file:
            reader_csv = csv.DictReader(csv_file, delimiter=";")
            for row in reader_csv:
                transactions_data.append(row)
    except FileNotFoundError:
        return []
    # Вызываем функцию приведения обычного словаря к вложенной структуре по примеру файла operations.json
    standard_transactions_data = get_standard_transactions(transactions_data)
    return standard_transactions_data

def get_transaction_from_excel(path_xlsx: str) -> list:
    """Функция для считывания финансовых операций из файла Excel, принимает путь к файлу CSV в качестве аргумента.
    Возвращает список словарей с транзакциями в приведенном виде."""
    transaction_df = pd.read_excel(path_xlsx, dtype=str) # Преобразует данные всех полей Excel файла в строки
    transaction_from_excel = transaction_df.to_dict(orient='records')
    # Вызываем функцию приведения обычного словаря к вложенной структуре по примеру файла operations.json
    standard_transactions_data = get_standard_transactions(transaction_from_excel)
    return standard_transactions_data

def get_standard_transactions(transactions_data: list) -> list:
    """Функция принимает на вход список словарей с транзакциями и возвращает список словарей с транзакциями
    в стандартизированном виде, приведенном к примеру файла operations.json"""
    edited_transaction = []
    for transaction in transactions_data:
        if transaction.get('id') == '' and transaction.get('date') == '' and transaction.get('state') == '':
            continue
        standard_dict = {}
        currency = { 'name' : transaction.get('currency_name'), 'code' : transaction.get('currency_code')}
        operation_amount = {'amount' : transaction.get('amount'), 'currency' : currency}
        standard_dict['id'] = transaction.get('id')
        standard_dict['state'] = transaction.get('state')
        standard_dict['date'] = transaction.get('date')
        standard_dict['operationAmount'] = operation_amount
        standard_dict['description'] = transaction.get('description')
        standard_dict['from'] = transaction.get('from')
        standard_dict['to'] = transaction.get('to')
        edited_transaction.append(standard_dict)
    return edited_transaction

