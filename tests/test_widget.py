import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "user_card_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_normal(user_card_data: str, expected: str) -> None:
    assert mask_account_card(user_card_data) == expected


@pytest.fixture
def account_card_data_invalid() -> str:
    return "Счет 123"


def test_mask_account_card_invalid(account_card_data_invalid: str) -> None:
    assert mask_account_card(account_card_data_invalid) == "Некорректный номер счета или карты"


@pytest.mark.parametrize(
    "user_card_data_invalid, expected",
    [
        ("МИР 1596837868705199", "МИР 1596 83** **** 5199"),
        ("Счет 123", "Некорректный номер счета или карты"),
        ("", "Некорректный номер счета или карты"),
        ("Счет", "Некорректный номер счета или карты"),
    ],
)
def test_mask_account_card_invalid_value(user_card_data_invalid: str, expected: str) -> None:
    assert mask_account_card(user_card_data_invalid) == expected


@pytest.fixture
def date_time_iso_normal() -> str:
    return "2024-03-11T02:26:18.671407"


def test_get_date(date_time_iso_normal: str) -> None:
    assert get_date(date_time_iso_normal) == "11.03.2024"


def test_get_date_invalid() -> None:
    assert get_date("15.04.2026 15:00:00") == "Некорректный формат даты"


def test_get_date_empty() -> None:
    assert get_date("") == "Некорректный формат даты"
