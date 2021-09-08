"""
Given a list of numbers, return the unique values. The output should be a list ordered by the first occurrence of the number.

Example 1:
Input: [1, 1, 1, 2, 3, 4, 4, 1]
Output: [1, 2, 3, 4]

Example 2:
Input: [1, 7, 2, 9]
Output: [1, 7, 2, 9]
"""

def unique_list(nums):
    s = set()
    res = []
    for n in nums:
        if n not in s:
            res.append(n)
        s.add(n)

    return res

assert unique_list([1, 1, 1, 2, 3, 4, 4, 1]) == [1, 2, 3, 4]
assert unique_list([1, 7, 2, 9]) == [1, 7, 2, 9]
print("passed")