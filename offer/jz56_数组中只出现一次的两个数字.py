#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @return int整型一维数组
#

"""
描述
一个整型数组里除了两个数字只出现一次，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

数据范围：数组长度 2\le n \le 10002≤n≤1000，数组中每个数的大小 0 < val \le 10000000<val≤1000000
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)

提示：输出时按非降序排列。

解析
1. 采用hash 方式
2. 异或方式  主要是不会
"""
class Solution:
    def FindNumsAppearOnce(self , array: List[int]) -> List[int]:
        # write code here
        mp = dict()
        res = list()
        #遍历数组
        for i in range(len(array)):
            #统计每个数出现的频率
            if array[i] in mp:
                mp[array[i]] += 1
            else:
                mp[array[i]] = 1
        #再次遍历数组
        for i in range(len(array)):
            #找到频率为1的两个数
            if mp[array[i]] == 1:
                res.append(array[i])
        #整理次序
        res.sort(reverse=False)
        return res