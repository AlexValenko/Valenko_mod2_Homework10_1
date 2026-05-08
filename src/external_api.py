import requests
import os
from dotenv import load_dotenv

def get_amount_transaction_rub(transaction:dict) -> float|None:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        rub_amount = float(transaction["operationAmount"]["amount"])
        return rub_amount
    else:
        valuta = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        try:
            rub_amount = round(float(get_amount_rub(valuta, amount)),2)
        except TypeError:
            print("Conversion was not successful")
            return None
        return rub_amount

def get_amount_rub(valuta:str, amount:str) -> float|None:
    url_converter = "https://api.apilayer.com/exchangerates_data/convert"
    load_dotenv()
    apikey = os.getenv('API_KEY')
    headers = {"apikey":apikey}
    payload = {"to":"RUB",
               "from":valuta,
               "amount":amount}
    try:
        response = requests.get(url_converter, headers=headers, params=payload)
    except requests.exceptions.ConnectionError:
        print("Connection Error. Please check your network connection.")
        return None
    except requests.exceptions.RequestException:
        print("An error occurred. Please try again later.")
        return None
    status_code = response.status_code
    result_exchange = response.json()
    rub_amount_exchanged = result_exchange["result"]
    if status_code == 200:
        return rub_amount_exchanged
    else:
        return None


example_response = {
  "date": "2018-02-22",
  "historical": "",
  "info": {
    "rate": 148.972231,
    "timestamp": 1519328414
  },
  "query": {
    "amount": 25,
    "from": "GBP",
    "to": "JPY"
  },
  "result": 3724.305775,
  "success": True
}
