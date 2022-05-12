#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param grid int整型二维数组 
# @return int整型
#
"""
描述
在一个m\times nm×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
如输入这样的一个二维数组，
[
[1,3,1],
[1,5,1],
[4,2,1]
]
那么路径 1→3→5→2→1 可以拿到最多价值的礼物，价值为12

解析:
动态规划
"""
class Solution:
    def maxValue(self , grid: List[List[int]]) -> int:
        # write code here
        import copy
        pd = copy.deepcopy(grid)
        
        for i in range(len(pd)):
            for j in range(len(pd[0])):
                
                x = i-1
                y = j-1
                
                if x < 0 and y < 0:
                    sums = pd[i][j]
                elif x < 0:
                    sums = pd[i][j] + pd[i][y]
                elif y < 0:
                    sums = pd[i][j] + pd[x][j]
                else:
                    sums = max(pd[i][j] + pd[i][y], pd[i][j] + pd[x][j])
                
                pd[i][j] = sums
        return pd[i][j]
                
        