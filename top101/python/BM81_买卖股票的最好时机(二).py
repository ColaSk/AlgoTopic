#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算最大收益
# @param prices int整型一维数组 股票每一天的价格
# @return int整型
#

"""
描述
假设你有一个数组prices，长度为n，其中prices[i]是某只股票在第i天的价格，请根据这个价格数组，返回买卖股票能获得的最大收益
1. 你可以多次买卖该只股票，但是再次购买前必须卖出之前的股票
2. 如果不能获取收益，请返回0
3. 假设买入卖出均无手续费

数据范围： 1 \le n \le 1 \times 10^51≤n≤1×10 
5
  ， 1 \le prices[i] \le 10^41≤prices[i]≤10 
4
 
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)
进阶：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)
"""
class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        
        def maxP1(prices: List[int]) -> int:
            
            if len(prices) < 2:
                return 0
            
            dp = [[0]*2 for _ in range(len(prices))]
            
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            
            for i in range(1, len(prices)):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]) # 不持股
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]) # 持股
                
            return dp[len(prices)-1][0]
        
        return maxP1(prices)
                
            
        