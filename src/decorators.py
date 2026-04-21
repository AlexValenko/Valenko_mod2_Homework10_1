import os.path
from functools import wraps
import time
from typing import Callable, Any, Tuple, Dict


def log(filename: str|None = None) -> Callable[[Any], Callable[[tuple[Any, ...], dict[str, Any]], None]]:
    """Декоратор, принимает имя файла и логирует время начала работы функции, ее аргументы и результат, а также время работы функции
    если имя файла не задано, выводит логи в консоль"""
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                start_time = time.time()
                formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
                result = function(*args, **kwargs)
                stop_time = time.time()
                log_message = f'foo \"{function.__name__}\" started at {formatted_time} inputs: {args}, {kwargs}, result: {result}, work_time = {stop_time - start_time:.7f} sec \n'
                if not filename:
                    print(log_message)
                else:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(log_message + '\n')
            except Exception as e:
                log_message_exception = f'foo \"{function.__name__}\" Error \"{e}\", inputs: {args}, {kwargs}'
                if not filename:
                    print(log_message_exception)
                else:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(log_message_exception + '\n')

        return wrapper
    return decorator

# Путь к файлу с логами
log_file_path = os.path.join(os.path.join(os.path.dirname(os.getcwd()), 'logs'), 'my_log.txt')

@log(log_file_path)
def my_function(x, y):
    return x + y

my_function(1, 2)

