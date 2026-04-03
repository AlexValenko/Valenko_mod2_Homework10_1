from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_number_normal() -> int:
    return 7000792289606361


@pytest.fixture
def account_number_normal() -> int:
    return 73654108430135874305


def test_get_mask_card_number_normal(card_number_normal: int) -> None:
    """Проверка работы get_mask_card_number с позитивным исходом"""
    assert get_mask_card_number(card_number_normal) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),  # Если integer
        ("7000792289606361", "7000 79** **** 6361"),  # Если строка
        ("  1111 1111 1111 1111  ", "1111 11** **** 1111"),  # Если пробелы
        ("1234 5678 123 12", "1234 56** **** 2312"),  # Если 13 цифр
        ("123", "Некорректный номер карты"),  # Если слишком короткий номер
        ("", "Некорректный номер карты"),  # Если пустой ввод
    ],
)
def test_get_mask_card_number_different_input(card_number: Union[str, int], expected: str) -> None:
    """Проверка работы get_mask_card_number с различными вариантами входных данных"""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_account_normal(account_number_normal: int) -> None:
    """Проверка работы get_mask_account с позитивным исходом"""
    assert get_mask_account(account_number_normal) == "**4305"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (73654108430135874305, "**4305"),  # Если integer
        ("73654108430135874305", "**4305"),  # Если строка
        ("11 111  111 11111", "**1111"),  # Если пробелы
        ("", "Некорректный номер счета"),  # Если пустой ввод
    ],
)
def test_get_mask_account_different_input(account_number: Union[str, int], expected: str) -> None:
    """Проверка работы get_mask_account с различными вариантами входных данных"""
    assert get_mask_account(account_number) == expected
