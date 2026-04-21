import pytest
from src.decorators import log

def test_decorator_console_success(capsys):
    """Тест успешного выполнения функции с логированием в консоль"""
    @log()
    def simple_addition(x,y):
        return x + y
    result = simple_addition(2,3)
    assert result == 5
    captyred = capsys.readouterr()

    assert captyred.out == 'simple_addition OK\n'
    assert captyred.err == ''

def test_decorator_console_error(capsys):
    """Тест обработки исключения с логированием в консоль"""
    @log()
    def simple_addition_err(x,y):
        return x + y

    with pytest.raises(TypeError):
        simple_addition_err("a", 3)

    captured = capsys.readouterr()

    expected_log = "foo \"simple_addition_err\" Error \"can only concatenate str (not \"int\") to str\", inputs: ('a', 3), {}\n"

    assert  captured.out == expected_log
    assert captured.err == ""
