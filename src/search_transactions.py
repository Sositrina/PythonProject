import json
import re
from collections import Counter

from src.financial_transactions import read_financial_transactions_csv, read_financial_transactions_xl


# Поиск определенных транзакций
def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Возвращает список словарей по ключу через поиск,если таких значений нет-возвращает пустой список"""
    if not isinstance(data, list):
        return []

    if not isinstance(search, str):
        raise ValueError("search должен быть строкой")

    result = []
    for transaction in data:
        if not isinstance(transaction, dict):
            continue

        desc = str(transaction.get("description", ""))  # None -> ''
        if re.search(search, desc, flags=re.IGNORECASE):
            result.append(transaction)
    return result


# Подсчет банковских операций
def counts_transactions(list_transactions: list[dict], categories: list) -> dict:
    """Возвращает названия категорий(ключ),количество операций(значение)"""
    counter: Counter[str] = Counter()
    for transaction in list_transactions:
        if not isinstance(transaction, dict):
            continue

        desc = str(transaction.get("description", "")).strip()
        if any(category in desc for category in categories):
            counter[desc] += 1
    return dict(counter)


if __name__ == "__main__":
    # Объединение списков
    transactions_csv = read_financial_transactions_csv("../transactions/transactions.csv")
    transactions_xlsx = read_financial_transactions_xl("../transactions/transactions_excel.xlsx")
    merge_list = transactions_csv + transactions_xlsx

    # Категории для фильтрации
    text = ["Перевод", "Открытие"]
    pattren = "|".join(text)

    # Фильтрация и считывание
    filtered = process_bank_search(merge_list, pattren)
    result = counts_transactions(filtered, text)

    print(json.dumps(result, ensure_ascii=False, indent=4))
