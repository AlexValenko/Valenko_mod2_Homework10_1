from src.read_csv_excel import get_transaction_from_csv, get_transaction_from_excel
from src.search import process_bank_search, process_bank_operations
# Тестовый запуск
if __name__ == "__main__":

    #Тестовый запуск чтения транзакций из файла csv
    csv_transactions = get_transaction_from_csv(path_csv='data/transactions.csv')
    print(csv_transactions[0])
    opened_transactions = process_bank_search(data=csv_transactions, search="Перевод со счета на счет")
    print(f'Найдено транзакций {len(opened_transactions)}')
    print(opened_transactions[0].get("id"), opened_transactions[0].get("description"))
    print(opened_transactions[-1].get("id"), opened_transactions[-1].get("description"))

    current_category = ["Перевод организации", "Открытие вклада", "Перевод со счета на счет"]
    category_counts = process_bank_operations(data=csv_transactions, categories=current_category)
    print(category_counts)

    #
    # excel_transactions = get_transaction_from_excel(path_xlsx='data/transactions_excel.xlsx')
    # print(excel_transactions[0])
    # print(excel_transactions[1])






