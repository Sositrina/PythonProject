from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> List[Dict]:
    """Возвращает пример списка словарей для тестов"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [41428829, 939719570]),
        ("CANCELED", [594226727, 615064591]),
    ],
)
def test_filter_by_state(sample_data: List[Dict], state: str, expected_ids: List[int]) -> None:
    """Проверяет фильтрацию словарей по ключу 'state'"""
    result = filter_by_state(sample_data, state)
    assert [item["id"] for item in result] == expected_ids


def test_filter_by_state_empty() -> None:
    """Проверяет, что функция выбрасывает ValueError на пустой список."""
    with pytest.raises(ValueError) as exc_info:
        filter_by_state([])
    assert str(exc_info.value) == "Список пуст"


def test_sort_by_date_descending(sample_data: List[Dict]) -> None:
    """Проверяет сортировку по убыванию по ключу 'date'"""
    result = sort_by_date(sample_data, reverse=True)
    expected_order = [41428829, 615064591, 594226727, 939719570]
    assert [item["id"] for item in result] == expected_order


def test_sort_by_date_ascending(sample_data: List[Dict]) -> None:
    """Проверяет сортировку по возрастанию по ключу 'date'"""
    result = sort_by_date(sample_data, reverse=False)
    expected_order = [939719570, 594226727, 615064591, 41428829]
    assert [item["id"] for item in result] == expected_order


def test_sort_by_date_same_dates() -> None:
    """Проверяет  сортировку, когда несколько элементов имеют одинаковую дату"""
    data = [
        {"id": 1, "date": "2023-01-01T00:00:00"},
        {"id": 2, "date": "2023-01-01T00:00:00"},
        {"id": 3, "date": "2022-12-31T23:59:59"},
    ]
    result = sort_by_date(data)
    expected_order = [1, 2, 3]
    assert [item["id"] for item in result] == expected_order


@pytest.mark.parametrize(
    "data",
    [
        [{"id": 1, "date": "2023-01-01"}, {"id": 2, "date": "not-a-date"}],
        [{"id": 1, "date": "invalid"}, {"id": 2, "date": "2023-01-01T00:00:00"}],
        [{"id": 1, "date": "2023/01/01"}, {"id": 2, "date": "2023-01-01T00:00:00"}],
    ],
)
def test_sort_by_date_invalid_format(data: List[Dict]) -> None:
    """Проверяет, что функция выбрасывает ValueError при неправильном формате даты."""
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(data)
    assert str(exc_info.value) == "Неправильная дата"
