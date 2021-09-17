"""
Given a 2 dim array (n x m), return a 1 dim array that is the vertical sum of all arrays.
"""

def vert_sum(array):
    res = []
    n = len(array[0])

    for i in range(0, n):
        sumed = 0
        for row in array:
            sumed += row[i]
        res.append(sumed)

    return res

assert vert_sum([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]) == [12, 15, 18]
assert vert_sum([
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,10]
]) == [12, 15, 18, 21]
print("passed")