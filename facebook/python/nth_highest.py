"""
Given a dictionary, print the key for nth highest 
value present in the dict. If there are more than 
1 record present for nth highest value then sort 
the key and print the first one.
"""


def solution(data, n):
    a_dict = {}
    for k, v in data.items():
        a_dict[v] = a_dict.get(v, []) + [k]

    key = sorted(a_dict.keys(), reverse=True)[n-1]
    return sorted(a_dict[key])[0]


assert solution({'a': 1, 'b': 2}, 1) == 'b'
assert solution({'a': 1, 'b': 2}, 2) == 'a'
assert solution({'a': 1, 'b': 2, 'c': 2}, 1) == 'b'
assert solution({'a': 1, 'b': 2, 'c': 2, 'd': 1}, 2) == 'a'
assert solution({'a': 1, 'b': 2, 'c': 3}, 3) == 'a'
