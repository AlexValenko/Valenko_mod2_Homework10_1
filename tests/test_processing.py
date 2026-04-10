from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def input_list_test_data() -> List[Dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(input_list_test_data: List[Dict]) -> None:
    """Проверка работы filter_by_state с различными данными"""
    # Нормальный случай работы, "state" по умолчанию
    assert filter_by_state(input_list_test_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    # Нормальный случай работы, "state" по выбору
    assert filter_by_state(input_list_test_data, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    # Ключа "state" нет в словаре
    assert filter_by_state([{"id": 123, "date": "2019-07-03T18:35:29.512364"}, {"id": 111}]) == []
    assert filter_by_state([]) == []  # Пустой ввод


def test_sort_by_date(input_list_test_data: List[Dict]) -> None:
    """Проверка работы sort_by_date"""
    # Нормальный случай работы, направление сортировки по умолчанию
    assert sort_by_date(input_list_test_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    # Нормальный случай работы, направление сортировки по выбору
    assert sort_by_date(input_list_test_data, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    # Пустой ввод
    assert sort_by_date([]) == []
