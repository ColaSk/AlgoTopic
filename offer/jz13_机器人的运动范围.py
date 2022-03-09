#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param threshold int整型 
# @param rows int整型 
# @param cols int整型 
# @return int整型
#
"""
描述
地上有一个 rows 行和 cols 列的方格。坐标从 [0,0] 到 [rows-1,cols-1] 。一个机器人从坐标 [0,0] 的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于 threshold 的格子。 例如，当 threshold 为 18 时，机器人能够进入方格   [35,37] ，因为 3+5+3+7 = 18。但是，它不能
进入方格 [35,38] ，因为 3+5+3+8 = 19 。请问该机器人能够达到多少个格子？

数据范围： 0≤threshold≤15  1≤rows,cols≤100 

进阶：空间复杂度 O(nm)，时间复杂度 O(nm)
"""
class Solution:
    def movingCount(self , threshold: int, rows: int, cols: int) -> int:
        # write code here
        
        visited = [False] * rows * cols
        
        return self.movingCountCore(threshold, rows, cols, 0, 0, visited)
        
        
    def movingCountCore(
        self, 
        threshold: int, 
        rows: int, 
        cols: int, 
        row: int, 
        col: int,
        visited: List[bool]):
        
        count = 0
        
        if (
            row < 0 or 
            row >= rows or 
            col < 0 or 
            col >= cols or 
            visited[row*cols+col] or
            self.getDigitSum(row) + self.getDigitSum(col) > threshold
        ):
            return 0
        
        visited[row*cols+col] = True
        count += 1
        
        return (count+
                self.movingCountCore(threshold, rows, cols, row+1, col, visited)+
                self.movingCountCore(threshold, rows, cols, row, col+1, visited))
    
    def getDigitSum(self, num: int):
        
        nsum = 0
        
        while num:
            nsum += num % 10
            num = int(num/10)
            
        return nsum
        