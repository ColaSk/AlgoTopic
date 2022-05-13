#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param index int整型 
# @return int整型
#
"""
描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第 n个丑数。

数据范围：0 \le n \le 20000≤n≤2000
要求：空间复杂度 O(n)O(n) ， 时间复杂度 O(n)O(n)
"""
class Solution:
    def GetUglyNumber_Solution(self , index: int) -> int:
        # write code here
        
        import heapq
        
        if index == 0 or index == 1:
            return index
        
        factors = [2,3,5]
        mp = dict()
        pq = [1]
        mp[1] = 1
        heapq.heapify(pq)
        res = 1
        for i in range(index):
            for x in factors:
                num = res*x
                if num not in mp:
                    mp[num] = 1
                    heapq.heappush(pq, num)
            res = heapq.heappop(pq)
        
        return res
                
            
            
        
            
        