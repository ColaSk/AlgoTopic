#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return string字符串
#
"""
描述
输入一个非负整数数组numbers，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组[3，32，321]，则打印出这三个数字能排成的最小数字为321323。
1.输出结果可能非常大，所以你需要返回一个字符串而不是整数
2.拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

解析:
- 这道题呢最重要的解决怎么样组装的数字是最小的，按照什么顺序组装？如果我们能得到这个次序，直接将
这个次序的数字拼接在一起就好了。
- 只考虑首字符的大小不可靠，但是如果字符串a拼接b的得到的数字大于b拼接a，那么肯定b应该排在a的前面，
我们要就按照这样的次序将排序的比较重载就可以了。
"""
class Solution:
    def PrintMinNumber(self , numbers: List[int]) -> str:
        # write code here
        import functools
        
        if not numbers:
            return ""
        
        nums = [str(n) for n in numbers]
        
        cmp = lambda x, y: 1 if x+y>y+x else -1
        
        nums.sort(key=functools.cmp_to_key(cmp))
        
        return "".join(nums)