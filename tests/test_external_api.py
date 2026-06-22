import unittest
from unittest.mock import Mock, patch

from src.external_api import get_operations


def test_get_operations_rub():
    # Тест для транзакции в рублях
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}
    result = get_operations(transaction)
    assert result == 100.0


@patch('requests.get')
def test_get_operations_usd(mock_get):
    # Тест для транзакции в долларах
    transaction = {
        'operationAmount': {
            'amount': '100.0',
            'currency': {'code': 'USD'}
        }
    }
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': {'RUB': 75.0}}
    mock_get.return_value = mock_response


def test_get_operations_eur():
    # Тест для транзакции в евро
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "EUR"}}}
    with patch("requests.get") as mock_get:
        # Настройка мок-ответа
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": {"RUB": 85.0}}
        mock_get.return_value = mock_response

        result = get_operations(transaction)
        assert result == 8500.0  # 100 * 85


def test_get_operations_invalid_currency():
    # Тест для транзакции с недопустимой валютой
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "GBP"}}}
    result = get_operations(transaction)
    assert result == 0.0


def test_get_operations_api_error():
    # Тест для обработки ошибки API
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}
    with patch("requests.get") as mock_get:
        # Настройка мок-ответа с ошибкой
        mock_response = Mock()
        mock_response.status_code = 500  # Ошибка сервера
        mock_get.return_value = mock_response

        result = get_operations(transaction)
        assert result == 0.0


def test_get_operations_invalid_amount():
    # Тест для обработки некорректной суммы
    transaction = {"operationAmount": {"amount": "invalid", "currency": {"code": "USD"}}}
    result = get_operations(transaction)
    assert result == 0.0


if __name__ == "__main__":
    unittest.main()
