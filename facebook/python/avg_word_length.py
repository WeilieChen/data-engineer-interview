"""
Calculate the average word length.
"""


def solution(sent):
    words = sent.split()
    return sum(len(word) for word in words) / len(words)


assert solution("Hi my name is Bob") == 2.6
assert solution("4444 4444") == 4.0
