import json
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_hendler = logging.FileHandler("./logs/utils.log" 'w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_hendler.setFormatter(file_formatter)
logger.addHandler(file_hendler)


def load_operations(file_path: str = "data/operations.json") -> dict:
    """ Загружает транзакции из JSON-файла """
    try:
        logger.info("Загрузка файла операций...")
        with open(file_path, "r", encoding="utf-8") as f:
            operations = json.load(f)
        return operations  # type: ignore
    except (FileNotFoundError, ValueError, json.JSONDecodeError):
        logger.error("Произошла ошибка при загрузке файла операций")
        return []  # type: ignore
