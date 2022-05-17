
"""
给定一个数组，一个整数n 将数组分割成大小为n的子数组

[1,2,3,4,5] 2 [[1,2], [3,4], [5]] 6 [[1,2,3,4,5]]
"""

from typing import List


def test(arr: List[int], n: int) -> List[List[int]]:

    result = []

    if not arr:
        return []

    if n >= len(arr):
        result.append(arr[:])
        return result
    
    i, j = 0, n

    while j <= len(arr):
        result.append(arr[i:j])
        i += n
        j += n

    if i < len(arr):
        result.append(arr[i:])
    
    return result

print(test([1,2,3,4,5], 7))