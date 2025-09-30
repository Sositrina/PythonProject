from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(props: str) -> str:
    """Обрабатывает информацию о карте и счете
    Возвращает строку с именем и максированным номером"""
    list_props = props.rsplit(maxsplit=1)
    if len(list_props) < 2:
        return "Неверные данные"

    card_name = list_props[0]  # название реквизитов
    number_props = list_props[1]  # цифры реквизитов
    if len(number_props) == 16:
        number_card_mask = get_mask_card_number(int(number_props))  # маска номера карты
        return f"{card_name} {number_card_mask}"
    if len(number_props) == 20:
        number_count_mask = get_mask_account(int(number_props))  # маска номера счета
        return f"{card_name} {number_count_mask}"
    else:
        return "Неверные данные"


def get_date(str_date: str) -> str:
    """Принимает строку с датой в формате '2024-03-11T02:26:18.671407'
    Возвращает строку с датой в формате 'ДД.ММ.ГГГГ'
    """
    try:
        dt = datetime.fromisoformat(str_date)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return "Такой даты несуществует"


print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
