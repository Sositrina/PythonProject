import os

import requests
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")


def get_transaction_amount_in_rub(transaction: dict) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях (float)
    Если транзакция в USD или EUR — обращается к Exchange Rates Data API для конвертации
    """
    if not isinstance(transaction, dict):
        raise TypeError("transaction должен быть словарём")

    if (
        "operationAmount" not in transaction
        or "amount" not in transaction["operationAmount"]
        or "currency" not in transaction["operationAmount"]
        or "code" not in transaction["operationAmount"]["currency"]
    ):
        raise ValueError("Некорректная структура транзакции")

    amount = float(transaction["operationAmount"]["amount"])
    currency = str(transaction["operationAmount"]["currency"]["code"]).upper()

    if currency == "RUB":
        return amount

    if currency not in ("USD", "EUR"):
        raise ValueError("Поддерживаются только валюты RUB, USD и EUR")

    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"

    response = requests.get(url, headers={"apikey": API_KEY})
    data = response.json()

    try:
        rate = data["rates"]["RUB"]
    except KeyError:
        raise ValueError("Ответ API не содержит курса RUB")

    amount_rub = amount * float(rate)
    return round(amount_rub, 2)


if __name__ == "__main__":
    transaction_usd = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }

    print(get_transaction_amount_in_rub(transaction_usd))
