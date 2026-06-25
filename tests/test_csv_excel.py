import unittest
from unittest.mock import Mock, patch

from src.csv_excel import read_transactions_from_csv, read_transactions_from_excel


@patch("os.path.exists")
@patch("pandas.read_csv")
def test_read_transactions_from_csv_success(mock_read_csv, mock_exists):
    # Тест для успешного чтения CSV файла
    mock_exists.return_value = True
    mock_df = Mock()
    mock_df.empty = False
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mock_read_csv.return_value = mock_df

    transactions = read_transactions_from_csv("path/to/file.csv")
    assert transactions == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]


@patch("os.path.exists")
def test_read_transactions_from_csv_file_not_found(mock_exists):
    # Тест для случая, когда файл не найден
    mock_exists.return_value = False

    try:
        read_transactions_from_csv("path/to/file.csv")
    except FileNotFoundError:
        pass  # Ожидаем ошибку, ничего не делаем
    else:
        assert False, "FileNotFoundError не была вызвана"


@patch("os.path.exists")
@patch("pandas.read_csv")
def test_read_transactions_from_csv_empty_file(mock_read_csv, mock_exists):
    # Тест для пустого CSV файла
    mock_exists.return_value = True
    mock_df = Mock()
    mock_df.empty = True
    mock_read_csv.return_value = mock_df

    try:
        read_transactions_from_csv("path/to/file.csv")
    except ValueError:
        pass  # Ожидаем ошибку, ничего не делаем
    else:
        assert False, "ValueError не была вызвана"


@patch("os.path.exists")
@patch("pandas.read_excel")
def test_read_transactions_from_excel_success(mock_read_excel, mock_exists):
    # Тест для успешного чтения Excel файла
    mock_exists.return_value = True
    mock_df = Mock()
    mock_df.empty = False
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mock_read_excel.return_value = mock_df

    transactions = read_transactions_from_excel("path/to/file.xlsx")
    assert transactions == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]


@patch("os.path.exists")
def test_read_transactions_from_excel_file_not_found(mock_exists):
    # Тест для случая, когда файл не найден
    mock_exists.return_value = False

    try:
        read_transactions_from_excel("path/to/file.xlsx")
    except FileNotFoundError:
        pass  # Ожидаем ошибку, ничего не делаем
    else:
        assert False, "FileNotFoundError не была вызвана"


@patch("os.path.exists")
@patch("pandas.read_excel")
def test_read_transactions_from_excel_empty_file(mock_read_excel, mock_exists):
    # Тест для пустого Excel файла
    mock_exists.return_value = True
    mock_df = Mock()
    mock_df.empty = True
    mock_read_excel.return_value = mock_df

    try:
        read_transactions_from_excel("path/to/file.xlsx")
    except ValueError:
        pass  # Ожидаем ошибку, ничего не делаем
    else:
        assert False, "ValueError не была вызвана"


if __name__ == "__main__":
    unittest.main()
