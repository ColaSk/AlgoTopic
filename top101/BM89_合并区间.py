# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param intervals Interval类一维数组 
# @return Interval类一维数组
#

"""
描述
给出一组区间，请合并所有重叠的区间。
请保证合并后的区间按区间起点升序排列。

数据范围：区间组数 0 \le n \le 2 \times 10^50≤n≤2×10 
5
 ，区间内 的值都满足 0 \le val \le 2 \times 10^50≤val≤2×10 
5
 
要求：空间复杂度 O(n)O(n)，时间复杂度 O(nlogn)O(nlogn)
进阶：空间复杂度 O(val)O(val)，时间复杂度O(val)O(val)

"""
class Solution:
    def merge(self , intervals: List[Interval]) -> List[Interval]:
        # write code here
        key = lambda x: x.start
        intervals_sort = sorted(intervals, key=key)
        res = []
        
        for val in intervals_sort:
            if not res:
                res.append(val)
                continue
            
            if val.start <= res[-1].end:
                res[-1].end = max(res[-1].end, val.end)
            else:
                res.append(val)
        
        return res
                
        
        
        