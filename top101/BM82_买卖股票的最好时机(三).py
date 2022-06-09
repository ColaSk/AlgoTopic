#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 两次交易所能获得的最大收益
# @param prices int整型一维数组 股票每一天的价格
# @return int整型
#
"""
描述
假设你有一个数组prices，长度为n，其中prices[i]是某只股票在第i天的价格，请根据这个价格数组，返回买卖股票能获得的最大收益
1. 你最多可以对该股票有两笔交易操作，一笔交易代表着一次买入与一次卖出，但是再次购买前必须卖出之前的股票
2. 如果不能获取收益，请返回0
3. 假设买入卖出均无手续费

数据范围：1 \le n \le 10^51≤n≤10 
5
 ，股票的价格满足 1 \le val\le 10^41≤val≤10 
4
 
要求: 空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)
进阶：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)
"""
class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        
        
        n = len(prices)
        
        if n < 2:
            return 0
        
        """
        i,0 不持股
        i,1 买入一次
        i,2 卖出一次
        i,3 买入一次
        i,4 卖出一次
        """
        dp = [[-10000]*5 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1, n):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]+prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2]-prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3]+prices[i])
            
        return max(0, dp[n-1][2], dp[n-1][4])
            
            
            
        