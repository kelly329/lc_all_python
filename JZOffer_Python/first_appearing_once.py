# -*- coding:utf-8 -*-
'''
题目描述：
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。

解题思路：
哈希表
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        # 存储当前字符
        self.alist = []
        # 存储当前字符和字符出现此处，只出现一次为1，大于1次设为2
        self.adict = {}
    def FirstAppearingOnce(self):
        while len(self.alist) > 0 and self.adict[self.alist[0]] == 2:
            self.alist.pop(0)
        if len(self.alist) == 0:
            return '#'
        else:
            return self.alist[0]


    def Insert(self, char):
        if char not in self.adict.keys():
            self.adict[char] = 1
            self.alist.append(char)
        else:
            self.adict[char] = 2