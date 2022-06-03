#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return string字符串一维数组
#

"""
描述
现在有一个只包含数字的字符串，将该字符串转化成IP地址的形式，返回所有可能的情况。
例如：
给出的字符串为"25525522135",
返回["255.255.22.135", "255.255.221.35"]. (顺序没有关系)

数据范围：字符串长度 0 \le n \le 120≤n≤12
要求：空间复杂度 O(n!)O(n!),时间复杂度 O(n!)O(n!)

注意：ip地址是由四段数字组成的数字序列，格式如 "x.x.x.x"，其中 x 的范围应当是 [0,255]。

解析
递归回溯
1. 第一个字母为0的情况 '010'
2. 为空的情况
3. ip范围 0-255
"""

class Solution:
    def restoreIpAddresses(self , s: str) -> List[str]:
        # write code here
        
        def dfs(s: str, n: int) -> List[str]:
            
            if not s:
                return []
            
            if n == 4:
                if s[0] == '0' and len(s) > 1:
                    return []
                if int(s) > 255:
                    return []
                return [s]
            
            res = []
            
            for i in range(3):
                if i < len(s):
                    ip_s = s[0:i+1]
                    
                    if ip_s[0] == '0' and len(ip_s) > 1:
                        continue
                        
                    if int(ip_s) <= 255:
                        r = dfs(s[i+1:], n+1)
                        if r:
                            for ip in r:
                                res.append(ip_s+'.'+ip)
            return res
        return dfs(s, 1)