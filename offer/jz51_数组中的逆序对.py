#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param data int整型一维数组 
# @return int整型
#

"""
描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P mod 1000000007

数据范围：  对于 50\%50% 的数据, size\leq 10^4size≤10 
4
 
对于 100\%100% 的数据, size\leq 10^5size≤10 
5
 
数组中所有数字的值满足 0 \le val \le 10000000≤val≤1000000

要求：空间复杂度 O(n)O(n)，时间复杂度 O(nlogn)O(nlogn)

解析 归并排序思想，递归拆分到底层然后向上层归并
"""
class Solution:
    mod = 1000000007
    def InversePairs(self , data: List[int]) -> int:
        # write code here
        temp = [0 for _ in range(len(data))]
        return self.Mergesort(0, len(data)-1, data, temp)
    
    def Mergesort(self, left, right, data, temp):
        
        if left >= right:
            return 0
        
        mid = int((left + right) / 2)
        
        res = self.Mergesort(left, mid, data, temp) + self.Mergesort(mid+1, right, data, temp)
#         res %= self.mod
        i, j = left, mid + 1
        
        for k in range(left, right+1):
            temp[k] = data[k]
            
        for k in range(left, right+1):
            
            if i == mid + 1: # 边界
                data[k] = temp[j]
                j += 1
            elif j == right + 1 or temp[i] <= temp[j]: # 边界与正常情况
                data[k] = temp[i]
                i += 1
            else: # 前边大于后边的情况
                data[k] = temp[j]
                j += 1
                res += mid - i + 1
        
        return res%self.mod
                
        