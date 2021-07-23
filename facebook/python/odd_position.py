def solution(nums):
    result = []
    for i, n in enumerate(nums):
        if i % 2 != 0:
            result.append(n)

    return result

assert solution([0,1,2,3,4,5]) == [1,3,5]
assert solution([1,-1,2,-2]) == [-1,-2]
            