from typing import Any

import pytest

from src.search_transactions import counts_transactions, process_bank_search


# Тесты для функции process_bank_search
def test_one_coincidence() -> None:
    """Одно совпадение"""
    data: list[dict[str, Any]] = [
        {"description": "Перевод организации", "amount": 234},
        {"description": "Оплата услуг", "amount": 100},
    ]
    pattern: str = "Перевод"
    result = process_bank_search(data, pattern)
    expected: list[dict[str, Any]] = [{"description": "Перевод организации", "amount": 234}]
    assert result == expected


def test_empty_description() -> None:
    """description пустая строка"""
    data: list[dict[str, Any]] = [
        {"description": "", "amount": 100},
        {"description": "Перевод на карту", "amount": 200},
    ]
    pattern: str = "Перевод"
    result = process_bank_search(data, pattern)
    expected: list[dict[str, Any]] = [{"description": "Перевод на карту", "amount": 200}]
    assert result == expected


def test_multiple() -> None:
    """Несколько совпадений"""
    data: list[dict[str, Any]] = [
        {"description": "Перевод организации", "amount": 234},
        {"description": "Открытие вклада", "amount": 370},
        {"description": "Снятие наличных", "amount": 100},
    ]
    pattern: str = "Перевод|Открытие"
    result = process_bank_search(data, pattern)
    expected: list[dict[str, Any]] = [
        {"description": "Перевод организации", "amount": 234},
        {"description": "Открытие вклада", "amount": 370},
    ]
    assert result == expected


def test_no_coincidence() -> None:
    """Без совпадений"""
    data: list[dict[str, Any]] = [
        {"description": "Снятие наличных", "amount": 100},
        {"description": "Оплата услуг", "amount": 500},
    ]
    pattern: str = "Перевод|Открытие"
    result = process_bank_search(data, pattern)
    expected: list[dict[str, Any]] = []
    assert result == expected


def test_empty_list() -> None:
    """Пустой список"""
    data: list[dict[str, Any]] = []
    pattern: str = "Перевод"
    result = process_bank_search(data, pattern)
    expected: list[dict[str, Any]] = []
    assert result == expected


def test_none_and_float() -> None:
    """None или float"""
    data: list[dict[str, Any]] = [
        {"description": None, "amount": 100},
        {"description": 123.45, "amount": 200},
        {"description": "Перевод на карту", "amount": 300},
    ]
    pattern: str = "Перевод"
    result = process_bank_search(data, pattern)
    expected: list[dict[str, Any]] = [{"description": "Перевод на карту", "amount": 300}]
    assert result == expected


def test_register() -> None:
    """Тест на регистр"""
    data: list[dict[str, Any]] = [
        {"description": "перевод организации", "amount": 234},
        {"description": "ОТКРЫТИЕ вклада", "amount": 370},
    ]
    pattern: str = "Перевод|Открытие"
    result = process_bank_search(data, pattern)
    expected: list[dict[str, Any]] = [
        {"description": "перевод организации", "amount": 234},
        {"description": "ОТКРЫТИЕ вклада", "amount": 370},
    ]
    assert result == expected


def test_value_error() -> None:
    """Проверяет, что при передаче нестрокового аргумента search выбрасывается ValueError"""
    data: list[dict[str, Any]] = [{"description": "Test"}]
    search: Any= 123
    with pytest.raises(ValueError):
        process_bank_search(data, search)


def test_data_not_list() -> None:
    """Не список"""
    data: Any = {"description": "Перевод"}  # не список
    result = process_bank_search(data, "Перевод")
    assert result == []


def test_data_no_dict() -> None:
    """Элементы, не являющиеся словарями"""
    data: list[Any] = [{"description": "Перевод организации"}, "строка", 123, None]
    pattern: str = "Перевод"
    result = process_bank_search(data, pattern)
    expected: list[dict[str, Any]] = [{"description": "Перевод организации"}]
    assert result == expected


# Тесты для функции counts_transactions
def test_one_category() -> None:
    """Одна категория"""
    transactions: list[dict[str, Any]] = [
        {"description": "Перевод организации", "amount": 234},
        {"description": "Перевод организации", "amount": 300},
        {"description": "Оплата услуг", "amount": 100},
    ]
    categories: list[str] = ["Перевод"]
    result = counts_transactions(transactions, categories)
    expected: dict[str, Any] = {"Перевод организации": 2}
    assert result == expected


def test_multiple_categories() -> None:
    """Несколько категорий"""
    transactions: list[dict[str, Any]] = [
        {"description": "Перевод организации", "amount": 234},
        {"description": "Открытие вклада", "amount": 370},
        {"description": "Перевод организации", "amount": 220},
        {"description": "Снятие наличных", "amount": 100},
    ]
    categories: list[str] = ["Перевод", "Открытие"]
    result = counts_transactions(transactions, categories)
    expected: dict[str, int] = {"Перевод организации": 2, "Открытие вклада": 1}
    assert result == expected


def test_no_coincidence_categories() -> None:
    """Нет совпадений"""
    transactions: list[dict[str, Any]] = [
        {"description": "Снятие наличных", "amount": 100},
        {"description": "Оплата услуг", "amount": 500},
    ]
    categories: list[str] = ["Перевод", "Открытие"]
    result = counts_transactions(transactions, categories)
    expected: dict[str, int] = {}
    assert result == expected


def test_empty() -> None:
    """Пустой список"""
    transactions: list[dict[str, Any]] = []
    categories: list[str] = ["Перевод"]
    result = counts_transactions(transactions, categories)
    expected: dict[str, int] = {}
    assert result == expected


def test_space() -> None:
    """Проверка на пробелы"""
    transactions: list[dict[str, Any]] = [
        {"description": " Перевод организации ", "amount": 234},
        {"description": "Перевод с карты на карту", "amount": 300},
    ]
    categories: list[str] = ["Перевод"]
    result = counts_transactions(transactions, categories)
    expected: dict[str, int] = {"Перевод организации": 1, "Перевод с карты на карту": 1}
    assert result == expected


def test_categories_empty() -> None:
    """Пустой список категорий"""
    transactions: list[dict[str, Any]] = [{"description": "Перевод организации"}]
    result = counts_transactions(transactions, [])
    expected: dict[str, int] = {}
    assert result == expected


def test_transactions_on_dict() -> None:
    """list_transactions содержит не словари"""
    transactions: list[Any] = [{"description": "Перевод организации"}, "строка", None, 123]
    categories: list[str] = ["Перевод"]
    result = counts_transactions(transactions, categories)
    expected: dict[str, int] = {"Перевод организации": 1}
    assert result == expected


def test_description_is_none_or_missing() -> None:
    """description отсутствует или равен None"""
    transactions: list[dict[str, Any]] = [{"amount": 100}, {"description": None}, {"description": "Перевод на карту"}]
    categories: list[str] = ["Перевод"]
    result = counts_transactions(transactions, categories)
    expected: dict[str, int] = {"Перевод на карту": 1}
    assert result == expected
