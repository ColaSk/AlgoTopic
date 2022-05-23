#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
"""
描述
给定一个长度为n的数组nums，请你找到峰值并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个所在位置即可。
1.峰值元素是指其值严格大于左右相邻值的元素。严格大于即不能有等于
2.假设 nums[-1] = nums[n] = -\infty−∞
3.对于所有有效的 i 都有 nums[i] != nums[i + 1]
4.你可以使用O(logN)的时间复杂度实现此问题吗？

解析
因为题目将数组边界看成最小值，而我们只需要找到其中一个波峰，因此只要不断地往高处走，一定会有波峰。
那我们可以每次找一个标杆元素，将数组分成两个区间，每次就较高的一边走，因此也可以用分治来解决，而
标杆元素可以选择区间中点。
"""
class Solution:
    def findPeakElement(self , nums: List[int]) -> int:
        # write code here
                
        i, j = 0, len(nums)-1
        
        while i < j:
            
            mid = (i+j)//2
            
            if nums[mid] < nums[mid+1]:
                i = mid + 1
            else:
                j = mid
        return j