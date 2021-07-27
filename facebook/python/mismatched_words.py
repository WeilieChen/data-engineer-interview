"""
Complete a function that returns a list containing 
all the mismatched words (case sensitive) between two 
given input strings.

Given two sentences, you have to print the words those 
are not present in either of the sentences. (If one word 
is present twice in 1st sentence but not present in 2nd 
sentence then you have to print that word too).
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
