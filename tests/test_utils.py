from src.utils import get_fin_transactions
import pytest

"""
Для тестирования работы функции get_fin_transactions используются файлы .json из директории tests/tests_data
запуск тестов осуществляется командой pytest из терминала,
пути настроены для запуска из директории проекта,а не теста
 """


def test_get_fin_transaction_success() -> None:
    """Тест нормальной работы функции"""
    result = get_fin_transactions("tests/tests_data/test_operations.json")
    assert result[0]["id"] == 441945886
    assert isinstance(result, list)


def test_get_fin_transaction_not_file(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест работы функции, если файл не найден"""
    result = get_fin_transactions("tests/missing_file.json")
    captured = capsys.readouterr()
    assert captured.out == "File not Found\n"
    # Функция в любом случае отработает и вернет пустой список
    assert result == []


def test_get_fin_transaction_invalid_json(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест работы функции, с ошибкой декодирования файла"""
    result = get_fin_transactions("tests/tests_data/invalid_file.json")
    captured = capsys.readouterr()
    assert captured.out == "Invalid JSON data.\n"
    # Функция в любом случае отработает и вернет пустой список
    assert result == []


def test_get_fin_transaction_empty_list() -> None:
    """Тест работы функции если на входе пустой список"""
    result = get_fin_transactions("tests/tests_data/empty_list.json")
    # Функция в любом случае отработает и вернет пустой список
    assert result == []
