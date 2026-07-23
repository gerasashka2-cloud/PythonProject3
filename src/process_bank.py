import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Возвращает список транзакций, в описании которых найдена указанная подстрока.
    Поиск выполняется с помощью регулярных выражений (регистронезависимо).
    """
    if not search:
        return data

    # re.escape экранирует спецсимволы, чтобы поиск работал как безопасная подстрока.
    # re.IGNORECASE делает поиск нечувствительным к регистру (стандарт для UI-поиска).
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    return [item for item in data if pattern.search(str(item.get("description", "")))]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Подсчитывает количество операций для каждой категории с использованием collections.Counter.

    :param data: Список словарей с банковскими операциями.
    :param categories: Список категорий для агрегации.
    :return: Словарь {категория: количество}
    """
    # Counter автоматически игнорирует отсутствующие ключи, возвращая 0
    counts = Counter(op.get("description") for op in data)

    # Формируем итоговый словарь строго в порядке переданных категорий
    return {cat: counts[cat] for cat in categories}
