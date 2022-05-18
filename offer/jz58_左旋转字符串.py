#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @param n int整型 
# @return string字符串
#

"""
描述
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列  S ，请你把其循环左移 K 位后的序列输出。例如，字符序列 S = ”abcXYZdef” , 要求输出循环左移 3 位后的结果，即 “XYZdefabc”

数据范围：输入的字符串长度满足 0 \le len \le 100 \0≤len≤100  ， 0 \le n \le 100 \0≤n≤100 
进阶：空间复杂度 O(n)\O(n) ，时间复杂度 O(n)\O(n) 

解析
就地逆置三次
"""
class Solution:
    
    def reverse(self, s: List[str], start: int, end: int):
        
        while start < end:
            s[start], s[end] = s[end], s[start]
            
            start += 1
            end -= 1
    
    def LeftRotateString(self , str: str, n: int) -> str:
        # write code here
        
        if not str:
            return ""
        
        n = n%len(str)
        sl = list(str)
        
        self.reverse(sl, 0, len(str)-1)
        self.reverse(sl, 0, len(str)-n-1)
        self.reverse(sl, len(str)-n, len(str)-1)
        
        return "".join(sl)
        
        
        