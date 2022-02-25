#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return int整型
#

""" 牛客网 jz3
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
# 请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，那么对应的输出是2或者3。存在不合法的输入的话输出-1

# 数据范围： 0≤n≤10000 
# 进阶：时间复杂度O(n) ，空间复杂度O(n)

# 解题思路: (数据重排) 重头到尾扫描数组S中的每一个元素，当扫描到第i个元素的时候，比较第i个元素位置的值m是否等于i，如果相等，则说明该元素已经在排好序的位置，
# 继续扫描其他元素；如果不相等，先判断m是否等于S[m]，相等则说明不同位置上的元素值相等，即元素重复。直接返回元素；否则交换m和S[m]将他们放置到排好序的位置

"""
class Solution:
    def duplicate(self , numbers: List[int]) -> int:
        # write code here
        
        if not numbers:
            return -1
        
        for i in range(len(numbers)):
            
            while numbers[i] != i:
                
                num = numbers[i]
                
                if num == numbers[num]:
                    return num
                
                numbers[i], numbers[num] = numbers[num], numbers[i]
                
        return -1