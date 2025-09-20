import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def mask_card() -> str:
    """Возвращает замаскированный номер карты"""
    return mask_account_card("Visa Platinum 7000792289606361")


def test_mask_card_compare(mask_card: str) -> None:
    """
    Проверяет правильность замаскированного номера карты.
    Проверяет длину  строки
    """
    assert mask_card == "Visa Platinum 7000 79** **** 6361"
    assert len(mask_card) == 33


@pytest.mark.parametrize(
    "card_wrong", ["", "VisaPlatinum700079******6361", "Visa Platinum", "7000 79** **** 6361", "43246764"]
)
def test_card_wrong(card_wrong: str) -> None:
    """
    Проверяет функцию  на некорректных данных.
    Все неверные значения должны возвращать строку "Неверные данные"
    """
    assert mask_account_card(card_wrong) == "Неверные данные"


@pytest.fixture
def data_right() -> str:
    """Возвращает корректную дату в ISO-формате."""
    return "2024-03-11T02:26:18.671407"


def test_get_date_correct_format(data_right: str) -> None:
    """
    Проверяет правильное преобразование даты из ISO-формата в 'ДД.ММ.ГГГГ'.
    """
    result = get_date(data_right)
    assert result == "11.03.2024"
    assert len(result) == 10


@pytest.mark.parametrize(
    "wrong_date",
    [
        "",
        "2024-13-01T00:00:00",
        "2024-02-30T12:00:00",
        "fsdfjkdjf",
        "Счет 73654108430135874305",
        "2024/03/11",
    ],
)
def test_get_date_wrong_formats(wrong_date: str) -> None:
    """
    Проверяет функцию на некорректные форматы даты.
    Функция должна возвращать строку 'Такой даты несуществует'.
    """
    assert get_date(wrong_date) == "Такой даты несуществует"


@pytest.mark.parametrize(
    "boundary_date, expected",
    [
        ("2020-02-29T00:00:00", "29.02.2020"),
        ("2000-01-01T23:59:59", "01.01.2000"),
        ("1999-12-31T23:59:59", "31.12.1999"),
    ],
)
def test_get_date_boundary_cases(boundary_date: str, expected: str) -> None:
    """
    Проверяет граничные случаи корректных дат.
    """
    assert get_date(boundary_date) == expected
