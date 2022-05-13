#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @return int整型
#

"""
描述
在一个长为 字符串中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）


数据范围：0 \le n \le 100000≤n≤10000，且字符串只有字母组成。
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)

解析
使用字典统计出现次数，遍历str 找到第一个出现次数为一的下表
"""
class Solution:
    def FirstNotRepeatingChar(self , str: str) -> int:
        # write code here
        mp = dict()
        
        for s in str:
            if s in mp:
                mp[s] += 1
            else:
                mp[s] = 1
        
        for i in range(len(str)):
            if mp[str[i]] == 1:
                return i
        return -1
            