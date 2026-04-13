import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
# Полный список исходных данных
def example_transactions() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
# Список транзакций в долларах
def usd_filtered_transactions() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.fixture
# Первая встречающаяся транзакция в рублях
def rub_filtered_transactions() -> dict:
    return {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


def test_filter_by_currency_usd(example_transactions: list[dict], usd_filtered_transactions: list[dict]) -> None:
    """Пример нормальной работы функции с тестовым списком данных в валюте USD"""
    generator_funk = filter_by_currency(example_transactions, "USD")
    assert next(generator_funk) == usd_filtered_transactions[0]
    assert next(generator_funk) == usd_filtered_transactions[1]


def test_filter_by_currency_rub(example_transactions: list[dict], rub_filtered_transactions: dict) -> None:
    """Пример нормальной работы функции с тестовым списком данных в валюте RUB"""
    generator_funk = filter_by_currency(example_transactions, "RUB")
    assert next(generator_funk) == rub_filtered_transactions


def test_filter_by_currency_empty() -> None:
    """Пример работы функции с пустым списком на входе"""
    generator_funk = filter_by_currency([], "RUB")
    assert next(generator_funk) == []


def test_transaction_descriptions_norm(example_transactions: list[dict]) -> None:
    """Пример нормальной работы функции transaction_descriptions()"""
    gen_descriptions = transaction_descriptions(example_transactions)
    assert next(gen_descriptions) == "Перевод организации"
    assert next(gen_descriptions) == "Перевод со счета на счет"


def test_transaction_descriptions_empty() -> None:
    """Пример работы функции transaction_descriptions с пустым списком на входе"""
    gen_descriptions = transaction_descriptions([])
    assert next(gen_descriptions) == []


def test_card_number_generator_norm() -> None:
    """Пример нормальной работы функции card_number_generator()"""
    gen_numbers = card_number_generator(1, 3)
    assert next(gen_numbers) == "0000 0000 0000 0001"
    assert next(gen_numbers) == "0000 0000 0000 0002"
    assert next(gen_numbers) == "0000 0000 0000 0003"


def test_card_number_generator_invalid_values() -> None:
    """Пример работы функции card_number_generator() при некорректно заданном диапазоне"""
    gen_numbers = card_number_generator(-2, 2)
    assert next(gen_numbers) == "Incorrect diapason"
