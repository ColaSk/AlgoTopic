#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param base double浮点型 
# @param exponent int整型 
# @return double浮点型
#
"""
描述
实现函数 double Power(double base, int exponent)，求base的exponent次方。

注意：
1.保证base和exponent不同时为0。
2.不得使用库函数，同时不需要考虑大数问题
3.有特殊判题，不用考虑小数点后面0的位数。

数据范围： |base|≤100  ， |exponent|≤100  ,保证最终结果一定满足 |val| <= 10^4
  
进阶：空间复杂度 O(1)  ，时间复杂度 O(n)
"""

class Solution:
    def Power(self , base: float, exponent: int) -> float:
        # write code here
        if not base and not exponent:
            return 0
        
        if not exponent:
            return 1
        
        if exponent < 0:
            exponent = -exponent
            base = 1/base
            
        rt = 1
        
        for _ in range(exponent):
            
            rt *= base
        
        return rt
        