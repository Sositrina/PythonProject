import json
def accepts_reads_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    if not isinstance(data, list) or not data:
        return []
    else:
        return data



if __name__ == "__main__":
    print(accepts_reads_file("../data/operations.json"))
