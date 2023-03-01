#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str1 string字符串 
# @param str2 string字符串 
# @return int整型
#

"""
描述
给定两个字符串 str1 和 str2 ，请你算出将 str1 转为 str2 的最少操作数。
你可以对字符串进行3种操作：
1.插入一个字符
2.删除一个字符
3.修改一个字符。

字符串长度满足 1 \le n \le 1000 \1≤n≤1000  ，保证字符串中只出现小写英文字母。

解析
动态规划
"""
class Solution:
    def editDistance(self , str1: str, str2: str) -> int:
        # write code here
        
        l1 = len(str1)
        l2 = len(str2)
        
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        
        for i in range(l1+1):
            dp[i][0] = i
        
        for j in range(l2+1):
            dp[0][j] = j
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if str2[j-1] == str1[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    
        return dp[i][j]
        