#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#

"""
描述
你是一个经验丰富的小偷，准备偷沿街的一排房间，每个房间都存有一定的现金，为了防止被发现，你不能偷相邻的两家，即，如果偷了第一家，就不能再偷第二家；如果偷了第二家，那么就不能偷第一家和第三家。
给定一个整数数组nums，数组中的元素表示每个房间存有的现金数额，请你计算在不被发现的前提下最多的偷窃金额。

数据范围：数组长度满足 1 \le n \le 2\times 10^5\1≤n≤2×10 
5
   ，数组中每个值满足 1 \le num[i] \le 5000 \1≤num[i]≤5000 
   
"""
class Solution:
    def rob(self , nums: List[int]) -> int:
        # write code here
        
        dp = [0]*(len(nums)+1)
        dp[1] = nums[0]
        
        for i in range(2, len(nums)+1):
            # 取当前金额与间隔金额的总数与不取当前金额用上家金额的最大值
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            
        return dp[len(nums)]