"""
Count the number of times a substring appear in a string.
"""


def solution(string, sub_str):
    inc = len(sub_str)
    count = 0

    for i in range(0, len(string)):
        if sub_str == string[i:i+inc]:
            count += 1

    return count


assert solution("abaabba", "aba") == 1
assert solution("ababab", "ab") == 3
assert solution("aaaaaa", "aa") == 5
assert solution("azcbobobegghaklbob", "bob") == 3
