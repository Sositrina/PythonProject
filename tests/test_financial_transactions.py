from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.financial_transactions import read_financial_transactions_csv, read_financial_transactions_xl

# Тест на правильный CSV
csv_fake_file = (
    "id;state;date;amount;currency_name;currency_code;from;to;description\n"
    "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
    "Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации"
)


@patch("builtins.open", new_callable=mock_open, read_data=csv_fake_file)
def test_read_financial_transactions_csv_fake(mock_file: Any) -> None:
    result = read_financial_transactions_csv("fake_file.csv")
    expected_result: list[dict[str, Any]] = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    assert result == expected_result


# Тест на пустой CSV
csv_empty_file = "id;state;date;amount;currency_name;currency_code;from;to;description"


@patch("builtins.open", new_callable=mock_open, read_data=csv_empty_file)
def test_read_financial_transactions_csv_empty(mock_file: Any) -> None:
    result = read_financial_transactions_csv("empty_file.csv")
    expected_result: list = []
    assert result == expected_result


# Тест на отсутствие файла CSV
@patch("builtins.open")
def test_read_financial_transactions_file_not_found(mock_file: Any) -> None:
    mock_file.side_effect = FileNotFoundError
    result = read_financial_transactions_csv("random_file.csv")
    assert result == []


# Тест на правильный xlsx
df_fake = pd.DataFrame(
    [
        {
            "id": 4137938.0,
            "state": "EXECUTED",
            "date": "2023-01-04T13:13:34Z",
            "amount": 15560.0,
            "currency_name": "Real",
            "currency_code": "BRL",
            "from": None,
            "to": "Счет 38164279390569873521",
            "description": "Открытие вклада",
        },
        {
            "id": 4699552.0,
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "amount": 23423.0,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        },
    ]
)


@patch("pandas.read_excel")
def test_read_financial_transactions_xl(mock_read_excel: Any) -> None:
    mock_read_excel.return_value = df_fake
    expected_result = df_fake.to_dict(orient="records")

    result = read_financial_transactions_xl("fake_file.xlsx")

    assert result == expected_result


# Тест на ошибку
@patch("pandas.read_excel")
def test_read_financial_transactions_xl_file_not_found(mock_read_excel: Any) -> None:
    mock_read_excel.side_effect = FileNotFoundError
    result = read_financial_transactions_xl("not_file.xlsx")
    assert result == []


# Тест на пустой файл

df_empty = pd.DataFrame([])


@patch("pandas.read_excel")
def test_read_financial_transactions_empty(mock_read_excel: Any) -> None:
    mock_read_excel.return_value = df_empty
    result = read_financial_transactions_xl("empty_file.xlsx")
    assert result == []
