"""
Complete a function that returns a list containing 
all the mismatched words (case sensitive) between two 
given input strings.
"""


def solution(str1, str2):
    count = {}
    for w in str1.split():
        count[w] = count.get(w, 0) + 1
    for w in str2.split():
        count[w] = count.get(w, 0) + 1

    return [w for w in count if count[w] == 1]


assert solution(
    "Firstly this is the first string",
    "Next is the second string"
) == ['Firstly', 'this', 'first', 'Next', 'second']

assert solution(
    "apple banana mango",
    "banana fruits mango"
) == ['apple', 'fruits']
