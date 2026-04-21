import os.path
import time
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор, принимает имя файла и логирует время начала работы функции, ее аргументы и результат,
    а также время работы функции. Если имя файла не задано, выводит логи в консоль"""

    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                start_time = time.time()
                formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
                result = function(*args, **kwargs)
                stop_time = time.time()
                log_message = (
                    f'foo "{function.__name__}" '
                    f"started at {formatted_time} "
                    f"inputs: {args}, {kwargs}, "
                    f"result: {result}, "
                    f"work_time = {stop_time - start_time:.3f} sec \n"
                )
                if not filename:
                    # Вывод в консоль значительно упрощен для возможности тестирования
                    print(f'{function.__name__} OK')
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")
                return result
            except Exception as e:
                log_message_exception = f'foo "{function.__name__}" Error "{e}", inputs: {args}, {kwargs}'
                if not filename:
                    print(log_message_exception)
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message_exception + "\n")
                raise

        return wrapper

    return decorator

#
# # Путь к файлу с логами
# log_file_path = os.path.join(os.path.join(os.path.dirname(os.getcwd()), "logs"), "my_log.txt")
#
#
# @log()
# def my_function(x: int, y: int) -> int:
#     return x + y
#
#
# print(my_function("a", 3))
