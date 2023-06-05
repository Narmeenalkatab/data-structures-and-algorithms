import pytest
from scripts.brackets import validate_brackets

def test_validate_brackets():
    assert validate_brackets("{}") == True
    assert validate_brackets("{}(){}") == True
    assert validate_brackets("()[[Extra Characters]]") == True
    assert validate_brackets("(){}[[]]") == True
    assert validate_brackets("{}{Code}[Fellows](())") == True
    assert validate_brackets("[({}]") == False  # Error: Closing bracket } doesn't match opening bracket (.
    assert validate_brackets("(](") == False  # Error: Closing bracket ) arrived without corresponding opening.
    assert validate_brackets("{(})") == False  # Error: Unmatched opening bracket { remaining.
    assert validate_brackets("{") == False  # Error: Unmatched opening bracket { remaining.
    assert validate_brackets(")") == False  # Error: Closing bracket ) arrived without corresponding opening.
    assert validate_brackets("[}") == False  # Error: Closing bracket } doesn't match opening bracket [.
