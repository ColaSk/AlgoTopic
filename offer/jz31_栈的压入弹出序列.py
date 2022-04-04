# -*- coding:utf-8 -*-
"""
描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
1. 0<=pushV.length == popV.length <=1000
2. -1000<=pushV[i]<=1000
3. pushV 的所有数字均不相同
"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        
        stack = []
        
        i = j = 0
        
        while i < len(pushV):
            if pushV[i] != popV[j]:
                stack.append(pushV[i])
                i += 1
            else:
                i += 1
                j += 1
                
                while stack and stack[-1] == popV[j]: 
                    stack.pop()
                    j += 1
                    
        return stack == []
            
            
            