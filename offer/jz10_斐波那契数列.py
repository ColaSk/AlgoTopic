#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#

"""
描述
大家都知道斐波那契数列，现在要求输入一个正整数 n ，请你输出斐波那契数列的第 n 项。
斐波那契数列是一个满足:
    fib(x) = 1 x = 1,2
    fib(x) = fib(x-1) + fib(x-2) x > 2
  
数据范围：1\leq n\leq 401≤n≤40
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n) ，本题也有时间复杂度 O(logn)O(logn) 的解法

输入描述：
一个正整数n
返回值描述：
输出一个正整数。

# 解析: 递归方式最简单易懂，时间复杂度为 2^n, 空间复杂度为n,所以这种不是最优解
    当我们构建递归树之后，发现有多个重复子问题, 通过状态转换图可以获取转换方程:
    a, b = b, a + b (初始a 和b 分别为 0, 1) 

"""
class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here
        if n < 2:
            return n
        sum,a, b = 0, 0, 1
        for i in range(2, n+1):
            sum = a + b
            a = b
            b = sum
        return sum