# -*- coding:utf-8 -*-
'''
题目：对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
解题思路：
1.整体翻转字符串
2.在把字符串分成两部分翻转（前面是[0:length-n)/[length - n,length)）
3.连接两个字符串
'''
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or len(s) < n or n < 0:
            return ''
        s = list(s)
        length = len(s)
        s = self.Reverse(s)
        s1 = self.Reverse(s[:length-n])
        s2 = self.Reverse(s[length-n:])
        result = ''.join(s1) + ''.join(s2)
        return result

    def Reverse(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s
s = Solution()
#abcdefg,2
print s.LeftRotateString("abcXYZdef",3)
print s.LeftRotateString("abcdefg",2)