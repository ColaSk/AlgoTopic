#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param number int整型 
# @return int整型
#
"""
描述
给你一根长度为 n 的绳子，请把绳子剪成整数长的 m 段（ m 、 n 都是整数， n > 1 并且 m > 1 ， m <= n ），每段绳子的长度记为 k[1],...,k[m] 。
请问 k[1]*k[2]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是 8 时，我们把它剪成长度分别为 2、3、3 的三段，此时得到的最大乘积是 18 。

数据范围：2≤n≤60
进阶：空间复杂度 O(1) ，时间复杂度 O(n)
输入描述：
输入一个数n，意义见题面。

# 解析: 动态规划 f(n) = max(f(i)*f(n-i)) 
"""
class Solution:
    def cutRope(self , number: int) -> int:
        # write code here
        """动态规划"""
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        if number == 3:
            return 3
        
        visited = [0]*(number+1)
        
        visited[1], visited[2], visited[3] = 1,2,3
        
        for i in range(4, number+1):
            max_num = 0
            for j in range(1, int(i/2)+1):
                product = visited[j]*visited[i-j]
                if max_num < product:
                    max_num = product
            visited[i] = max_num
        return visited[-1]