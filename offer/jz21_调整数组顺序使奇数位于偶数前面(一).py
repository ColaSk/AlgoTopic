#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @return int整型一维数组
#
"""
描述
输入一个长度为 n 整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

数据范围：0≤n≤5000，数组中每个数的值 0 ≤val≤10000
要求：时间复杂度 O(n)，空间复杂度 O(n)
进阶：时间复杂度 O(n^2)，空间复杂度 O(1)

解析: 本题有两种解题过程，采用了时间换空间的解题过程，需要注意(并保证奇数和奇数，偶数和偶数之间的相对位置不变)条件
"""
class Solution:
    def reOrderArray(self , array: List[int]) -> List[int]:
        # write code here
        i = 0
        j = 0
        
        while j < len(array):
            
            # 奇数
            if array[j]%2:
                z = j-1
                v = array[j]
                while z >= i:
                    array[z+1] = array[z]
                    z -= 1
                array[i] = v
                i += 1
                j += 1
            # 偶数
            else:
                j += 1
        return array