"""
654. https://www.lintcode.com/problem/654/description

Given two Sparse Matrix A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Input: 
    [[1,0,0],[-1,0,3]]
    [[7,0,0],[0,0,0],[0,0,1]]
Output:
    [[7,0,0],[-7,0,3]]
Explanation:
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

Example2
Input:
    [[1,0],[0,1]]
    [[0,1],[1,0]]
Output:
    [[0,1],[1,0]]
"""

class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        row_a = len(A)
        col_a = len(A[0])
        row_b = len(B)
        col_b = len(B[0])

        res = [[0] * col_b for _ in range(row_a)]
        for i in range(row_a):
            for j in range(col_b):
                for k in range(col_a):
                    res[i][j] += A[i][k] * B[k][j]

        return res