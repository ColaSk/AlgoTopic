#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @return int整型
#
# 动态规划状态转化方程: dp[i]=max(dp[i−1]+array[i],array[i])
"""
描述
输入一个长度为n的整型数组array，数组中的一个或连续多个整数组成一个子数组，子数组最小长度为1。求所有子数组的和的最大值。
数据范围:
1 <= n <= 2\times10^51<=n<=2×10 
5
 
-100 <= a[i] <= 100−100<=a[i]<=100

解析:
动态规划: 动态规划状态转化方程: dp[i]=max(dp[i−1]+array[i],array[i])
"""
class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> int:
        # write code here
        
        temp = [0]*len(array)
        temp[0] = array[0]
        maxsum = array[0]
        
        for i in range(1, len(array)):
            s = max(temp[i-1]+array[i], array[i])
            if maxsum < s:
                maxsum = s
            
            temp[i] = s
        
        return maxsum
            