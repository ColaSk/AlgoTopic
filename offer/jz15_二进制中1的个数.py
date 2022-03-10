#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#

"""
描述
输入一个整数 n ，输出该数32位二进制表示中1的个数。其中负数用补码表示。

数据范围：- 2^{31} <= n <= 2^{31}-1

即范围为:−2147483648<=n<=2147483647
"""

# TODO: 当前不是最优解
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        B = 32
        while B:
            key = (n >> (B-1)) & 1 ##判断第B为是否为1
            B -= 1
            if key == 1:
                count += 1
        return count