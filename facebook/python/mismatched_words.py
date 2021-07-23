"""
Complete a function that returns a list containing 
all the mismatched words (case sensitive) between two 
given input strings.
"""


def solution(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    return (set1 - set2).union(set2 - set1)


assert solution(
    "Firstly this is the first string",
    "Next is the second string"
) == {'Firstly', 'this', 'first', 'Next', 'second'}
