import pytest
from scripts.Comparisons import (
    compare_numbers,
    compare_strings,
    sort_by_year,
    ignore_leading_words,
    sort_alphabetically,
)


def test_compare_numbers():
    assert compare_numbers(5, 10) == -1
    assert compare_numbers(10, 5) == 1
    assert compare_numbers(5, 5) == 0


def test_compare_strings():
    assert compare_strings("apple", "banana") == -1
    assert compare_strings("banana", "apple") == 1
    assert compare_strings("apple", "apple") == 0


def test_sort_by_year():
    movie1 = {"title": "Movie 1", "year": 2020}
    movie2 = {"title": "Movie 2", "year": 2021}
    movie3 = {"title": "Movie 3", "year": 2019}

    assert sort_by_year(movie1) == 2020
    assert sort_by_year(movie2) == 2021
    assert sort_by_year(movie3) == 2019


def test_sort_alphabetically():
    movie1 = {"title": "The Movie"}
    movie2 = {"title": "An Awesome Movie"}
    movie3 = {"title": "Great Movie"}

    assert sort_alphabetically(movie1) == "Movie"
    assert sort_alphabetically(movie2) == "Awesome Movie"
    assert sort_alphabetically(movie3) == "Great Movie"


def test_ignore_leading_words():
    assert ignore_leading_words("The Movie") == "Movie"
    assert ignore_leading_words("An Awesome Movie") == "Awesome Movie"
    assert ignore_leading_words("Great Movie") == "Great Movie"


if __name__ == "__main__":
    pytest.main()
