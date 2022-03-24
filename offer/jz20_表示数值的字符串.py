#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @return bool布尔型
#
"""
描述
请实现一个函数用来判断字符串str是否表示数值（包括科学计数法的数字，小数和整数）。
解析: 使用正则法则, 当然也可以使用其他方式
"""
class Solution:
    def isNumeric(self , str: str) -> bool:
        # write code here
        import re
        match_Obj = re.match('^\s*[+-]{0,1}((\d)+((\.)(\d)+){0,1}|((\.)(\d)+)|((\d)+(\.)))([eE][+-]{0,1}[\d]+){0,1}\s*$',str)
        if match_Obj:
            return True
        else:
            return False