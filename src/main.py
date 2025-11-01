from reading_files import get_transactions
from transaction_sorting import process_transactions
from typing import List, Dict


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")
    print(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    while True:
        try:
            choice: int = int(input("Введите число: "))
            if choice not in [1, 2, 3]:
                print("Ошибка: нужно ввести число 1, 2 или 3.")
                continue
            break
        except ValueError:
            print("Ошибка: нужно ввести число.")

    transactions = get_transactions(choice)
    if not transactions:
        print("Программа: Ошибка: не удалось загрузить данные.")
        return

    # Фильтрация по статусу
    valid_statuses: List[str] = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        user_status: str = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            )
            .strip()
            .upper()
        )
        if user_status in valid_statuses:
            break
        print(f'Статус операции "{user_status}" недоступен.\n')

    filtered: List[Dict] = [
        t for t in transactions
        if t.get("state", "").strip().upper() == user_status
    ]
    print(f'Операции отфильтрованы по статусу "{user_status}"')

    process_transactions(filtered)


if __name__ == "__main__":
    main()
