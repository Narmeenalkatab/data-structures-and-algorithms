import pytest
from scripts.duck import DuckDuckGoose

def test_DuckDuckGoose():
    # Test case 1: 
    players = ["A", "B", "C", "D", "E"]
    k = 3
    assert DuckDuckGoose(players, k) == "D"
