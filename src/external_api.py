import requests


API_KEY = "SKGj2KhrRW9cjfXqZHX8zzZIW1Bpboy5"

def get_transaction_amount_in_rub(transaction: dict) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях (float)
    Если транзакция в USD или EUR — обращается к Exchange Rates Data API для конвертации
    """
    if not isinstance(transaction, dict):
        raise TypeError("transaction должен быть словарём")

    if "amount" not in transaction or "currency" not in transaction:
        raise ValueError("Транзакция должна содержать ключи 'amount' и 'currency'")

    amount = float(transaction["amount"])
    currency = str(transaction["currency"]).upper()

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