import pytest

from src.decorators import my_function


@pytest.fixture(autouse=True)
def clean_logfile() -> None:
    """Очищает лог-файл перед каждым тестом"""
    with open("mylog.txt", "w", encoding="utf-8") as f:
        f.write("")
    yield


def test_my_function_success() -> None:
    result = my_function(1, 2)
    assert result == 3

    with open("mylog.txt", encoding="utf-8") as f:
        log_text = f.read()

    assert log_text == ("Начало работы функции\n" "my_function ok\n" "Функция завершила работу\n")


def test_my_function_typeerror() -> None:
    result = my_function("a", 2)
    assert result is None

    with open("mylog.txt", encoding="utf-8") as f:
        log_text = f.read()

    assert "Начало работы функции\n" in log_text
    assert "my_function error: TypeError" in log_text
    assert "Inputs:" in log_text
    assert "('a', 2)" in log_text
    assert "Функция завершила работу\n" in log_text
