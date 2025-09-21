import pytest
from src.generators import filter_by_currency


def test_filter_by_currency():
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
        [{"operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "RUB"}}}]


    ],
)
def test_incorrect_currency(transactions):
    with pytest.raises(StopIteration):
        next(filter_by_currency(transactions, "USD"))

def test_empty_transactions():
    with pytest.raises(StopIteration):
        next(filter_by_currency([], "USD"))
