import os
from typing import Any

import pytest

from src.decorators import log
from src.masks import get_mask_card_number


def test_decorator_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест успешного выполнения функции с логированием в консоль"""

    @log()
    def simple_addition(x: int, y: int) -> int:
        return x + y

    result = simple_addition(2, 3)
    assert result == 5
    captyred = capsys.readouterr()

    assert captyred.out == "simple_addition OK\n"
    assert captyred.err == ""


def test_decorator_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест обработки исключения с логированием в консоль"""

    @log()
    def simple_addition_err(x: int, y: int) -> int:
        return x + y

    with pytest.raises(TypeError):
        simple_addition_err("a", 3)

    captured = capsys.readouterr()

    expected_log = (
        'foo "simple_addition_err" Error "can only concatenate str (not "int") to str", inputs: (\'a\', 3), {}\n'
    )

    assert captured.out == expected_log
    assert captured.err == ""


# Путь к файлу с логами
log_file_path = os.path.join(os.path.join(os.getcwd(), "logs"), "my_log.txt")
print(log_file_path)


def test_decorator_file_success() -> None:
    """Тест успешного выполнения функции с логированием в файл"""

    @log(log_file_path)
    def example_foo(x: int, y: int) -> int:
        return x + y

    result = example_foo(3, 4)

    assert result == 7

    with open(log_file_path, "r", encoding="utf-8") as f:
        log_content = f.readlines()
    # Проверяет, что результат выполнения функции записан в последней строке лог файла
    assert f"result: {result}," in log_content[-1]


def test_decorator_file_error() -> None:
    """Тест выполнения функции с исключением с логированием в файл"""

    @log(log_file_path)
    def get_square(x: int) -> Any:
        if x < 0:
            raise ValueError("Negative value not allowed")
        return x**0.5

    with pytest.raises(ValueError, match="Negative value not allowed"):
        get_square(-2)

    with open(log_file_path, "r", encoding="utf-8") as f:
        log_content = f.readlines()
    log_error_mess = "Negative value not allowed"
    assert log_error_mess in log_content[-1]


def test_decorator_mask_card() -> None:
    """Тест декоратора логирования на примере работы функции маскировки карты"""

    @log(log_file_path)
    def proba_mask_card(card_number: int = 1234567812345678) -> None:
        result = get_mask_card_number(card_number)
        assert result == "1234 56** **** 5678"
        with open(log_file_path, "r", encoding="utf-8") as f:
            log_content = f.readlines()
        # Проверяет, что результат выполнения функции записан в последней строке лог файла
        assert f"result: {result}," in log_content[-1]
