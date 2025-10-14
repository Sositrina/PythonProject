import logging

logger = logging.getLogger(__name__)  # логер с именем модуля
file_handler = logging.FileHandler("../logs/masks_logs.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")  # формат записи логов
file_handler.setFormatter(file_formatter)  # установка формата для хендлера
logger.addHandler(file_handler)  # добавляет хендлер к логам
logger.setLevel(logging.DEBUG)  # уровень логирования


def get_mask_card_number(card_number: int) -> str:
    """Принимает номер карты и возвращает замаскированный номер карты"""
    logger.info("Начало работы")
    logger.info("Проверка номера карты")
    str_card_number = str(card_number)
    if len(str_card_number) != 16:
        logger.error("Номер карты неверный")
        return "Ошибка: номер карты неверный"
    logger.info("Номер карты прошел проверку успешно")
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[12:]}"


def get_mask_account(account_number: int) -> str:
    """Принимает номер счета и возвращает замаскированный номер счета"""
    logger.info("Проверка номера счета")
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        logger.error("Номер счета неверный")
        return "Ошибка: номер счет неверный"
    logger.info("Номер счет прошел проверку успешно")
    logger.info("Конец работы")
    return f"**{str_account_number[-4:]}"


masked_card = get_mask_card_number(7000792289606361)
masked_count = get_mask_account(73654108430135874305)
print(masked_card)
print(masked_count)
