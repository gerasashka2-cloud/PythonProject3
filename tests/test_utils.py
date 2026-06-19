import json
import unittest
from unittest.mock import mock_open, patch

from src.utils import load_operations


def test_load_operations_success():
    # Тест успешной загрузки операций
    expected_result = [{"id": 1, "amount": 100}]
    with patch("builtins.open", new_callable=mock_open, read_data='[ { "id": 1, "amount": 100 } ]'):
        result = load_operations()
    assert result == expected_result


def test_load_operations_file_not_found():
    # Тест обработки ошибки FileNotFoundError
    with patch("builtins.open", new_callable=mock_open) as mock_file:
        mock_file.side_effect = FileNotFoundError
        result = load_operations()
    assert result == []


def test_load_operations_json_decode_error():
    # Тест обработки ошибки JSONDecodeError
    with patch("builtins.open", new_callable=mock_open, read_data="[ invalid json ]"):
        with patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0)):  # Имитация ошибки
            result = load_operations()
    assert result == []


if __name__ == "__main__":
    unittest.main()
