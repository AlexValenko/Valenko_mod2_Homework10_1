from numpy.random import standard_t

from src.masks import get_mask_account, get_mask_card_number
from src.utils import get_fin_transactions
from src.read_csv_excel import get_transaction_from_csv, get_transaction_from_excel

# Тестовый запуск
if __name__ == "__main__":
    # # Нормальная работа функций get_fin_transactions из модуля src/utils.py
    # example_transactions = get_fin_transactions('data/operations.json')
    # print(example_transactions[1])
    # # Файл поврежден
    # get_fin_transactions('tests/tests_data/invalid_file.json')
    #
    # # Тестовый запуск функций из модуля src/masks.py - нормальные данные
    # print(get_mask_card_number(7000792289606361))
    # print(get_mask_account(73654108430135874305))
    # # Тестовый запуск функций из модуля src/masks.py - некорректные данные
    # get_mask_card_number('acb')
    # get_mask_account(0)

    #Тестовый запуск чтения транзакций из файла csv
    csv_transactions = get_transaction_from_csv('tests/tests_data/transactions_test.csv')


    excel_transactions = get_transaction_from_excel('tests/tests_data/transactions_test_excel.xlsx')
    print(excel_transactions[0])





