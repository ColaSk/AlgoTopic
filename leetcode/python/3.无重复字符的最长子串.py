#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        str_record = {}
        for i in range(len(s)-1):
            temp_break = True
            for j in range(i+1, len(s)):
                s_ij = s[i:j]
                if s[j] in s_ij:
                    str_record[s_ij] = len(s_ij)
                    temp_break = False
                    break
            if temp_break:
                str_record[s_ij] = len(s_ij) + 1
            
        result = 0
        for k, v in str_record.items():
            if result < v:
                result = v
        return result
# @lc code=end

