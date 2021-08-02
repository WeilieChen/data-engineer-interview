"""
Count distinct words in a sentence.
"""


def solution(sent):
    count = {}
    for word in sent.split():
        count[word] = count.get(word, 0) + 1

    result = [
        v
        for k, v in count.items()
        if v == 1
    ]

    return len(result)

assert solution("") == 0
assert solution("once") == 1
assert solution("once twice") == 2
assert solution("once twice twice") == 1
assert solution("this is a sentence") == 4
