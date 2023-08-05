def most_common_word(book):
    word_frequency = {}
    max_frequency = 0
    most_common = ""

    words = book.lower().split()

    for word in words:
        word = word.strip('.,?!:;"\'()')

        if not word:
            continue

        word_frequency[word] = word_frequency.get(word, 0) + 1

        if word_frequency[word] > max_frequency:
            max_frequency = word_frequency[word]
            most_common = word

    return most_common
