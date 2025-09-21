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
        currency_info = transaction.get("operationAmount", {}).get("currency", {})
        if (
                currency_info.get("name") == currency
                and currency_info.get("code") == currency
        ):
            yield transaction


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    try:
        print(next(usd_transactions))
    except StopIteration:
        break


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
for _ in range(5):
    try:
        print(next(descriptions))
    except StopIteration:
        break


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Принимает:
    - start: целое число, начальное значение диапазона
    - stop: целое число, конечное значение диапазона включительно
    Описание:
    - перебирает числа от start до stop включительно
    - преобразует числа в строку длинной 16 с ведущими нулями
    - преобразует строку в формат XXXX XXXX XXXX XXXX
    - возвращает номера в карты по однйо строке
    """
    for number in range(start, stop + 1):
        number_str = str(number).zfill(16)
        correct_format = f"{number_str[0:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
        yield correct_format


for card_number in card_number_generator(1, 5):
    print(card_number)
