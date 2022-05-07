"""
描述
给一个长度为 n 的数组，数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2]。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。

数据范围：n \le 50000n≤50000，数组中元素的值 0 \le val \le 100000≤val≤10000
要求：空间复杂度：O(1)O(1)，时间复杂度 O(n)O(n)
输入描述：
保证数组输入非空，且保证有解

解析:
hash法
排序法
候选法
"""

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return int整型
#
# 候选法
class Solution:
    def MoreThanHalfNum_Solution(self , numbers: List[int]) -> int:
        # write code here
        cond = -1 # 候选人
        cnt = 0 # 投票数
        
        for num in numbers:
            
            if cnt == 0:
                cond = num   
                cnt += 1
            elif num == cond:
                cnt += 1
            else:
                cnt -= 1
            
        cnt = 0
        for num in numbers:
            if cond == num:
                cnt += 1
        
        if cnt > (len(numbers)/2):
            return cond
        
        return 0
                
        