# @before-stub-for-debug-begin
from python3problem7 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        result = 0
        while x != 0:
            # 正负数取余问题，python里会比较特殊
            if x > 0:
                pop = x%10
            else:
                pop = x%(-10)
                
            x = int(x/10)
            if result > int(INT_MAX/10)or (result == int(INT_MAX/10) and pop > 7):
                return 0
            if result < int(INT_MIN/10) or (result == int(INT_MIN/10) and pop < -8):
                return 0;
            result = result * 10 + pop

        return result
# @lc code=end

