#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#
"""
描述
给定两个字符串str1和str2，输出两个字符串的最长公共子序列。如果最长公共子序列为空，则返回"-1"。目前给出的数据，仅仅会存在一个最长的公共子序列

数据范围：0 \le |str1|,|str2| \le 20000≤∣str1∣,∣str2∣≤2000
要求：空间复杂度 O(n^2)O(n 
2
 ) ，时间复杂度 O(n^2)O(n 
2
 )
题目主要信息：
找到两个字符串的最长公共子序列，子序列不要求位置在原串中连续
仅存在一个最长公共子序列，不需要去重
最长公共子序列为空需要返回"-1"，而不是空序列，最后要变换

"""
class Solution:
    def LCS(self , s1: str, s2: str) -> str:
        # write code here
        
        if not s1 or not s2:
            return "-1"
        
        l1 = len(s1)
        l2 = len(s2)
        
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        
        # 计算最长序列
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # 找到序列           
        s = []
        while dp[i][j] != 0:
            
            if dp[i][j] == dp[i-1][j]:
                i-=1
            elif dp[i][j] == dp[i][j-1]:
                j-=1
            else:
                i-=1
                j-=1
                s.insert(0, s1[i])
                
        return "".join(s) if s else "-1"
        
        
        
        