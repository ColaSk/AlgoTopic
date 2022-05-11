#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
"""
描述
数字以 0123456789101112131415... 的格式作为一个字符序列，在这个序列中第 2 位（从下标 0 开始计算）是 2 ，第 10 位是 1 ，第 13 位是 1 ，以此类题，请你输出第 n 位对应的数字。

解析
1.确定所在的位数区间2.确定数字3.确定位数
"""
class Solution:
    def findNthDigit(self , n: int) -> int:
        # write code here
        
        if n <= 9:
            return n
        digit = 1 # 记录位数
        start = 1 # 记录当前区间起始数据 1, 10, 100
        sum = 9 # # 记录当前区间数字数量
        
        # 定位n的区间
        while n > sum:
            n -= sum
            digit += 1
            start *= 10
            sum = 9*digit*start
        
        # 定位n在哪个数字上
        num = start + n//digit -1
        
        # 定位n在数字的那个位数上
        index = (n-1)%digit
        return int(str(num)[index])
            
        
        