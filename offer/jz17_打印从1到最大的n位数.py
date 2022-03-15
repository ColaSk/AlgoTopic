#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 最大位数
# @return int整型一维数组
#
"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
1. 用返回一个整数列表来代替打印
2. n 为正整数，0 < n <= 5
"""

class Solution:
    def printNumbers(self , n: int) -> List[int]:
        # write code here
        maxnum = int('9'*n)
        i = 1
        rt = []
        while i <= maxnum:
            
            rt.append(i)
            
            i += 1
            
        return rt
            
            
        