#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
"""
描述
输入一个整数 n ，求 1～n 这 n 个整数的十进制表示中 1 出现的次数
例如， 1~13 中包含 1 的数字有 1 、 10 、 11 、 12 、 13 因此共出现 6 次

注意：11 这种情况算两次

数据范围： 1 \le n \le 30000 \1≤n≤30000 
进阶：空间复杂度 O(1) \O(1)  ，时间复杂度 O(lognn) \O(lognn) 

解析:
数学问题
"""
class Solution:
    def NumberOf1Between1AndN_Solution(self , n: int) -> int:
        # write code here
        
        base, res = 1, 0
        
        while base <= n:
            
            cur = n//base%10
            a = n//base//10
            b = n%base
            
            if cur == 1:
                res += a*base+b+1
            elif cur == 0:
                res += a*base
            else:
                res += (a+1)*base
                
            base *= 10
        
        return res
            
        