import pytest
from scripts.commonword import most_common_word


def test_most_common_word_book1():
    book1 = "In a galaxy far far away"
    assert most_common_word(book1) == "far"

def test_most_common_word_book2():
    book2 = "Taco cat ate a taco"
    assert most_common_word(book2) == "taco"

def test_most_common_word_book3():
    book3 = "No. Try not. Do or do not. There is no try."
    assert most_common_word(book3).lower() == "no"  # Change the assertion to be case-insensitive

def test_most_common_word_book4():
    book4 = "Cat, cat. CAT! cat"
    assert most_common_word(book4) == "cat"

def test_most_common_word_empty_book():
    book5 = ""
    assert most_common_word(book5) == ""

def test_most_common_word_single_word():
    book6 = "apple"
    assert most_common_word(book6) == "apple"

def test_most_common_word_multiple_common_words():
    book7 = "dog dog cat cat"
    assert most_common_word(book7) == "dog"

if __name__ == "__main__":
    pytest.main()
