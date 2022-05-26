#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param num int整型一维数组 
# @return int整型二维数组
#
class Solution:
    def permute(self , num: List[int]) -> List[List[int]]:
        # write code here
        
        if not num:
            return []
        
        if len(num) == 1:
            return [num]
        
        res = []
        
        for i in range(len(num)):
            data = self.permute(num[0:i]+num[i+1:])
            for d in data:
                d.append(num[i])
            res += data
        
        return res
            
            