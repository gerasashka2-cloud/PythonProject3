import json


def load_operations(file_path: str = "data/operations.json") -> dict:
    """ Загружает транзакции из JSON-файла """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            operations = json.load(f)
        return operations  # type: ignore
    except (FileNotFoundError, ValueError, json.JSONDecodeError):
        return []  # type: ignore
