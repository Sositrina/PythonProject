# Учебный проект

## Описание:

Учебный проект - это виджет, который показывает несколько последних успешных банковских операций клиента

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Sositrina/Project3
```
2. Установите виртуальное окружение:
```
python -m venv venv
```
3. Активируйте виртуальное окружение:
```
venv\Scripts\activate
```
4. Установите библиотеки:
```
pip install -r requirements
```
5. Проверьте установку библиотек:
```
pip list
```
6. Установите фреймворки:
```
poetry add --group dev pytest
```

## Функционал
В модуле masks:
- `get_mask_card_number` — маскирует номер банковской карты (16 цифр).
- `get_mask_account` — маскирует номер банковского счёта (20 цифр).

В модуле widget:
- `mask_account_card` — определяет, карта или счёт, и маскирует номер.
- `get_date` — преобразует дату в формат `ДД.ММ.ГГГГ`.

В модуле processing:
- `filter_by_state` — фильтрует список операций по статусу.
- `sort_by_date` — сортирует список операций по дате.

В модуле generators:
- `filter_by_currency` — возвращает транзакции у которых валюта USD
- Пример:
```
from generators import filter_by_currency

transactions = [
    {"operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}}},
    {"operationAmount": {"amount": "200", "currency": {"name": "EUR", "code": "EUR"}}},
]

usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:
    print(transaction) 
```
- `transaction_descriptions` — возвращает значение по ключу 'description'
- Пример:
```
from module_name import transaction_descriptions

transactions = [
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"},
]

descriptions = transaction_descriptions(transactions)

print(next(descriptions))  # 👉 "Перевод организации"
print(next(descriptions))
```
- `card_number_generator` — возвращает номера в карты формата XXXX XXXX XXXX XXXX
- Пример:
```
from src.generators import card_number_generator

cards = card_number_generator(1, 5)

print(next(cards))  
print(next(cards))  
print(next(cards))  
print(next(cards))  
print(next(cards))
```


## Тесты

- Тесты модуля `masks.py` пройдены на 100%
- Тесты модуля `widget.py` пройдены на 100%
- Тесты модуля `processing.py` пройдены на 100%
- Тесты модуля `generators.py` пройдены

Самостоятельная проверка тестов:

1. Установите pytest: `poetry add --group dev pytest`
2. `pytest/путь_к_файлу`- тест файла

Чтобы запустить тесты с оценкой покрытия, можно воспользоваться следующими командами:
1. `pytest --cov` - при активированном виртуальном окружении.
2. `poetry run pytest --cov` - через poetry.
3. `pytest --cov=src --cov-report=html` - чтобы сгенерировать отчет о покрытии в HTML-формате, где 
src
 — пакет c модулями, которые тестируем. Отчет будет сгенерирован в папке 
htmlcov
 и храниться в файле с названием 
index.html.