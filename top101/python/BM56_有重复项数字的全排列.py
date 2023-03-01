#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param num int整型一维数组 
# @return int整型二维数组
#

"""
描述
给出一组可能包含重复项的数字，返回该组数字的所有排列。结果以字典序升序排列。

数据范围： 0 < n \le 80<n≤8 ，数组中的值满足 -1 \le val \le 5−1≤val≤5
要求：空间复杂度 O(n!)O(n!)，时间复杂度 O(n!)O(n!)
"""
class Solution:
    def permuteUnique(self , num: List[int]) -> List[List[int]]:
        # write code here
        
        def permuteUniqueCore(num: List[int]) -> List[List[int]]:
        
            if not num:
                return []

            if len(num) == 1:
                return [num]

            res = []
            temp = {}

            for i in range(len(num)):
                if num[i] in temp:
                    continue
                temp[num[i]] = True
                data = permuteUniqueCore(num[0:i]+num[i+1:])
                for d in data:
                    d.insert(0, num[i])
                res += data

            return res
        
        num.sort()
        return permuteUniqueCore(num)