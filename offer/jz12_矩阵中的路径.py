#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param matrix char字符型二维数组 
# @param word string字符串 
# @return bool布尔型
#

"""
描述
请设计一个函数，用来判断在一个n乘m的矩阵中是否存在一条包含某长度为len的字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 例如 
[[a,b,c,e],[s,f,c,s],[a,d,e,e]] 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了
矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
数据范围：0≤n,m≤20 ,1≤len≤25 
进阶：时间复杂度O(n^2)， 空间复杂度O(n^2)

# 解析: DFS, 深度优先遍历
"""
class Solution:
    def hasPath(self , matrix: List[List[str]], word: str) -> bool:
        # write code here
        rows = len(matrix)
        
        if not rows:
            return False
        
        cols = len(matrix[0])
        
        if not cols:
            return False
        
        str_lens = 0
        
        for i in range(rows):
            for j in range(cols):
                visited = [False] * rows * cols
                if self.hasPathCore(matrix, rows,cols, i, j, word, str_lens, visited):
                    return True
        return False
                
    def hasPathCore(
        self, 
        matrix: List[List[str]],
        rows: int, 
        cols: int, 
        row: int, 
        col: int, 
        word: str, 
        strlen: int, 
        visited: List[bool]):
        
        if strlen == len(word):
            return True
        
        has = False
        
        if (row >= 0 and 
            row < rows and 
            col >= 0 and 
            col < cols and 
            matrix[row][col] == word[strlen] and 
            not visited[row * cols + col]):
            
            visited[row * cols + col] = True
            
            has = (self.hasPathCore(matrix,rows, cols, row, col-1, word, strlen+1, visited) or
                   self.hasPathCore(matrix,rows, cols, row-1, col, word, strlen+1, visited) or
                   self.hasPathCore(matrix,rows, cols, row, col+1, word, strlen+1, visited) or
                   self.hasPathCore(matrix,rows, cols, row+1, col, word, strlen+1, visited))
            
            if not has:
                visited[row * cols + col] = False
        return has
