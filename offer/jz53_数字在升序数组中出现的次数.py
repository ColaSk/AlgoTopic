#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param data int整型一维数组 
# @param k int整型 
# @return int整型
#

"""
描述
给定一个长度为 n 的非降序数组和一个非负数整数 k ，要求统计 k 在数组中出现的次数

数据范围：0 \le n \le 1000 , 0 \le k \le 1000≤n≤1000,0≤k≤100，数组中每个元素的值满足 0 \le val \le 1000≤val≤100
要求：空间复杂度 O(1)O(1)，时间复杂度 O(logn)O(logn)

解析:
二分查找 
1. 二分查找过程中进行剪枝
2. 二分查找查到k的边界 k-0.5 k+0.5 
"""
class Solution:
    def GetNumberOfK(self , data: List[int], k: int) -> int:
        # write code here
        if not data:
            return 0
        return self.search(data, 0, len(data)-1, k)
    
    def search(self, data, left, right, k):
        
        if left >= right:
            if k == data[left]:
                return 1
            return 0
        
        mid =(left+right)//2
        
        if k == data[mid]:
            res = self.search(data, left, mid, k) + self.search(data, mid+1, right, k)
        elif k > data[mid]:
            res = self.search(data, mid+1, right, k)
        else:
            res = self.search(data, left, mid, k)
            
        return res
        
class Solution1:
    #二分查找
    def bisearch(self, data: List[int], k: float) -> int:
        left = 0
        right = len(data) - 1
        #二分左右界
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right = mid - 1
        return left
     
    def GetNumberOfK(self , data: List[int], k: int) -> int:
        #分别查找k+0.5和k-0.5应该出现的位置，中间的部分就全是k
        return self.bisearch(data, k + 0.5) - self.bisearch(data, k - 0.5)        