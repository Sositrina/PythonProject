from unittest.mock import patch
from src.external_api import get_transaction_amount_in_rub

# Тест USD → RUB
with patch("src.external_api.requests.get") as mock_get:
    mock_get.return_value.json.return_value = {"rates": {"RUB": 100}}
    transaction = {"amount": 10, "currency": "USD"}
    result = get_transaction_amount_in_rub(transaction)
    assert result == 1000
    print("USD → RUB PASS")

# Тест EUR → RUB
with patch("src.external_api.requests.get") as mock_get:
    mock_get.return_value.json.return_value = {"rates": {"RUB": 120}}
    transaction = {"amount": 5, "currency": "EUR"}
    result = get_transaction_amount_in_rub(transaction)
    assert result == 600
    print("EUR → RUB PASS")

# Тест RUB → RUB
transaction = {"amount": 500, "currency": "RUB"}
result = get_transaction_amount_in_rub(transaction)
assert result == 500
print("RUB → RUB PASS")
