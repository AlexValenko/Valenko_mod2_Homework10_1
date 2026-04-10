import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "user_card_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),  # Если название карты в одно слово
        ("Счет 64686473678894779589", "Счет **9589"),  # Нормальный номер счета 20 символов
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),  # Если карта 2 слова
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_normal(user_card_data: str, expected: str) -> None:
    """Проверка нормального случая работы mask_account_card"""
    assert mask_account_card(user_card_data) == expected


@pytest.fixture
def account_card_data_invalid() -> str:
    return "Счет 123"


def test_mask_account_card_invalid(account_card_data_invalid: str) -> None:
    """Проверка работы mask_account_card с некорректными данными (короткий номер счета)"""
    assert mask_account_card(account_card_data_invalid) == "Некорректный номер счета или карты"


@pytest.mark.parametrize(
    "user_card_data_invalid, expected",
    [
        ("МИР 1596837868705199", "МИР 1596 83** **** 5199"),  # Если название карты на кириллице
        ("Счет 123", "Некорректный номер счета или карты"),  # Если в счете недостаточно цифр
        ("", "Некорректный номер счета или карты"),  # Если пустой ввод
        ("Счет", "Некорректный номер счета или карты"),  # Если счет не содержит символов
    ],
)
def test_mask_account_card_invalid_value(user_card_data_invalid: str, expected: str) -> None:
    """Проверка работы mask_account_card с различными некорректными данными (параметризация)"""
    assert mask_account_card(user_card_data_invalid) == expected


@pytest.fixture
def date_time_iso_normal() -> str:
    return "2024-03-11T02:26:18.671407"


def test_get_date(date_time_iso_normal: str) -> None:
    """Проверка работы get_date с различными данными"""
    assert get_date(date_time_iso_normal) == "11.03.2024"
    assert get_date("15.04.2026 15:00:00") == "Некорректный формат даты"
    assert get_date("") == "Некорректный формат даты"  # Если пустой ввод
