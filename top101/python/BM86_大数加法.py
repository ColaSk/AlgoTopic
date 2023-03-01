#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算两个数之和
# @param s string字符串 表示第一个整数
# @param t string字符串 表示第二个整数
# @return string字符串
#

"""
描述
以字符串的形式读入两个数字，编写一个函数计算它们的和，以字符串形式返回。

数据范围：s.length,t.length \le 100000s.length,t.length≤100000，字符串仅由'0'~‘9’构成
要求：时间复杂度 O(n)O(n)
"""
class Solution:
    def solve(self , s: str, t: str) -> str:
        # write code here
        
        if not s:
            return t
        
        if not t:
            return s
        
        n = len(s) if len(s) > len(t) else len(t)
        s = s[::-1]
        t = t[::-1]
        res = []
        i = 0
        sign = 0
        
        while i < n:
            
            if i < len(s):
                snum = s[i]
            else:
                snum = '0'
            
            if i < len(t):
                tnum = t[i]
            else:
                tnum = '0'
                
            num = int(snum) + int(tnum) + sign
            res.append(str(num%10))
            sign = int(num/10)
            
            i += 1
            
        if sign:
            res.append(str(sign))
        
        return ''.join(res[::-1])
            
            
        