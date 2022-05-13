#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return int整型
#
"""
描述
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
数据范围:
\ \text{s.length}\le 40000 s.length≤40000
解析
使用滑动窗口
"""
class Solution:
    def lengthOfLongestSubstring(self , s: str) -> int:
        # write code here
        
        l = len(s)
        
        if l == 0 or l == 1:
            return l
            
        rates = {}
        i = j = 0
        maxl = 0
        
        while i < l:
            s_ = s[i]
            
            if s_ in rates:
                rates[s_] += 1
            else:
                rates[s_] = 1
                
            while rates[s_] > 1:
                rates[s[j]] -= 1
                j += 1
            
            if i-j+1 > maxl:
                maxl = i-j+1
            i+=1
            
        return maxl
            
                
            
        
        