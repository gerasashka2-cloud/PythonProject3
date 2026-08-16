import os

from pathlib import Path
from typing import Any, Dict, List, Optional

from src.process_bank import process_bank_operations, process_bank_search
from src.csv_excel import read_transactions_from_csv, read_transactions_from_excel

# Импорт функций из модулей проекта
from src.utils import load_operations
from src.widget import get_date, mask_account_card

# Фиксированные пути к файлам с данными
DATA_DIR: Path = Path(__file__).resolve().parent / "data"
FILE_PATHS: Dict[str, str] = {
    "json": str(DATA_DIR / "operations.json"),
    "csv": str(DATA_DIR / "transactions.csv"),
    "xlsx": str(DATA_DIR / "transactions_excel.xlsx"),
}

# Проверка наличия файлов
for file_type, file_path in FILE_PATHS.items():
    if not os.path.exists(file_path):
        print(f"Файл для {file_type} не найден: {file_path}")


def main() -> None:
    """Основная логика программы."""
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями. \n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    file_choice = get_user_choice("\nВаш выбор (1-3): ", ["1", "2", "3"])
    format_map = {"1": "json", "2": "csv", "3": "xlsx"}
    selected_format = format_map[file_choice]

    print(f"\nДля обработки выбран {selected_format.upper()}-файл.")

# 1. Загрузка данных
    transactions = read_transactions_wrapper(selected_format)
    if not transactions:
        print("Не удалось загрузить транзакции. Проверьте наличие и структуру файла.")
        return

    # 2. Фильтрация по статусу
    status = get_valid_status(["EXECUTED", "CANCELED", "PENDING"])
    if status:
        print(f'Операции отфильтрованы по статусу "{status}"')
        transactions = filter_by_status(transactions, status)

    # 3. Сортировка по дате
    if get_user_choice("\nОтсортировать операции по дате? Да/Нет: ", ["да", "нет"]) == "да":
        order = get_user_choice("Отсортировать по возрастанию или по убыванию? ", ["по возрастанию", "по убыванию"])
        transactions = sort_by_date(transactions, ascending=(order == "по возрастанию"))
        print(f"Операции отсортированы {'по возрастанию' if order == 'по возрастанию' else 'по убыванию'}")

    # 4. Фильтрация по валюте (RUB)
    if get_user_choice("\nВыводить только рублевые транзакции? Да/Нет: ", ["да", "нет"]) == "да":
        transactions = filter_by_currency(transactions)
        print("Отображаются только рублевые транзакции")

    # 5. Фильтрация по ключевому слову (используем process_bank_search)
    if (
        get_user_choice(
            "\nОтфильтровать список транзакций по определенному слову \nв описании? Да/Нет: ", ["да", "нет"]
        ) == "да"
    ):
        keyword = input("Введите слово для поиска: ").strip()
        if keyword:
            transactions = process_bank_search(transactions, keyword)
            print(f'Применена фильтрация по слову: "{keyword}"')

    # ПРОВЕРКА НА ПУСТУЮ ВЫБОРКУ
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши\nусловия фильтрации")
        return

    # 6. Опциональная аналитика (используем process_bank_operations)
    if get_user_choice("\nПоказать сводку по типам операций? Да/Нет: ", ["да", "нет"]) == "да":
        categories = list({tx.get("description") or tx.get("name", "Без категории") for tx in transactions})
        stats = process_bank_operations(transactions, categories)
        print("\nСводка по операциям:")
        for cat, count in sorted(stats.items(), key=lambda x: -x[1]):
            if count > 0:
                print(f"  • {cat}: {count}")

    # 7. Вывод результата
    print("\nРаспечатываю итоговый список транзакций...")
    print_transactions(transactions)


