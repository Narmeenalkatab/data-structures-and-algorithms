
def sort_by_most_recent_year(movies):
    return sorted(movies, key=lambda movie: movie["year"], reverse=True)


def remove_leading_articles(title):
    return title.lstrip("AaTtNn ").strip()


def sort_alphabetically_ignore_articles(movies):
    return sorted(movies, key=lambda movie: remove_leading_articles(movie["title"].upper()))
