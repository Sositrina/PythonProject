def log(filename=None):
    """
    Декоратор логирования
    Если filename указан, то логи пишутся в файл
    Если не указан, то логи выводятся в консоль
    """

    def decorator(func):
        """Принимает исходную функцию и возвращает функцию wrapper"""
        def wrapper(*args, **kwargs):
            """Принимает аргументы исходной функции"""
            def write_log(text):
                """Проверяет,если файл указан, то записывает текст в файл
                   Если не указан, то текст выводится в консоль"""
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(text)
                else:
                    print(text, end="")
            try:
                write_log("Начало работы функции\n")
                result = func(*args, **kwargs)
                write_log(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                    write_log(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
            finally:
                    write_log("Функция завершила работу\n")

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Принимает 2 аргумента и возвращает сложение"""
    return x + y


my_function(1, 2)
