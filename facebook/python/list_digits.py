def solution(n):
    return [int(c) for c in str(n)]

assert solution(123) == [1,2,3]
assert solution(400) == [4,0,0]