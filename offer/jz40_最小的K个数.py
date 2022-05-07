#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param input int整型一维数组 
# @param k int整型 
# @return int整型一维数组
#
"""
描述
给定一个长度为 n 的可能有重复值的数组，找出其中不去重的最小的 k 个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4(任意顺序皆可)。
数据范围：0\le k,n \le 100000≤k,n≤10000，数组中每个数的大小0 \le val \le 10000≤val≤1000
要求：空间复杂度 O(n)O(n) ，时间复杂度 O(nlogn)O(nlogn)

解析:
大顶锥
"""
class Solution:
    def GetLeastNumbers_Solution(self , input: List[int], k: int) -> List[int]:
        # write code here
        import heapq
        
        if len(input) < k or k == 0:
            return []
        
        res = []
        pq = []
        
        for i in range(k):
            heapq.heappush(pq, -1*input[i])
        
        for i in range(k, len(input)):
            if (-1*pq[0]) > input[i]:
                heapq.heapreplace(pq, (-1 * input[i]))
        
        for i in range(k):
            res.append(-1 * pq[0])
            heapq.heappop(pq)
        
        return res
        
        
        
        