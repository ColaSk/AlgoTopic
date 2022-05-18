#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return bool布尔型
#

"""
描述
现在有2副扑克牌，从扑克牌中随机五张扑克牌，我们需要来判断一下是不是顺子。
有如下规则：
1. A为1，J为11，Q为12，K为13，A不能视为14
2. 大、小王为 0，0可以看作任意牌
3. 如果给出的五张牌能组成顺子（即这五张牌是连续的）就输出true，否则就输出false。
4.数据保证每组5个数字，每组最多含有4个零，数组的数取值为 [0, 13]

要求：空间复杂度 O(1)O(1)，时间复杂度 O(nlogn)O(nlogn)，本题也有时间复杂度 O(n)O(n) 的解法
"""
class Solution:
    def IsContinuous(self , numbers: List[int]) -> bool:
        # write code here
        hash = dict()
        
        max = 0
        min = 13
        
        for i in range(len(numbers)):
            if numbers[i] > 0:
                if numbers[i] in hash:
                    return False
                else:
                    hash[numbers[i]] = i
                    
                    if numbers[i] >= max:
                        max = numbers[i]
                    
                    if numbers[i] <= min:
                        min = numbers[i]
                        
        if max-min >= 5:
            return False
        else:
            return True
        
        