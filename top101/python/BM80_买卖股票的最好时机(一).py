#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param prices int整型一维数组 
# @return int整型
#

"""
描述
假设你有一个数组prices，长度为n，其中prices[i]是股票在第i天的价格，请根据这个价格数组，返回买卖股票能获得的最大收益
1.你可以买入一次股票和卖出一次股票，并非每天都可以买入或卖出一次，总共只能买入和卖出一次，且买入必须在卖出的前面的某一天
2.如果不能获取到任何利润，请返回0
3.假设买入卖出均无手续费

数据范围： 0 \le n \le 10^5 , 0 \le val \le 10^40≤n≤10 
5
 ,0≤val≤10 
4
 
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)
"""
class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        
        # 贪心算法 搜索便利的最小值，搜索最小值与遍历的数值的最大差值
        def maxP1(prices: List[int]) -> int:
            if len(prices) < 2:
                return 0
            
            minv = prices[0]
            diff = prices[1]-minv
            
            for i in range(1, len(prices)):
                
                if prices[i] < minv:
                    minv = prices[i]
                    
                if prices[i] - minv > diff:
                    diff = prices[i] - minv
                    
            return diff
        
        # 动态规划
        def maxP2(prices: List[int]) -> int:
            if len(prices) < 2:
                return 0
            
            # dp[i][0] 不持股 dp[i][1] 持股
            dp = [[0]*2 for _ in range(len(prices))]
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            
            for i in range(1, len(prices)):
                
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]) # 今天不持股  
                dp[i][1] = max(dp[i-1][1], -prices[i]) # 今天持股
            
            return max(dp[len(prices)-1])
            
        
        return maxP2(prices)
    
        
            
            