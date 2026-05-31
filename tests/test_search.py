import pytest

from src.search import process_bank_operations, process_bank_search


@pytest.fixture
def get_transactions() -> list[dict]:
    return [
        {
            "id": 441945886,
            "description": "Перевод организации",
        },
        {
            "id": 41428829,
            "description": "Перевод организации",
        },
        {
            "id": 939719570,
            "description": "Перевод организации",
        },
        {
            "id": 587085106,
            "description": "Открытие вклада",
        },
        {
            "id": 142264268,
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "description": "Перевод со счета на счет",
        },
    ]


@pytest.fixture
def get_transactions_filtered() -> list[dict]:
    return [
        {
            "id": 441945886,
            "description": "Перевод организации",
        },
        {
            "id": 41428829,
            "description": "Перевод организации",
        },
        {
            "id": 939719570,
            "description": "Перевод организации",
        },
    ]


def test_process_bank_search_norm(get_transactions: list[dict], get_transactions_filtered: list[dict]) -> None:
    """Пример нормальной работы функции поиска транзакций по описанию"""
    result = process_bank_search(data=get_transactions, search="перевод организации")
    assert result == get_transactions_filtered
    assert len(result) == 3


def test_process_bank_search_incorrect(get_transactions: list[dict]) -> None:
    """Пример работы функции если нет соответствия поисковой строке"""
    result = process_bank_search(data=get_transactions, search="Некорректная строка")
    assert result == []


def test_process_bank_operations_norm(get_transactions: list[dict]) -> None:
    """Пример нормальной работы функции подсчета транзакций по категориям"""
    result = process_bank_operations(data=get_transactions, categories=["Открытие вклада", "Перевод со счета на счет"])
    assert result == {"Открытие вклада": 1, "Перевод со счета на счет": 2}


def test_process_bank_operations_none_trans(get_transactions: list[dict]) -> None:
    """Пример работы функции подсчета транзакций по категориям если нет пересечения"""
    result = process_bank_operations(
        data=get_transactions, categories=["Перевод с карты на карту", "Неизвестная операция"]
    )
    assert result == {}
