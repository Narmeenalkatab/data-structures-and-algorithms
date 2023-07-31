def left_join(synonyms, antonyms):
    result = []
    for key in synonyms:
        synonym_value = synonyms[key]
        antonym_value = antonyms.get(key, None)
        result.append([key, synonym_value, antonym_value])
    return result


