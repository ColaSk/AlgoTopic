"""
数组  [1, 3, 5, 7] 打印 1357 1375
"""

from typing import List


# 1 3 5 7

# 3 5 7

# 5 7

# 7 



# def test(arr: List[int]) -> List[List[int]]:
    
#     if len(arr) <= 1:
#         return []

#     if len(arr) == 2:
#         return [[arr[0], arr[1]], [arr[1], arr[0]]]
    
#     for i in range(len(arr)):

#         res = test(arr[i:])

#         for r in res:
#             r.insert(0, arr[0])
    
#     return res


def test1(arr: List[int]) -> List[List[int]]:

    if len(arr) == 1:
        return arr

    result = []
    for i in range(len(arr)):
        res = test1(arr[0:i] + arr[i+1:])

        if len(res) == 1:
            result.append(arr[i:i + 1] + res)
        else:
            result += [[arr[i]] + j for j in res]

    return result



print(test1([1,3,5,7]))

    

    