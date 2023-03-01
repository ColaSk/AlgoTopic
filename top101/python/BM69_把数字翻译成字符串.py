#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 解码
# @param nums string字符串 数字串
# @return int整型
#

"""
1. nums 为空
2. 首字母为0
3. nums 直接为10 或 20的时候
4. 字母为0 但是不能够和前边的字母组成10，20的情况
"""
class Solution:
    def solve(self , nums: str) -> int:
        # write code here
        
        if nums[0] == '0':
            return 0
        
        dp = [1]*(len(nums)+1)
        
        for i in range(2, len(nums)+1):
            
            if nums[i-1] == '0':
                if nums[i-2] not in ['1', '2']:
                    return 0
                else:
                    dp[i] = dp[i-2]
            elif nums[i-2] != '0' and (
                (int(nums[i-2:i]) >=1 and int(nums[i-2:i])<=19) or \
                 (int(nums[i-2:i]) >=21 and int(nums[i-2:i])<=26)):
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        
        return dp[len(nums)]
                
                      