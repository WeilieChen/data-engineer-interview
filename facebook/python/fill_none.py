def solution(nums):
    prev = next(n for n in nums if n != None)

    for i, n in enumerate(nums):
        if n == None:
            nums[i] = prev
        else:
            prev = n
    
    return nums

assert solution([1,None,2,3,None,None,5,None]) == [1,1,2,3,3,3,5,5]
assert solution([12,34,None,1,2,3,22,None,23,24,25,None,25,17,29,None,None,1]) ==  [12,34,34,1,2,3,22,22,23,24,25,25,25,17,29,29,29,1]
assert solution([None,1,2,3,None,4,None,None]) == [1,1,2,3,3,4,4,4]