#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 给定数组的最长严格上升子序列的长度。
# @param arr int整型一维数组 给定的数组
# @return int整型
#

"""
描述
给定一个长度为 n 的数组 arr，求它的最长严格上升子序列的长度。
所谓子序列，指一个数组删掉一些数（也可以不删）之后，形成的新数组。例如 [1,5,3,7,3] 数组，其子序列有：[1,3,3]、[7] 等。但 [1,6]、[1,3,5] 则不是它的子序列。
我们定义一个序列是 严格上升 的，当且仅当该序列不存在两个下标 ii 和 jj 满足 i<ji<j 且 arr_i \geq arr_jarr 
i
​
 ≥arr 
j
​
 。
数据范围： 0\leq n \leq 10000≤n≤1000
要求：时间复杂度 O(n^2)O(n 
2
 )， 空间复杂度 O(n)O(n)
"""
class Solution:
    def LIS(self , arr: List[int]) -> int:
        # write code here
        
        dp = [1]*(len(arr)+1)
        dp[0] = 0
        res = 0
        for i in range(2, len(dp)):
            for j in range(i-1):
                if arr[i-1] > arr[j]:
                    dp[i] = max(dp[i], dp[j+1]+1)
                    res = max(res, dp[i])
        
        return res
            
            