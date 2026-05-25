from src.read_csv_excel import get_transaction_from_csv, get_transaction_from_excel

# Тестовый запуск
if __name__ == "__main__":

    #Тестовый запуск чтения транзакций из файла csv
    csv_transactions = get_transaction_from_csv(path_csv='data/transactions.csv')
    print(csv_transactions[0])
    print(csv_transactions[1])


    excel_transactions = get_transaction_from_excel(path_xlsx='data/transactions_excel.xlsx')
    print(excel_transactions[0])
    print(excel_transactions[1])






