"""
Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.

Examples : 
Input : arr[] = {0, -1, 2, -3, 1}
Output : (0 -1 1), (2 -3 1)

Explanation : The triplets with zero sum are
0 + -1 + 1 = 0 and 2 + -3 + 1 = 0  

Input : arr[] = {1, -2, 1, 0, 5}
Output : 1 -2  1
Explanation : The triplets with zero sum is
1 + -2 + 1 = 0   
"""

def find_triplets(arr):
    res = []

    for i in range(len(arr)):
        seen = set()

        for j in range(i+1, len(arr)):
            x = -(arr[i] + arr[j])

            if x not in seen:
                seen.add(arr[j])
            else:
                res.append([arr[i], arr[j], x])
    
    return res

print(find_triplets([0,-1,2,-3,1]))