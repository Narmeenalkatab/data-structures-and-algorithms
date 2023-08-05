from scripts.leftjoin import left_join

def test_left_join():
    synonyms = {
        'happy': 'joyful',
        'sad': 'unhappy',
        'angry': 'mad',
    }

    antonyms = {
        'happy': 'sad',
        'excited': 'bored',
    }

    result = left_join(synonyms, antonyms)
    assert result == [('happy', 'joyful', 'sad'), ('sad', 'unhappy', None), ('angry', 'mad', None)]

    antonyms_empty = {}
    result_empty = left_join(synonyms, antonyms_empty)
    assert result_empty == [('happy', 'joyful', None), ('sad', 'unhappy', None), ('angry', 'mad', None)]

    synonyms_empty = {
        'hot': 'warm',
        'cold': 'chilly',
    }

    antonyms = {
        'hot': 'cold',
        'warm': 'cool',
    }

    result = left_join(synonyms_empty, antonyms)
    assert result == [('hot', 'warm', 'cold'), ('cold', 'chilly', None)]
