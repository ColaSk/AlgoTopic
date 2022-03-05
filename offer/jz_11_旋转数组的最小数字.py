#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param rotateArray int整型一维数组 
# @return int整型
#
"""
描述
有一个长度为 n 的非降序数组，比如[1,2,3,4,5]，将它进行旋转，即把一个数组最开始的若干个元素搬到数组的末尾，变成一个旋转数组，比如变成了[3,4,5,1,2]，或者[4,5,1,2,3]这样的。请问，给定这样一个旋转数组，求数组中的最小值。

数据范围：1 \le n \le 100001≤n≤10000，数组中任意元素的值: 0 \le val \le 100000≤val≤10000
要求：空间复杂度：O(1)O(1) ，时间复杂度：O(logn)O(logn)

解析: 二分查找
"""
class Solution:
    def minNumberInRotateArray(self , rotateArray: List[int]) -> int:
        # write code here
        
        lens = len(rotateArray)
        
        if lens == 1:
            return rotateArray[0]
        
        i, j = 0, lens-1
        
        while i < j:
            center = int((i+j)/2)
            value = rotateArray[center]
            
            if value > rotateArray[j]:
                i = center + 1
            elif value < rotateArray[j]:
                j = center
            else:
                j -= 1
                
        return rotateArray[j]
        