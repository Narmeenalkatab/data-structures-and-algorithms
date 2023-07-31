from scripts.leftjoin import left_join
import pytest

def test_left_join():
    synonyms_hash = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms_hash = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    result = left_join(synonyms_hash, antonyms_hash)
    assert result == [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"],
    ]

    result = left_join({}, {})
    assert result == []

    result = left_join({"apple": "red", "banana": "yellow"}, {"apple": "green"})
    assert result == [["apple", "red", "green"], ["banana", "yellow", None]]
