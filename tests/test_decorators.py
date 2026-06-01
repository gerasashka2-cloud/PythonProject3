import pytest

from src.decorators import log


# Тестируемый декоратор в отдельной функции
@log(filename=None)  # Декоратор для вывода на экран
def sample_function_success(a, b):
    return a + b


@log(filename=None)  # Декоратор для вывода на экран
def sample_function_error(a, b):
    return a / b


# Тестирование декоратора


def test_log_success(capsys):
    result = sample_function_success(3, 5)
    assert result == 8
    captured = capsys.readouterr().out  # Получаем вывод
    assert "sample_function_success ok" in captured


# Тестирование с записью в файл


def test_log_to_file(tmpdir):
    log_file = tmpdir.join("test_log.txt")  # Временный файл для логов

    @log(filename=str(log_file))
    def test_function(a, b):
        return a + b

    test_function(1, 2)

    # Проверяем, что в файл записано сообщение об успешном выполнении
    with open(log_file) as f:
        log_content = f.read()
        assert "test_function ok" in log_content
