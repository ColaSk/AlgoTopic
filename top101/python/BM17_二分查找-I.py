#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @param target int整型 
# @return int整型
#

"""
描述
请实现无重复数字的升序数组的二分查找

给定一个 元素升序的、无重复数字的整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标（下标从 0 开始），否则返回 -1

数据范围：0 \le len(nums) \le 2\times10^50≤len(nums)≤2×10 
5
  ， 数组中任意值满足 |val| \le 10^9∣val∣≤10 
9
 
进阶：时间复杂度 O(\log n)O(logn) ，空间复杂度 O(1)O(1)
"""
class Solution:
    def search(self , nums: List[int], target: int) -> int:
        # write code here
        
        i, j = 0, len(nums)-1
        
        while i <= j:
            
            mid = (i+j)//2
            
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                return mid
        return -1
            
            