def get_user_choice(prompt: str, options: List[str]) -> str:
    """Запрашивает выбор пользователя из списка допустимых вариантов."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in [opt.lower() for opt in options]:
            return choice
        print(f"Неверный ввод. Доступные варианты: {', '.join(options)}")


def get_valid_status(available_statuses: List[str]) -> Optional[str]:
    """Запрашивает статус с валидацией и нормализацией регистра."""
    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. \n"
            f"Доступные для фильтровки статусы: {', '.join(available_statuses)}"
        )
        user_input = input().strip()
        normalized_input = user_input.upper()

        if normalized_input in available_statuses:
            return normalized_input
        else:
            print(f'Статус операции "{user_input}" недоступен.')


def filter_by_status(transactions: List[Dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    """Фильтрует транзакции по статусу."""
    return [t for t in transactions if str(t.get("state", "")).upper() == status]


def sort_by_date(transactions: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """Сортирует транзакции по дате."""

    def parse_date(tx: Dict[str, Any]) -> str:
        date_val = str(tx.get("date", ""))
        return date_val.split("T")[0] if "T" in date_val else date_val

    return sorted(transactions, key=parse_date, reverse=not ascending)


def filter_by_currency(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Фильтрует только рублевые транзакции."""
    filtered = []
    for t in transactions:
        amount_data = t.get("operationAmount", {})
        currency = ""
        if isinstance(amount_data, dict):
            curr_info = amount_data.get("currency", {})
            if isinstance(curr_info, dict):
                currency = str(curr_info.get("code", "") or curr_info.get("name", ""))
            else:
                currency = str(curr_info)
        else:
            currency = str(t.get("currency", ""))

        if currency.upper() in ["RUB", "RUR", "РУБ", "руб.", "рубль"]:
            filtered.append(t)
    return filtered


def format_amount(tx: Dict[str, Any]) -> str:
    """Извлекает и форматирует сумму с валютой."""
    amount = "0"
    currency = ""

    if "operationAmount" in tx:
        amount_data = tx.get("operationAmount", {})
        if isinstance(amount_data, dict):
            amount = amount_data.get("amount", "0")
            currency = amount_data.get("currency", {}).get("code", None)
    else:
        amount = tx.get("amount", "0")
        currency = tx.get("currency", None)

    if currency is None:
        return f"{amount}"

    currency_map = {
        "RUB": "руб.",
        "RUR": "руб.",
        "РУБ": "руб.",
        "руб.": "руб.",
        "рубль": "руб.",
        "USD": "USD",
        "EUR": "EUR",
        "GBP": "GBP",
    }

    return f"{amount} {currency_map.get(str(currency).upper(), currency)}"


def format_transaction(tx: Dict[str, Any]) -> str:
    """Форматирует одну транзакцию для вывода."""
    raw_date = tx.get("date", "")
    date_formatted = get_date(str(raw_date)) if raw_date else "Неизвестно"

    description = tx.get("description") or tx.get("name", "Без описания")

    accounts = []
    if tx.get("from"):
        accounts.append(mask_account_card(str(tx["from"])))
    if tx.get("to"):
        accounts.append(mask_account_card(str(tx["to"])))

    result = f"{date_formatted} {description}\n"
    if accounts:
        result += " -> ".join(accounts) + "\n"
    result += f"Сумма: {format_amount(tx)}"
    return result


def print_transactions(transactions: List[Dict[str, Any]]) -> None:
    """Выводит отформатированный список транзакций."""
    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")
    for i, tx in enumerate(transactions):
        print(format_transaction(tx))
        if i < len(transactions) - 1:
            print()


def read_transactions_wrapper(file_type: str) -> List[Dict[str, Any]]:
    """Загружает данные из фиксированного файла."""
    file_path = FILE_PATHS.get(file_type)
    if not file_path:
        return []
    try:
        if file_type == "json":
            return load_operations(file_path)
        elif file_type == "csv":
            return read_transactions_from_csv(file_path)
        elif file_type == "xlsx":
            return read_transactions_from_excel(file_path)
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return []
    return []


if __name__ == "__main__":
    main()
