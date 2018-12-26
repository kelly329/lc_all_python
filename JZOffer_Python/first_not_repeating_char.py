# -*- coding:utf-8 -*-
'''
题目描述：
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
'''

'''
解题思路：
https://blog.csdn.net/u010005281/article/details/80085597
利用Python中的字典。字典的键（Key）一定唯一，每个键对应的值（Value）对应该键Key出现的次数。
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s or len(s) <= 0:
            return -1

        dicts = {}

        for ele in s:
            if ele in dicts:
                dicts[ele] = dicts[ele] + 1
            else:
                dicts[ele] = 1
        # 按照s字符串中的顺序查看每一个字符出现的次数，即可查到第一个出现一次的字符
        for i in range(len(s)):
            if dicts[s[i]] == 1:
                return i
        return -1