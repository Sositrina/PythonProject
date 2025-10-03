import pytest
from src.utils import accepts_reads_file
from unittest.mock import Mock, patch


@pytest.fixture
def receives_a_file() -> list[dict]:
    return accepts_reads_file("../data/operations.json")


def test_accepts_reads_file(receives_a_file):
    """Проверят, что объект список, а элементы словари и возвращает список словарей"""
    assert isinstance(receives_a_file, list) and all(isinstance(item, dict) for item in receives_a_file)


def test_file_not_found():
    """Проверяет,файл не найден,то возвращает пустой список"""
    result = accepts_reads_file("fs2dhkad.json")
    assert result == []


@pytest.mark.parametrize("data", ["str", 123, True, {"a:"}, [], [{"a": 1}, 123, "str"], [{"a": None}, {"b": ""}]])
@patch("json.load")
def incorrect_data(mock_json_load, data):
    """Проверяет, если в файле не список словарей,либо список пустой
    Возвращает пустой список
    """
    mock_json_load.return_value = data
    result = accepts_reads_file("name.json")
    assert result == []
