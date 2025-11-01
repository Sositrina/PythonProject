def file_selection() -> int:
    """Запрашивает у пользователя тип файла и возвращает число 1–3."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

    actions = {
        1: "Для обработки выбран JSON-файл.",
        2: "Для обработки выбран CSV-файл.",
        3: "Для обработки выбран XLSX-файл."
    }

    while True:
        print(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )

        try:
            user_choice = int(input("Введите число: "))
            if user_choice not in actions:
                print("Неверно! Попробуйте снова.\n")
                continue
        except ValueError:
            print("Ошибка: нужно ввести число (1, 2 или 3).\n")
            continue

        print(actions[user_choice])
        return user_choice


def transaction_status() -> str:
    """Запрашивает статус транзакции и возвращает его в верхнем регистре."""
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        user_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).strip().upper()

        if user_input in valid_statuses:
            print(f'Операции отфильтрованы по статусу "{user_input}"')
            return user_input
        else:
            print(f'Статус операции "{user_input}" недоступен.\n')


if __name__ == "__main__":
    file_selection()
    transaction_status()