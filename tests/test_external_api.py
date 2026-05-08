from unittest.mock import Mock, patch
import pytest
from requests.exceptions import RequestException, ConnectionError


from src.external_api import get_amount_transaction_rub, get_amount_rub

@pytest.fixture
def normal_transaction_rub():
    return {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

@pytest.fixture
def normal_transaction_usd():
    return {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

@pytest.fixture
def get_standard_response():
    return {
  "date": "2026-05-08",
  "info": {
    "rate": 74.651554,
    "timestamp": 1778222583
  },
  "query": {
    "amount": 200,
    "from": "USD",
    "to": "RUB"
  },
  "result": 14930.3108,
  "success": True
}

def test_get_amount_transaction_rub_valuta_rub(normal_transaction_rub):
    """Тест работы функции get_amount_transaction_rub с рублевой транзакцией на входе"""
    assert get_amount_transaction_rub(normal_transaction_rub) == 31957.58

@patch('src.external_api.get_amount_rub')
def test_get_amount_transaction_rub_valuta_usd(mock_rub, normal_transaction_usd):
    """Тест работы функции get_amount_transaction_rub с валютной транзакцией на входе
    Результат работы функции get_amount_rub, которая обращается по api подменен на 100,00"""
    mock_rub.return_value = 100.00
    assert get_amount_transaction_rub(normal_transaction_usd) == 100.00
    mock_rub.assert_called_once()

@patch('src.external_api.get_amount_rub')
def test_get_amount_transaction_rub_none_api_request(mock_rub, normal_transaction_usd, capsys: pytest.CaptureFixture[str]):
    """Тест работы функции get_amount_transaction_rub с валютной транзакцией на входе
    Функция get_amount_rub, которая обращается по api подменен вернула None (выполнена неудачно)"""
    mock_rub.return_value = None
    assert get_amount_transaction_rub(normal_transaction_usd) is None
    captured = capsys.readouterr()
    assert captured.out == "Conversion was not successful\n"
    mock_rub.assert_called_once()

@patch('src.external_api.requests.get')
def test_get_amount_rub(mock_get, get_standard_response):
    """Тест работы функции get_amount_rub с исходными данными 200 USD.
    В качестве api ответа используется фикстура get_standard_response"""
    mock_get.return_value.json.return_value = get_standard_response
    mock_get.return_value.status_code = 200
    assert get_amount_rub("USD", "200") == 14930.3108

@patch('src.external_api.requests.get')
def test_get_amount_rub_return_none(mock_get, get_standard_response):
    """Тест работы функции get_amount_rub с исходными данными 200 USD.
    Проверка работы, в случае, если статус-код не равен 200"""
    mock_get.return_value.json.return_value = get_standard_response
    mock_get.return_value.status_code = 401
    assert get_amount_rub("USD", "200") is None

@patch('src.external_api.requests.get')
def test_get_amount_rub_exception_error(mock_get, capsys: pytest.CaptureFixture[str]):
    """Тест работы функции get_amount_rub с выбросом исключения RequestException"""
    mock_get.side_effect = RequestException("Ошибка запроса")

    result = get_amount_rub("USD", "200")
    captured = capsys.readouterr()
    assert captured.out == "An error occurred. Please try again later.\n"
    assert result is None

@patch('src.external_api.requests.get')
def test_get_amount_rub_connection_error(mock_get, capsys: pytest.CaptureFixture[str]):
    """Тест работы функции get_amount_rub с выбросом исключения RequestException"""
    mock_get.side_effect = ConnectionError("Ошибка соединения")

    result = get_amount_rub("USD", "200")
    captured = capsys.readouterr()
    assert captured.out == "Connection Error. Please check your network connection.\n"
    assert result is None
