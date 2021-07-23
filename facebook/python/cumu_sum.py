"""
Write a function that returns the cumulative
sum of elements in a list.
"""


def solution(nums):
    prev = 0
    result = []
    for i, n in enumerate(nums):
        prev = n + prev
        result.append(prev)
    return result


assert solution([1, 1, 1]) == [1, 2, 3]
assert solution([1, -1, 3]) == [1, 0, 3]
assert solution([100, -1, 5]) == [100, 99, 104]
