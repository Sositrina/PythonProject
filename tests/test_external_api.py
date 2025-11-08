from unittest.mock import patch

from src.external_api import get_transaction_amount_in_rub

# Тест USD → RUB
with patch("src.external_api.requests.get") as mock_get:
    mock_get.return_value.json.return_value = {"rates": {"RUB": 100}}
    transaction_usd = {"operationAmount": {"amount": "10", "currency": {"code": "USD", "name": "доллар"}}}
    result = get_transaction_amount_in_rub(transaction_usd)
    assert result == 1000
    print("USD → RUB")

# Тест EUR → RUB
with patch("src.external_api.requests.get") as mock_get:
    mock_get.return_value.json.return_value = {"rates": {"RUB": 120}}
    transaction_eur = {"operationAmount": {"amount": "5", "currency": {"code": "EUR", "name": "евро"}}}
    result = get_transaction_amount_in_rub(transaction_eur)
    assert result == 600
    print("EUR → RUB")

# Тест RUB → RUB
transaction_rub = {"operationAmount": {"amount": "500", "currency": {"code": "RUB", "name": "руб."}}}
result = get_transaction_amount_in_rub(transaction_rub)
assert result == 500
print("RUB → RUB")


# Неправильная структура транзации
invalid_transaction = {"amount": "100"}
try:
    get_transaction_amount_in_rub(invalid_transaction)
except ValueError as e:
    print(e)

# Другая валюта
unsupported_currency = {"operationAmount": {"amount": "100", "currency": {"code": "GBP", "name": "фунт"}}}
try:
    get_transaction_amount_in_rub(unsupported_currency)
except ValueError as e:
    print(e)
