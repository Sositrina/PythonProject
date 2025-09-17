import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def mask_card() -> str:
    """Возвращает замаскированный номер карты для теста"""
    return get_mask_card_number(7000792289606361)


def test_get_mask_card_number(mask_card: str) -> None:
    """
    Тестирует функцию get_mask_card_number на корректном номере карты
    Проверяет:
    - длину результата,
    - начало номера,
    - конец номера
    """
    assert len(mask_card) == 19
    assert mask_card.startswith("7000")
    assert mask_card.endswith("6361")


@pytest.mark.parametrize(
    "element",
    [
        0,
        12345678909042374986327,
    ],
)
def test_mask_card_wrong_number(element: int) -> None:
    """
    Тестирует на неверных значениях.
    Проверяет, что функция возвращает строку: 'Номер карты неверный'
    """
    expected = "Номер карты неверный"
    assert get_mask_card_number(element) == expected


@pytest.fixture
def mask_account() -> str:
    """Возвращает замаскированный номер счета для теста."""
    return get_mask_account(73654108430135874305)


def test_get_mask_account(mask_account: str) -> None:
    """
    Тестирует функцию на корректном номере счета.
    Проверяет, что длина замаскированного номера равна 6 символам.
    """
    assert len(mask_account) == 6


@pytest.mark.parametrize("element", [0, 12345678909042374986327])
def test_mask_account_wrong(element: int) -> None:
    """Тестирует на неверных значениях.
    Проверяет, что функция возвращает строку: 'Номер счета неверный'
    """
    expected = "Номер счета неверный"
    assert get_mask_account(element) == expected