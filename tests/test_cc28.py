import pytest
from scripts.cc28 import sort_by_most_recent_year, sort_alphabetically_ignore_articles, remove_leading_articles

@pytest.fixture
def sample_movies():
    return [
        {"title": "The Avengers", "year": 2012, "genres": ["Action", "Adventure", "Sci-Fi"]},
        {"title": "The Dark Knight", "year": 2008, "genres": ["Action", "Crime", "Drama"]},
        {"title": "An Inception", "year": 2010, "genres": ["Action", "Adventure", "Sci-Fi"]},
        {"title": "A Titanic", "year": 1997, "genres": ["Drama", "Romance"]},
        {"title": "Avatar", "year": 2009, "genres": ["Action", "Adventure", "Fantasy"]},
        {"title": "Gladiator", "year": 2000, "genres": ["Action", "Adventure", "Drama"]},
    ]

def test_sort_by_most_recent_year(sample_movies):
    sorted_movies = sort_by_most_recent_year(sample_movies)
    for i in range(len(sorted_movies) - 1):
        assert sorted_movies[i]["year"] >= sorted_movies[i + 1]["year"]

def test_sort_alphabetically_ignore_articles(sample_movies):
    sorted_movies = sort_alphabetically_ignore_articles(sample_movies)
    for i in range(len(sorted_movies) - 1):
        title_a = remove_leading_articles(sorted_movies[i]["title"].upper())
        title_b = remove_leading_articles(sorted_movies[i + 1]["title"].upper())
        assert title_a <= title_b
