import os
import json
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # путь к src
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")         # путь к папке logs
os.makedirs(LOG_DIR, exist_ok=True)                   # создаём папку, если нет

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(os.path.join(LOG_DIR, "utils_logs.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


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
