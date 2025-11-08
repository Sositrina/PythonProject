from datetime import datetime
from typing import Dict, List


def filter_by_state(dictionaries: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Принимает список словарей и опционально значение для ключа state по умолчанию 'EXECUTED'
    Возвращает новый список словарей у которых ключ state со значением 'EXECUTED'"""
    if not dictionaries:
        raise ValueError("Список пуст")
    return [new_list for new_list in dictionaries if new_list["state"] == state]


dictionaries = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def sort_by_date(dictionaries: List[Dict], reverse: bool = True) -> List[Dict]:
    """Принимает список словарей и сортировку по умлочанию - убывание
    Возвращает  отсортированный список словарей по убиванию по ключу 'date'"""
    for item in dictionaries:
        try:
            datetime.fromisoformat(item["date"])
        except ValueError:
            raise ValueError("Неправильная дата")
    return sorted(dictionaries, key=lambda x: x["date"], reverse=reverse)


print(sort_by_date(dictionaries))
print(filter_by_state(dictionaries))
