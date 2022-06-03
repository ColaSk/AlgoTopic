#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param A string字符串 
# @return int整型
#

"""
描述
对于长度为n的一个字符串A（仅包含数字，大小写英文字母），请设计一个高效算法，计算其中最长回文子串的长度。


数据范围： 1 \le n \le 10001≤n≤1000
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n^2)O(n 
2
 )
进阶:  空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)


解析
1. 目前解决方法是将字符串反转，寻找两个字符串的最长连续公共子序列，但是有一个用例未通过，
时间复杂度与空间复杂度都较高
"""
class Solution:
    def getLongestPalindrome(self , A: str) -> int:
        # write code here
        
        B = A[::-1]
        
        dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
        res = 0
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if B[j-1] == A[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                if dp[i][j] > res:
                    res = dp[i][j]
        
        return res