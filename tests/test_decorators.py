import os
import pytest
from src.decorators import my_function


@pytest.fixture(autouse=True)
def clean_logfile():
    """Автоматически очищает лог-файл перед каждым тестом"""
    if os.path.exists("mylog.txt"):
        os.remove("mylog.txt")
    yield
    if os.path.exists("mylog.txt"):
        os.remove("mylog.txt")


def test_my_function_success(capsys):
    """Проверяет успешное выполнение и запись в лог-файл"""
    result = my_function(1, 2)
    assert result == 3

    with open("mylog.txt", encoding="utf-8") as f:
        log_text = f.read()

    assert log_text == (
        "Начало работы функции\n"
        "my_function ok\n"
        "Функция завершила работу\n"
    )


def test_my_function_typeerror(capsys):
    """Проверяет обработку TypeError и запись в лог-файл"""
    result = my_function("a", 2)
    assert result is None

    with open("mylog.txt", encoding="utf-8") as f:
        log_text = f.read()

    assert "Начало работы функции\n" in log_text
    assert "my_function error: TypeError" in log_text
    assert "Inputs:" in log_text
    assert "('a', 2)" in log_text
    assert "Функция завершила работу\n" in log_text



