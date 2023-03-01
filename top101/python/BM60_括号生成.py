#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return string字符串一维数组
#

"""
描述
给出n对括号，请编写一个函数来生成所有的由n对括号组成的合法组合。
例如，给出n=3，解集为：
"((()))", "(()())", "(())()", "()()()", "()(())"

数据范围：0 \le n \le 100≤n≤10
要求：空间复杂度 O(n)O(n)，时间复杂度 O(2^n)O(2n)
"""

class Solution:
    def generateParenthesis(self , n: int) -> List[str]:
        # write code here
        
        
        def recursion(left: int, right: int, temp: str, res: List[str], n: int):
            
            if left == n and right == n:
                res.append(temp)
                return
            
            #使用一次左括号
            if left < n:
                recursion(left+1, right, temp+'(', res, n)
            
            # 使用右括号个数必须少于左括号
            if right < n and left > right:
                recursion(left, right+1, temp+')', res, n)
                
        res = []
        recursion(0, 0, "", res, n)
        return res
        