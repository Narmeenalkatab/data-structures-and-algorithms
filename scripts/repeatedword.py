import re

def repeated_word(s):
    def process_string(s):
        words = re.findall(r'\w+', s.lower())
        return words

    def build_word_frequency_map(words):
        word_freq_map = {}
        for word in words:
            if word in word_freq_map:
                return word
            word_freq_map[word] = True  
        return None

    words = process_string(s)
    return build_word_frequency_map(words)
