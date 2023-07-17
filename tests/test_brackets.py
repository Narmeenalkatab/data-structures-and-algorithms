import pytest
from scripts.brackets  import validate_brackets  # Assuming the 'validate_brackets' function is in the 'brackets.py' file.

def test_validate_brackets():
    assert validate_brackets("{}") is True
    assert validate_brackets("{}(){}") is True
    assert validate_brackets("()[[Extra Characters]]") is True
    assert validate_brackets("(){}[[]]") is True
    assert validate_brackets("{}{Code}[Fellows](())") is True
    assert validate_brackets("[({}]") is False
    assert validate_brackets("(](") is False
    assert validate_brackets("{(})") is False
    assert validate_brackets("{") is False
    assert validate_brackets(")") is False
    assert validate_brackets("[}") is False
