#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return string字符串
#

"""描述
请实现一个函数，将一个字符串s中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

数据范围:0≤len(s)≤1000 。保证字符串中的字符为大写英文字母、小写英文字母和空格中的一种。
进阶：时间复杂度 O(n)\O(n)  ,空间复杂度 O(n) \O(n) 

解析: python 中有替换函数 replace, sub, 这里使用栈的方式

"""
class Solution:
    def replaceSpace(self , s: str) -> str:
        # write code here
        stack = []
        
        for strr in s:
            
            if strr == ' ':
                stack.append('%20')
            else:
                stack.append(strr)
        return ''.join(stack)
        