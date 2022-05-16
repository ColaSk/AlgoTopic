#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @param sum int整型 
# @return int整型一维数组
#
"""
描述
输入一个升序数组 array 和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，返回任意一组即可，如果无法找出这样的数字，返回一个空数组即可。

数据范围: 0 \le len(array) \le 10^5 ​​\0≤len(array)≤10 
5
 ​​ ， 1 \le array[i] \le 10^6 \1≤array[i]≤10 
6

解析: 双指针
"""
class Solution:
    def FindNumbersWithSum(self , array: List[int], sum: int) -> List[int]:
        # write code here
        
        if not array or len(array) == 1:
            return []
        
        i = 0
        j = len(array) - 1
        
        while i < j:
            
            if array[i] + array[j] == sum:
                return [array[i], array[j]]
            
            elif array[i] + array[j] > sum:
                j -= 1
            
            else:
                i += 1
        
        return []