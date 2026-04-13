from collections.abc import Generator


def filter_by_currency(transactions_data: list[dict], currency: str) -> Generator:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    if not transactions_data:
        yield []
    if not any(x["operationAmount"]["currency"]["code"] == currency for x in transactions_data):
        yield "No transactions"
    try:
        yield from filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions_data)
    except KeyError:
        yield "key not found"


def transaction_descriptions(transactions_data: list[dict]) -> Generator:
    """Принимает список транзакций и возвращает описание каждой операции по очереди"""
    if not transactions_data:
        yield []
    if not any(x["description"] for x in transactions_data):
        yield "No transactions"
    else:
        for i in transactions_data:
            try:
                yield i["description"]
            except KeyError:
                yield "key description not found"


def card_number_generator(start_card_num: int = 1, end_card_num: int = 9999999999999999) -> Generator:
    """Принимает начальный и конечный номер диапазона и выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    if 1 <= start_card_num <= end_card_num <= 9999999999999999:
        num = start_card_num
        while num <= end_card_num:
            string_num = str(num).zfill(16)
            yield string_num[:4] + " " + string_num[4:8] + " " + string_num[8:12] + " " + string_num[12:]
            num += 1
    else:
        yield "Incorrect diapason"
