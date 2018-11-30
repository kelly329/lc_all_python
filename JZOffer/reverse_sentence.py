# -*- coding:utf-8 -*-
'''
题目描述：翻转单词顺序
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一起处理。
例如输入字符"I am a student."则输出为"student. a am I"
'''

'''
解题思路：
第一步翻转句子中所有字符。".tenduts a ma I" 此时不但翻转了句子中单词的顺序，连单词内的字符顺序也翻转了。
第二步在翻转单词中字符中的顺序。"student. a am I"
在英语单词中，单词被空格分隔，我们通过扫描空格来确定每个单词的起始和终止位置
'''
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s == None or len(s)<=0:
            return ''
        s = list(s)
        s = self.Reverse(s)
        # print s
        pStart = 0
        pEnd = 0
        listTemp = []
        result = ''
        while pEnd < len(s):
            if pEnd == len(s) - 1:
                listTemp.append(self.Reverse(s[pStart:]))
                break
            if s[pStart] == ' ':
                pStart = pStart + 1
                pEnd = pEnd + 1
                listTemp.append(' ')
            elif s[pEnd] == ' ':
                listTemp.append(self.Reverse(s[pStart:pEnd]))
                pStart = pEnd
            else:
                pEnd = pEnd + 1
        print listTemp
        for i in listTemp:
            result += ''.join(i)
        return result
        




    def Reverse(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end],s[start]
            start += 1
            end -= 1
        return s


s = Solution()
print s.ReverseSentence("I am a student.")