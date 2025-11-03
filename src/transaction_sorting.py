from datetime import datetime
from typing import List, Dict, Any


def process_transactions(transactions: List[Dict[str, Any]]) -> None:
    """Обрабатывает список транзакций: сортировка, фильтры и вывод."""

    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    sort_date = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_date == "да":
        order = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        ascending = order == "по возрастанию"
        transactions.sort(
            key=lambda t: datetime.strptime(t.get("date", "")[:19], "%Y-%m-%dT%H:%M:%S"),
            reverse=not ascending,
        )

    rubles_only = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if rubles_only == "да":
        transactions = [
            t for t in transactions
            if t.get("currency", {}).get("code", "").upper() in ["RUB", "РУБ."]
        ]

    keyword_filter = input(
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
    ).strip().lower()

    if keyword_filter == "да":
        keyword = input("Программа: Введите ключевое слово для фильтрации:\nПользователь: ").strip().lower()
        if keyword:
            transactions = [t for t in transactions if keyword in t.get("description", "").lower()]

    print("\nПрограмма: Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(transactions)}\n")

    for t in transactions:
        date = t.get("date", "")[:10]
        description = t.get("description", "Нет описания")

        from_acc = t.get("from", "")
        to_acc = t.get("to", "")

        if from_acc and to_acc:
            accounts_info = f"{from_acc} -> {to_acc}"
        else:
            accounts_info = from_acc or to_acc or ""

        amount = t.get("amount") or t.get("operationAmount", {}).get("amount", "???")
        currency = t.get("currency", {}).get("name") or t.get("operationAmount", {}).get("currency", {}).get("name", "???")

        print(f"{date} {description}")
        if accounts_info:
            print(accounts_info)
        print(f"Сумма: {amount} {currency}\n")
