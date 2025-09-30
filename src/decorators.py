def log(filename="mylog.txt"):
    """
    Декоратор логирования
    Логи всегда пишутся в в файл mylog.txt
    """

    def decorator(func):
        """Принимает исходную функцию и возвращает функцию wrapper"""

        def wrapper(*args, **kwargs):
            """ """
            try:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write("Начало работы функции\n")
                result = func(*args, **kwargs)
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
            finally:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write("Функция завершила работу\n")

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Принимает 2 аргумента и возвращает сложение"""
    return x + y


my_function(1, 2)
