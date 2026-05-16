import json
import logging

utils_logger = logging.getLogger("utils_logger")
utils_file_handler = logging.FileHandler(filename="logs/log_utils.log", mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s:%(filename)s:%(levelname)s:%(message)s")
utils_file_handler.setFormatter(file_formater)
utils_logger.addHandler(utils_file_handler)
utils_logger.setLevel(logging.DEBUG)


def get_fin_transactions(path_json: str) -> list[dict[str, str | dict[str, str]]]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    utils_logger.debug("Starting ...")
    try:
        with open(path_json, encoding="utf-8") as file:
            transactions_data = json.load(file)
            utils_logger.debug(f"Loading JSON data from {path_json}")
    except FileNotFoundError:
        print("File not Found")
        utils_logger.error(f"File {path_json} not Found")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON data.")
        utils_logger.error(f"Invalid JSON data in {path_json}. Exception JSONDecodeError")
        return []
    if not transactions_data:
        utils_logger.error(f"The list in {path_json} was empty")
        return []

    utils_logger.debug("Function was successfully finished")
    return transactions_data
