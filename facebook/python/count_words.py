"""
Count the number of times a word appear in a sentence using a Hash Map.
"""


def solution(sent, input_word):
    count = {}
    for word in sent.split():
        count[word] = count.get(word, 0) + 1

    return count[input_word]


assert solution("once twice twice", "twice") == 2
