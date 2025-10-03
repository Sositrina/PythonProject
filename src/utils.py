import json


def accepts_reads_file(path: str) -> list[dict]:
    """
    Читает файл.
    Если файла нет,либо он пустой,либо не список- возвращает пустой список
    При успешном чтении возвращает список словарей
    """
    try:
        with open(path, encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print("Ошибка декодирования JSON:", e)
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []
    if not isinstance(data, list) or not data:
        return []
    else:
        return data


if __name__ == "__main__":
    print(accepts_reads_file("../data/operations.json"))
