#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 the n
# @return int整型
#

"""
描述
N 皇后问题是指在 n * n 的棋盘上要摆 n 个皇后，
要求：任何两个皇后不同行，不同列也不在同一条斜线上，
求给一个整数 n ，返回 n 皇后的摆法数。
"""
class Solution:
    def Nqueen(self , n: int) -> int:
        # write code here
        
        def isValid(pos: List[int], row: int, col: int) -> bool:
            
            for i in range(row):
                if pos[i] == col or abs(row-i) == abs(col-pos[i]):
                    return False
            return True
        
        
        def NqueeCore(pos: List[int], row: int, res: int) -> int:
            
            n = len(pos)
            
            if row == n:
                return res+1
            
            for i in range(n):
                if isValid(pos, row, i):
                    pos[row] = i
                    res = NqueeCore(pos, row+1, res)
                    pos[row] = 0
            return res
        
        pos = [0]*n
        return NqueeCore(pos, 0, 0)
                
            
            
        
        
                