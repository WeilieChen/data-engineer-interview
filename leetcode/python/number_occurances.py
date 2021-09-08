"""
Find the number of occurrences of each number in the list and store the result.

Example 1:
Input: [1, 2, 1, 2, 2, 5, 7]
Output: {1: 2, 2: 3, 5: 1, 7: 1}
"""

def number_occurance(nums):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    return counts

assert number_occurance([1, 2, 1, 2, 2, 5, 7]) == {1: 2, 2: 3, 5: 1, 7: 1}
print("passed")