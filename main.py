from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_csv_excel import get_transaction_from_csv, get_transaction_from_excel
from src.search import process_bank_search
from src.utils import get_fin_transactions
from src.widget import get_date, mask_account_card

# Основная функция


def main() -> None:
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")
    file_type = input()
    if file_type == "1":
        all_transactions_data = get_fin_transactions(path_json="data/operations.json")
        print("Для обработки выбран JSON-файл.\n")
    elif file_type == "2":
        all_transactions_data = get_transaction_from_csv(path_csv="data/transactions.csv")
        print("Для обработки выбран CSV-файл.\n")
    elif file_type == "3":
        all_transactions_data = get_transaction_from_excel(path_xlsx="data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл.\n")
    else:
        print("Ошибка: пункт меню не найден. Программа завершена.")
        exit()
    print("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        current_state = input("Введите статус для фильтрации транзакций: ").upper()
        if current_state == "EXECUTED":
            filtered_by_state_transactions = filter_by_state(input_list=all_transactions_data)
            print('Операции отфильтрованы по статусу "EXECUTED"\n')
            break
        elif current_state == "CANCELED":
            filtered_by_state_transactions = filter_by_state(
                input_list=all_transactions_data, current_state="CANCELED"
            )
            print('Операции отфильтрованы по статусу "CANCELED"\n')
            break
        elif current_state == "PENDING":
            filtered_by_state_transactions = filter_by_state(input_list=all_transactions_data, current_state="PENDING")
            print('Операции отфильтрованы по статусу "PENDING"\n')
            break
        else:
            attempts += 1
            if attempts >= max_attempts:
                print("Превышено число попыток. Программа завершена.")
                exit()
            else:
                print(
                    f"Введите корректный статус для фильтрации транзакций из доступных [EXECUTED, CANCELED, PENDING],"
                    f"попытка {attempts + 1} из {max_attempts}"
                )

    # Сортировка по дате операции, по умолчанию - нет
    print("Отсортировать операции по дате? Да/Нет")
    flag_sorted = input().lower()
    if flag_sorted == "да":
        print("Отсортировать по возрастанию или по убыванию? ")  # По умолчанию - по убыванию
        flag_desending = input("Введите по возрастанию / по убыванию  \n").lower()
        if "возраст" in flag_desending:
            sorted_by_date_transactions = sort_by_date(input_list=filtered_by_state_transactions, descending=False)
        else:
            sorted_by_date_transactions = sort_by_date(input_list=filtered_by_state_transactions)
    else:
        sorted_by_date_transactions = filtered_by_state_transactions

    # Фильтр только по рублевым транзакциям, если нет, то выводит все
    print("Выводить только рублевые транзакции? Да/Нет  ")
    flag_rub = input().lower()
    if flag_rub == "да":
        filtered_by_valute = list(filter_by_currency(transactions_data=sorted_by_date_transactions, currency="RUB"))
    else:
        filtered_by_valute = sorted_by_date_transactions

    # Фильтр по описанию, если нет, то выводит все
    print("Отфильтровать список транзакций по определенному слову в описании?")
    flag_filter_by_description = input("Введите да/нет  \n").lower()
    if flag_filter_by_description == "да":
        search_words = input("Введите описание операции\n")
        filtered_by_description_transactions = process_bank_search(data=filtered_by_valute, search=search_words)
    else:
        filtered_by_description_transactions = filtered_by_valute

    # Формирование результата
    print("Распечатываю итоговый список транзакций...\n")
    if not filtered_by_description_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        exit()
    print(f"Всего банковских операций в выборке: {len(filtered_by_description_transactions)}\n")

    for transaction in filtered_by_description_transactions:
        transaction_date = get_date(time_iso=transaction.get("date"))
        transaction_description = transaction.get("description")
        print(f"{transaction_date} {transaction_description}")
        destination = mask_account_card(transaction.get("to"))
        if "from" in transaction.keys():
            departure = mask_account_card(transaction.get("from"))
            print(f"{departure} -> {destination}")
        else:
            print(destination)
        amount = transaction.get("operationAmount").get("amount")
        valuta = transaction.get("operationAmount").get("currency").get("name")
        print(f"Сумма: {amount} {valuta}\n")


if __name__ == "__main__":
    main()
