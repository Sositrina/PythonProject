from typing import Dict, List

import pytest

from src.generators import filter_by_currency, transaction_descriptions


def test_filter_by_currency() -> None:
    transactions = [
        {"operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}},
        {"operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}}},
    ]
    usd_transactions = filter_by_currency(transactions, "USD")
    first_transactions = next(usd_transactions)
    assert first_transactions["operationAmount"]["currency"]["name"] == "USD"


@pytest.mark.parametrize(
    "transactions",
    [
        [{"operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "USD"}}}],
        [{"operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "USD"}}}],
        [{"operationAmount": {"amount": "79114.93", "currency": {"name": "", "code": "USD"}}}],
        [{"operationAmount": {"amount": "79114.93", "currency": {"name": "asdasd", "code": "USD"}}}],
        [{"operationAmount": {"amount": "79114.93", "currency": {"name": "", "123123": "USD"}}}],
        [{"operationAmount": {"amount": "9824.07", "currency": {"name": "", "code": "USD"}}}],
        [{"operationAmount": {"amount": "9824.07", "currency": {"name": "аоывао", "code": "USD"}}}],
        [{"operationAmount": {"amount": "9824.07", "currency": {"name": "7328", "code": "USD"}}}],
        [{"operationAmount": {"amount": "9824.07"}}],
        [{"operationAmount": {"amount": "79114.93"}}],
        [{"operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "EUR"}}}],
        [{"operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "RUB"}}}],
        [{"operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "EUR"}}}],
        [{"operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "RUB"}}}],
    ],
)
def test_incorrect_currency(transactions: List[Dict]) -> None:
    with pytest.raises(StopIteration):
        next(filter_by_currency(transactions, "USD"))


def test_empty_transactions() -> None:
    with pytest.raises(StopIteration):
        next(filter_by_currency([], "USD"))


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]


@pytest.mark.parametrize(
    "transactions_input, expected_descriptions",
    [
        (transactions, ["Перевод организации", "Перевод со счета на счет"]),
        ([], []),
        ([{"description": "Тестовая транзакция"}], ["Тестовая транзакция"]),
    ],
)
def test_transaction_descriptions_param(transactions_input: List[Dict], expected_descriptions: List[str]) -> None:
    descriptions_iter = transaction_descriptions(transactions_input)
    results = []
    for _ in range(len(expected_descriptions)):
        results.append(next(descriptions_iter))
    assert results == expected_descriptions
