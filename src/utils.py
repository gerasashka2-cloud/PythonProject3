import json
import logging
from typing import Union

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_hendler = logging.FileHandler("./logs/utils.log" 'w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_hendler.setFormatter(file_formatter)
logger.addHandler(file_hendler)


def load_operations(file_path: str) -> Union[dict, list]:
    """ Загружает транзакции из JSON-файла """
    try:
        logger.info("Загрузка файла операций...")
        with open(file_path, "r", encoding="utf-8") as f:
            operations = json.load(f)
        return operations
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        logger.error(f"Произошла ошибка при загрузке файла операций: {e}")
        return []
