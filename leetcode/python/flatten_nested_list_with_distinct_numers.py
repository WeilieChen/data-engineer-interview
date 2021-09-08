"""
Given a nested list, return a flattened list with only the distinct numbers. The output should be a list ordered by the first occurrence of the number.

Example 1:
Input: [1, 2, 3, [1, 2], [4, 5], 1]
Output: [1, 2, 3, 4, 5]
"""

def flatten_dedupe_list(nums):
    s = set()

    def _flatten(a_list):    
        res = []
        for ele in a_list:
            if isinstance(ele, list):
                flattened = _flatten(ele)
                res.extend(flattened)
            else:
                if ele not in s:
                    res.append(ele)
                s.add(ele)
                
        return res
    
    return _flatten(nums)

assert flatten_dedupe_list([1, 2, 3, [1, 2], [4, 5], 1]) == [1, 2, 3, 4, 5]
print("passed")