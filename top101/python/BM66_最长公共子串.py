#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#

"""
描述
给定两个字符串str1和str2,输出两个字符串的最长公共子串
题目保证str1和str2的最长公共子串存在且唯一。 

数据范围： 1 \le |str1|,|str2| \le 50001≤∣str1∣,∣str2∣≤5000
要求： 空间复杂度 O(n^2)O(n 
2
 )，时间复杂度 O(n^2)O(n 
2
 )

解析: 动态规划
"""
class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        # write code here
        
        len1 = len(str1)
        len2 = len(str2)
        
        dp = [[0]*(len2+1) for _ in range(len1+1)]
        max = 0
        pos = 0
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                if dp[i][j] > max:
                    max = dp[i][j]
                    pos = i
                    
        return str1[pos-max: pos]
                    
        
        