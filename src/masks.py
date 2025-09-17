def get_mask_card_number(card_number: int) -> str:
    """Принимает номер карты и возвращает замаскированный номер карты"""
    str_card_number = str(card_number)
    if len(str_card_number) == 16:
        return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[12:]}"
    else:
        return "Номер карты неверный"


def get_mask_account(account_number: int) -> str:
    """Принимает номер счета и возвращает замаскированный номер счета"""
    str_account_number = str(account_number)
    if len(str_account_number) == 20:
        return f"**{str_account_number[-4:]}"
    else:
        return "Номер счета неверный"


masked_card = get_mask_card_number(7000792289606361)
masked_count = get_mask_account(73654108430135874305)
