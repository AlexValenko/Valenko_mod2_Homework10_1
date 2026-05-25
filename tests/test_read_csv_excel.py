from unittest.mock import patch

import pytest

from src.read_csv_excel import get_transaction_from_csv, get_transaction_from_excel


@pytest.fixture
def first_transactions() -> list:
    """Первые 3 транзакции, приведенные ко вложенной структуре"""
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": "29740", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        {
            "id": "593027",
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "operationAmount": {"amount": "30368", "currency": {"name": "Shilling", "code": "TZS"}},
            "description": "Перевод с карты на карту",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
        },
    ]


def test_get_transaction_from_csv_normal(first_transactions:list) -> None:
    """Пример нормальной работы функции get_transaction_from_csv с тестовым файлом tests_data/transactions_test.csv"""
    result = get_transaction_from_csv(path_csv="tests/tests_data/transactions_test.csv")
    assert result == first_transactions
    assert isinstance(result, list)


def test_get_transaction_from_csv_not_file() -> None:
    """Пример работы функции get_transaction_from_csv с исключением FileNotFoundError"""
    result = get_transaction_from_csv(path_csv="none_data")
    assert result == []


def test_get_transaction_from_csv_incorrect_data(capsys: pytest.CaptureFixture[str]) -> None:
    """Пример работы функции get_transaction_from_csv с некорректными данными"""
    mock_incorrect_data = [{"name": "Rent", "date": "2023-01-15"}, {"name": "Salary", "date": "2023-01-20"}]
    with patch("csv.DictReader") as mock_reader:
        mock_reader.return_value = iter(mock_incorrect_data)
    result = get_transaction_from_csv(path_csv="none_data")
    assert result == []


def test_get_transaction_from_csv_decode_error(capsys: pytest.CaptureFixture[str]) -> None:
    """Пример ошибки декодирования файла в csv в функции get_transaction_from_csv
    с тестовым файлом tests_data/transactions_test_invalid.csv"""
    result = get_transaction_from_csv(path_csv="tests/tests_data/transactions_test_invalid.csv")
    captured = capsys.readouterr()
    assert result == []
    assert captured.out == "Invalid file\n"


def test_get_transaction_from_excel_normal(first_transactions:list) -> None:
    """Пример нормальной работы функции get_transaction_from_excel
    с тестовым файлом tests_data/transactions_test_excel.xlsx"""
    result = get_transaction_from_excel(path_xlsx="tests/tests_data/transactions_test_excel.xlsx")
    assert result == first_transactions
    assert isinstance(result, list)


def test_get_transaction_from_excel_not_file(capsys: pytest.CaptureFixture[str]) -> None:
    """Пример работы функции get_transaction_from_excel с исключением FileNotFoundError"""
    result = get_transaction_from_excel("none_data")
    captured = capsys.readouterr()
    assert result == []
    assert captured.out == "File not found\n"


def test_get_transaction_from_excel_decode_error(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест некорректного заполнения названий столбцов в файле excel в функции get_transaction_from_excel
    с тестовым файлом tests_data/transactions_test_excel_invalid.xlsx"""
    result = get_transaction_from_excel(path_xlsx="tests/tests_data/transactions_test_excel_invalid.xlsx")
    captured = capsys.readouterr()
    assert result == []
    assert captured.out == "Invalid file\n"
