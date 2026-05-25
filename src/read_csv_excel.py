import csv

import pandas as pd

NORMAL_KEYS = {"id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"}


def get_transaction_from_csv(path_csv: str) -> list:
    """Функция для считывания финансовых операций из CSV-файла, принимает путь к файлу CSV в качестве аргумента.
    Возвращает список словарей с транзакциями в приведенном виде."""
    transactions_data = []
    try:
        with open(path_csv, "r", encoding="utf-8") as csv_file:
            reader_csv = csv.DictReader(csv_file, delimiter=";")
            for row in reader_csv:
                transactions_data.append(row)
    except FileNotFoundError:
        return []

    # Проверяем, что ключи полученного словаря содержат нужные ключи, иначе - пустой список
    keys_dict = set(transactions_data[0].keys())
    if NORMAL_KEYS.issubset(keys_dict):
        # Вызываем функцию приведения обычного словаря к вложенной структуре по примеру файла operations.json
        standard_transactions_data = get_standard_transactions(transactions_data)
    else:
        print("Invalid file")
        return []

    return standard_transactions_data


def get_transaction_from_excel(path_xlsx: str) -> list:
    """Функция для считывания финансовых операций из файла Excel, принимает путь к файлу CSV в качестве аргумента.
    Возвращает список словарей с транзакциями в приведенном виде."""
    try:
        transaction_df = pd.read_excel(path_xlsx, dtype=str)  # Преобразует данные всех полей Excel файла в строки
        try:
            # Фильтрует Датафрэйм, если поле id пустое
            not_null_id_transactions = transaction_df.loc[transaction_df["id"].notnull()]
        except KeyError:
            print("Invalid file")
            return []
        transaction_from_excel = not_null_id_transactions.to_dict(orient="records")
    except FileNotFoundError:
        print("File not found")
        return []
    keys_dict = set(transaction_from_excel[0].keys())
    # Проверяем, что ключи полученного словаря содержат нужные ключи, иначе - пустой список
    if NORMAL_KEYS.issubset(keys_dict):
        # Вызываем функцию приведения обычного словаря к вложенной структуре по примеру файла operations.json
        standard_transactions_data = get_standard_transactions(transaction_from_excel)
        return standard_transactions_data
    else:
        print("Invalid file")
        return []


def get_standard_transactions(transactions_data: list) -> list:
    """Функция принимает на вход список словарей с транзакциями и возвращает список словарей с транзакциями
    в стандартизированном виде, приведенном к примеру файла operations.json"""
    edited_transaction = []
    for transaction in transactions_data:
        if (
            transaction.get("id") in [None, "nan", ""]
            and transaction.get("date") in [None, "nan", ""]
            and transaction.get("state") in [None, "nan", ""]
        ):
            continue
        standard_dict = {}
        currency = {"name": transaction.get("currency_name"), "code": transaction.get("currency_code")}
        operation_amount = {"amount": transaction.get("amount"), "currency": currency}
        standard_dict["id"] = transaction.get("id")
        standard_dict["state"] = transaction.get("state")
        standard_dict["date"] = transaction.get("date")
        standard_dict["operationAmount"] = operation_amount
        standard_dict["description"] = transaction.get("description")
        standard_dict["from"] = transaction.get("from")
        standard_dict["to"] = transaction.get("to")
        edited_transaction.append(standard_dict)
    return edited_transaction
