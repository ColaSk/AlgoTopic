#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param matrix int整型二维数组 
# @return int整型一维数组
#
class Solution:
    def printMatrix(self , matrix: List[List[int]]) -> List[int]:
        res = []                               
        while matrix:
            res += matrix.pop(0)            
            matrix = list(zip(*matrix))[::-1]  
        return res