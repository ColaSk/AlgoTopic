#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_l = len(s)
        result = ""
        if s_l == numRows:
            return s
        if numRows == 1:
            return s
        max_jump = 2*numRows-2
        for i in range(numRows):
            jump = max_jump - 2*i
            j = i
            k = j + jump
            while j < s_l:

                result = result + s[j]
                # 第一行最后一行的情况
                if k < s_l and i > 0 and i < numRows-1:
                    result = result + s[k]
                j = j + max_jump
                k = j + jump 

        return result

            
# @lc code=end

print(Solution().convert("PAYPALISHIRING", 3))

