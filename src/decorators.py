def log(filename="mylog.txt"):
    """
    Описание декоратора:
        принимает необязательный аргумент filename="mylog.txt"
        определяет куда записывать логи(в файл или консоль)
        если filename задан, логи записываются в указанный файл
        если filename не задан, логи выводятся в консоль
    Функциональность декоратора:
        автоматически логирует начало работы  и конец работы функции
        если ошибка, то вывод в лог-файл:
            my_function error: TypeError. Inputs: {args}, {kwargs}
        если нет ошибок, то вывод в лог-файл:
            my_function ok
    """
    def decorator(func):
        """Принимает исходную функцию и возвращает функцию wrapper"""
        def wrapper(*args, **kwargs):
            """
            Функция принимает на вход 2 аргумента исходной функции
            Записывает текст о начале работы функции в файл mylog.txt
            Для обработки ошибки, вызызвается исходная функция с аргументами в блоке try/except
            В блоке try/except обрабатывается ошибка TypeError и записывается в файл mylog.txt с текстом:
               имя_функции: тип ошибки: входные данные
            Записывает в файл mylog.txt текст о завершении работы
            Если результат завершился успешно, то в файл mylog.txt записывается текст: my_function ok
            Записывает в файл mylog.txt текст о завершении работы
            Возвращает результат
            """
            with open(filename, "a", encoding="utf-8") as file:
                file.write("Начало работы функции\n")
            try:
                result = func(*args, **kwargs)
            except TypeError:
                with open(filename, "a") as file:
                    file.write(f"my_function error: TypeError. Inputs: {args}, {kwargs}\n")
                with open(filename, "a", encoding="utf-8") as file:
                    file.write("Функция завершила работу\n")
            else:
                with open(filename, "a") as file:
                    file.write("my_function ok\n")
                with open(filename, "a", encoding="utf-8") as file:
                    file.write("Функция завершила работу\n")
                return result
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """Принимает 2 аргумента и возвращает сложение"""
    return x + y

my_function(1, 2)
