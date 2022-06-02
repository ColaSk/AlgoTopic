#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 最少货币数
# @param arr int整型一维数组 the array
# @param aim int整型 the target
# @return int整型
#

"""
描述
给定数组arr，arr中所有的值都为正整数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个aim，代表要找的钱数，求组成aim的最少货币数。
如果无解，请返回-1.

数据范围：数组大小满足 0 \le n \le 100000≤n≤10000 ， 数组中每个数字都满足 0 < val \le 100000<val≤10000，0 \le aim \le 50000≤aim≤5000

要求：时间复杂度 O(n \times aim)O(n×aim) ，空间复杂度 O(aim)O(aim)。

解析
动态规划 迭代1-aim每种钱数的最小值
"""
class Solution:
    def minMoney(self , arr: List[int], aim: int) -> int:
        # write code here
        
        if not arr:
            return -1
        
        dp = [aim+1]*(aim+1)
        dp[0] = 0
        for i in range(1, aim+1):
            for j in range(len(arr)):
                if arr[j] <= i:
                    dp[i] = min(dp[i], dp[i-arr[j]]+1)
        return -1 if dp[aim] > aim else dp[aim]
                
                
            