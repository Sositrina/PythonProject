from typing import Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency() -> None:
    """
    Проверяет транзакцию в USD
    Проверяет,что 'name' совпадает с USD
    """
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
    """
    Проверяет,что при несовпадении валюты генератор не возвращает элементов
    Ожидается StopIteration при вызове next()
    """
    with pytest.raises(StopIteration):
        next(filter_by_currency(transactions, "USD"))


def test_empty_transactions() -> None:
    """
    Генератор не возвращает значений
    Ожидается StopIteration
    """
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
    """
    Проверяет:
    - что возвращаются все описания транзакций
    - корректную обработку пустого списка
    - корректную работу с одним элементом
    """
    descriptions_iter = transaction_descriptions(transactions_input)
    results = []
    for _ in range(len(expected_descriptions)):
        results.append(next(descriptions_iter))
    assert results == expected_descriptions


def test_card_number_generator_range() -> None:
    """Проверяет, что генератор выдает все числа в диапазоне"""
    numbers = list(card_number_generator(1, 5))
    assert len(numbers) == 5
    assert numbers[0] == "0000 0000 0000 0001"
    assert numbers[1] == "0000 0000 0000 0002"
    assert numbers[2] == "0000 0000 0000 0003"
    assert numbers[3] == "0000 0000 0000 0004"
    assert numbers[4] == "0000 0000 0000 0005"


def test_card_number_generator_format() -> None:
    """Проверяет правильность формата номера"""
    numbers = list(card_number_generator(123, 123))
    assert numbers == ["0000 0000 0000 0123"]


def test_card_number_generator_large_number() -> None:
    """Проверяет корректность работы с большим числом"""
    numbers = list(card_number_generator(9999999999999999, 9999999999999999))
    assert numbers == ["9999 9999 9999 9999"]


def test_card_number_generator_empty() -> None:
    """Проверяет, когда диапазон пустой"""
    numbers = list(card_number_generator(5, 4))
    assert numbers == []
