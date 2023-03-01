#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @return string字符串一维数组
#

"""
描述
输入一个长度为 n 字符串，打印出该字符串中字符的所有排列，你可以以任意顺序返回这个字符串数组。
例如输入字符串ABC,则输出由字符A,B,C所能排列出来的所有字符串ABC,ACB,BAC,BCA,CBA和CAB。
"""
class Solution:
    def Permutation(self , str: str) -> List[str]:
        # write code here
        def recursion(str: str) -> List[str]:
            
            if not str:
                return []
            
            if len(str) == 1:
                return [str]
            
            result = []
            temp = {}
            
            for i in range(len(str)):
                
                if str[i] in temp:
                    continue
                
                temp[str[i]] = True
                
                res = recursion(str[0:i] + str[i+1:])
                for j in range(len(res)):
                    s = str[i] + res[j]
                    res[j] = s
                result += res
            return result
            
        return recursion(str)   
        