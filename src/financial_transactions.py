import csv
import json
from typing import Any, Dict, Hashable, List

import pandas as pd


def read_financial_transactions_csv(transaction_csv: str) -> List[Dict[Hashable, Any]]:
    """Читает CSV и возвращает список словарей"""
    list_transactions = []
    try:
        with open(transaction_csv, encoding="utf-8") as file:
            reader_file_csv = csv.DictReader(file, delimiter=";")
            for row in reader_file_csv:
                list_transactions.append(row)
                print(json.dumps(list_transactions, indent=4, ensure_ascii=False))
            return list_transactions
    except FileNotFoundError:
        print("Файл не найден")
        return []


def read_financial_transactions_xl(transaction_xl: str) -> List[Dict[Hashable, Any]]:
    """Читает xlsx и возващает список словаей"""
    try:
        df = pd.read_excel(transaction_xl)
        transactions_list = df.to_dict(orient="records")
        return transactions_list
    except FileNotFoundError:
        print("Файл не найден")
        return []


if __name__ == "__main__":
    transaction_csv = read_financial_transactions_csv(
        r"C:\Users\parov\PycharmProjects\PythonProject\transactions\transactions.csv"
    )
    print(json.dumps(transaction_csv, indent=4, ensure_ascii=False))

    transaction_xl = read_financial_transactions_xl(
        r"C:\Users\parov\PycharmProjects\PythonProject\transactions\transactions_excel.xlsx"
    )
    print(json.dumps(transaction_xl, indent=4, ensure_ascii=False))
