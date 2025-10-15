import json
import logging

# Настройка логирования
logger = logging.getLogger(__name__)  # логер с именем модуля
file_handler = logging.FileHandler("../logs/utils_logs.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")  # формат записи логов
file_handler.setFormatter(file_formatter)  # установка формата для хендлера
logger.addHandler(file_handler)  # добавляет хендлер к логам
logger.setLevel(logging.DEBUG)  # уровень логирования


def accepts_reads_file(path: str) -> list[dict]:
    """
    Читает файл.
    Если файла нет,либо он пустой,либо не список- возвращает пустой список
    При успешном чтении возвращает список словарей
    """
    try:
        logger.info("Открывается файл...")
        with open(path, encoding="utf-8") as f:
            logger.info("Проверка файла...")
            try:
                data = json.load(f)
                logger.info("Успешное открытие файла.")
            except json.JSONDecodeError as e:
                logger.error(f"Ошибка декодирования JSON: {e}")
                print("Ошибка декодирования JSON:", e)
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {path}")
        print("Файл не найден")
        return []
    if not isinstance(data, list) or not data:
        logger.warning("Файл пустой или содержит не список")
        return []
    else:
        return data


if __name__ == "__main__":
    print(accepts_reads_file("../data/operations.json"))
