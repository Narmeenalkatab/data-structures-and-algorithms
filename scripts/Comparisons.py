def compare_numbers(a, b):
    if a == b:
        return 0
    if a < b:
        return -1
    if a > b:
        return 1


def compare_strings(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    return 0


def sort_by_year(movie):
    return movie["year"]


def sort_alphabetically(movie):
    return ignore_leading_words(movie["title"])


def ignore_leading_words(title):
    ignore_words = ["A", "An", "The"]
    words = title.split(" ")
    if len(words) > 1 and words[0] in ignore_words:
        return " ".join(words[1:])
    return title



