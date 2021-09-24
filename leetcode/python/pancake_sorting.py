"""
https://leetcode.com/problems/pancake-sorting/
"""

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        res = []
        
        for i in range(len(arr)-1, -1, -1):
            max_idx = i
            
            for j in range(i, -1, -1):
                if arr[j] > arr[max_idx]:
                    max_idx = j

            if max_idx != i:
                flip(max_idx)
                flip(i)

                res.append(max_idx+1)
                res.append(i+1)

        return res

[3, 2,1,4]