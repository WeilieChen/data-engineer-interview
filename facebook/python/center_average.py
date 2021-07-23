def solution(nums):
    total = sum(nums)
    _min = min(nums)
    _max = max(nums)
    return int((total - _min - _max) / (len(nums) - 2))
    
assert solution([1, 2, 3, 4, 100]) == 3
assert solution([1, 1, 5, 5, 10, 8, 7]) == 5
assert solution([-10, -4, -2, -4, -2, 0]) == -3