from typing import Dict, Iterator, List

# Список словарей
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


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Принимает:
    - transactions: список словарей с информацией о транзакциях
    - currency: валюта в виде строки
    Описание:
     - перебирает список словарей
     - возвращает по одному только те, у которых валюта 'USD'
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Принимает:
    - список словарей
    Описание:
    - перебирает список словарей
    - возвращает значение по ключу 'description'
    """
    for transaction in transactions:
        yield transaction["description"]


descriptions = transaction_descriptions(transactions)
for _ in range(2):
    print(next(descriptions))
