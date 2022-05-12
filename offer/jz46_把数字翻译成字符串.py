#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 解码
# @param nums string字符串 数字串
# @return int整型
#
"""
描述
有一种将字母编码成数字的方式：'a'->1, 'b->2', ... , 'z->26'。
我们把一个字符串编码成一串数字，再考虑逆向编译成字符串。
由于没有分隔符，数字编码成字母可能有多种编译结果，例如 11 既可以看做是两个 'a' 也可以看做是一个 'k' 。但 10 只可能是 'j' ，因为 0 不能编译成任何结果。
现在给一串数字，返回有多少种可能的译码结果

数据范围：字符串长度满足 0 < n \le 900<n≤90
进阶：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)

解析:
动态规划，但是要分析一些特殊情况
"""
class Solution:
    def solve(self , nums: str) -> int:
        # write code here
        
        # 为空的情况
        if not nums:
            return 0
        
        # 首字母为0的情况
        if '0' == nums[0]:
            return 0
        
        # nums 直接为 10 或者 20 的情况
        if nums in ['10', '20']:
            return 1
        
        dp = [1]*(len(nums)+1)
        
        for i in range(1, len(nums)):
            s = nums[i]
            s_ = nums[i-1]
            
            n = int(s_+s)
            
            # 字母为0 但是不能够和前边的字母组成10，20的情况
            if s == '0' and n not in [10, 20]:
                return 0
            
            if 11<=n<=19 or 21<=n<=26:
                dp[i+1] = dp[i] + dp[i-1]
            else:
                dp[i+1] = dp[i]
        
        return dp[len(nums)]
                    
                
            
        
        