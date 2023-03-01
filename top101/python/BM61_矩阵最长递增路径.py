#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 递增路径的最大长度
# @param matrix int整型二维数组 描述矩阵的每个数
# @return int整型
#
"""
描述
给定一个 n 行 m 列矩阵 matrix ，矩阵内所有数均为非负整数。 你需要在矩阵中找到一条最长路径，使这条路径上的元素是递增的。并输出这条最长路径的长度。
这个路径必须满足以下条件：

1. 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外。
2. 你不能走重复的单元格。即每个格子最多只能走一次。

数据范围：1 \le n,m \le 10001≤n,m≤1000，0 \le matrix[i][j] \le 10000≤matrix[i][j]≤1000
进阶：空间复杂度 O(nm)O(nm) ，时间复杂度 O(nm)O(nm)

解析
1.递归dfs + 动态规划
"""

class Solution:
    def solve(self , matrix: List[List[int]]) -> int:
        # write code here
        
        def solveCore(matrix: List[List[int]], dp: List[List[int]], i: int, j: int) -> int:
            
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            n = len(matrix)
            m = len(matrix[0])
             
            if dp[i][j] != 0:
                return dp[i][j]
            
            dp[i][j] += 1
            
            for d in dirs:
                nexti = i + d[0]
                nextj = j + d[1]
                if nexti >= 0 and nexti < n and nextj >= 0 and nextj < m and matrix[nexti][nextj] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], solveCore(matrix, dp, nexti, nextj)+1)
            return dp[i][j]
        
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[0 for _ in range(m)] for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, solveCore(matrix, dp, i, j))
        return res
            