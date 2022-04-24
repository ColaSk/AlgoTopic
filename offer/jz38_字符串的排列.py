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
        def recursion(res, string, temp, vis):
            
            if len(temp) == len(string):
                res.append(temp)
                return
            
            for i in range(len(string)):
                if vis[i] == 1:
                    continue
                if i > 0 and string[i-1] == string[i] and vis[i-1]:
                    continue
                
                vis[i] = 1 # 标记用过
                temp += string[i]              
                recursion(res, string, temp, vis)              
                vis[i] = 0               
                temp = temp[:-1]
              
        # 字典排序，重复相邻
        string = "".join((lambda x:(x.sort(), x)[1])(list(str)))      
        vis = [0]*len(str) # 标记每个位置字符的使用情况     
        res = []
        temp = ""
        # 递归方法 。。。
        recursion(res, string, temp, vis)   
        return res
        