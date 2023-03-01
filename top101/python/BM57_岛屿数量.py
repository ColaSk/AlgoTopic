#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 判断岛屿数量
# @param grid char字符型二维数组 
# @return int整型
#
class Solution:
    def solve(self , grid: List[List[str]]) -> int:
        # write code here
        
        def dfs(grid: List[List[str]], i, j):
            
            rows = len(grid)
            columns = len(grid[0])
            
            if i < 0 or i >= rows or j < 0 or j >= columns:
                return
            
            if grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(grid, i-1, j)
                dfs(grid, i, j+1)
                dfs(grid, i+1, j)
                dfs(grid, i, j-1)
        
        n = len(grid)
        m = len(grid[0])
        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j)
        return res