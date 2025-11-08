import os
import logging


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(os.path.join(LOG_DIR, "masks_logs.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Принимает номер карты и возвращает замаскированный номер карты"""
    logger.info("Начало работы")
    logger.info("Проверка номера карты")
    str_card_number = str(card_number)
    if len(str_card_number) != 16:
        logger.error("Номер карты неверный")
        return "Ошибка: Номер карты неверный"
    logger.info("Номер карты прошел проверку успешно")
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[12:]}"


def get_mask_account(account_number: int) -> str:
    """Принимает номер счета и возвращает замаскированный номер счета"""
    logger.info("Проверка номера счета")
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        logger.error("Номер счета неверный")
        return "Ошибка: Номер счета неверный"
    logger.info("Номер счета прошел проверку успешно")
    logger.info("Конец работы")
    return f"**{str_account_number[-4:]}"


masked_card = get_mask_card_number(7000792289606361)
masked_count = get_mask_account(73654108430135874305)
#print(masked_card)
#print(masked_count)
