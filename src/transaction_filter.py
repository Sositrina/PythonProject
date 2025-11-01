from datetime import datetime
from typing import List, Dict, Any

def process_transactions(transactions):
    """Обрабатывает список транзакций: сортировка, фильтры и вывод."""
    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    sort_date = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_date == "да":
        order = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        ascending = order == "по возрастанию"
        transactions = sorted(
            transactions, key=lambda t: datetime.strptime(t["date"][:19], "%Y-%m-%dT%H:%M:%S"), reverse=not ascending
        )

    rubles_only = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if rubles_only == "да":
        transactions = [t for t in transactions if t["operationAmount"]["currency"]["code"] in ["RUB", "руб."]]

    keyword_filter = (
        input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ")
        .strip()
        .lower()
    )
    if keyword_filter == "да":
        keyword = input("Программа: Введите ключевое слово для фильтрации:\nПользователь: ").strip().lower()
        if keyword:
            transactions = [t for t in transactions if keyword in t.get("description", "").lower()]

    print("\nПрограмма: Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(transactions)}\n")

    for t in transactions:
        date = t["date"][:10]
        print(f"{date} {t['description']}")
        if "from" in t:
            print(t["from"])
        if "to" in t:
            print(t["to"])
        amount = t["operationAmount"]["amount"]
        currency = t["operationAmount"]["currency"]["name"]
        print(f"Сумма: {amount} {currency}\n")
