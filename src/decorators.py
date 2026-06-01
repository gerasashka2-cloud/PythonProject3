from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор , который  логирует  начало и конец выполнения функции, ее результаты или возникшие ошибки.
    Должен принимать необязательный аргумент 'filename', который определяет,
    куда будут записываться логи (в файл или в консоль)
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            try:
                result = func(*args, **kwargs)
                message = f"{func_name} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                error_message = f"{func_name} error: {e}." f"Inputs: args{args}, kwargs{kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)

        return wrapper

    return decorator

# Пример 1: Логирование в файл `mylog.txt`
@log(filename="mylog.txt")
def add(a, b):
    return a + b


add(3, 5)  # В mylog.txt будет записано: "add ok"
add(
    3, "5"
)  # В mylog.txt будет записано: "add error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: args(3, '5'), kwargs{}"


# Пример 2: Логирование в файл `mylog.txt`
@log(filename="mylog.txt")
def multiply(a, b):
    return a * b


multiply(4, 2)  # В mylog.txt будет записано: "multiply ok"
multiply(
    4, "a"
)  # В mylog.txt будет записано: "multiply error: can't multiply sequence by non-int of type 'str'. Inputs: args(4, 'a'), kwargs{}"


# Пример 3: Логирование нескольких функций в `mylog.txt`
@log(filename="mylog.txt")
def divide(a, b):
    return a / b


@log(filename="mylog.txt")
def subtract(a, b):
    return a - b


divide(10, 2)  # В mylog.txt будет записано: "divide ok"
subtract(10, 5)  # В mylog.txt будет записано: "subtract ok"
subtract(
    10, "5"
)  # В mylog.txt будет записано: "subtract error: unsupported operand type(s) for -: 'int' and 'str'. Inputs: args(10, '5'), kwargs{}"


### Пример 4: Логирование без параметров в `mylog.txt`
@log(filename="mylog.txt")
def greet(name):
    return f"Hello, {name}!"


greet("Alice")  # В mylog.txt будет записано: "greet ok"
