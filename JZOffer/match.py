# -*- coding:utf-8 -*-
'''
题目描述：
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

解题思路：

当模式中的第二个字符不是“*”时：
1、如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，然后匹配剩余的。
2、如果 字符串第一个字符和模式中的第一个字符相不匹配，直接返回false。

而当模式中的第二个字符是“*”时：
如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，继续匹配。如果字符串第一个字符跟模式第一个字符匹配，可以有3种匹配方式：
1、模式后移2字符，相当于x*被忽略；
2、字符串后移1字符，模式后移2字符；
3、字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位；
'''
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s is None or pattern is None:
            return False
        return self.matchCore(s, pattern)

    def matchCore(self, s, pattern):
        if s == "" and pattern == "":
            return True
        if s != "" and pattern == "":
            return False
        if len(pattern) >= 2 and pattern[1] == '*':
            if s != "" and (s[0] == pattern[0] or pattern[0]=='.'):
                return self.matchCore(s[1:],pattern[2:]) or self.matchCore(s[1:],pattern) or self.matchCore(s,pattern[2:])
            else:
                return self.matchCore(s, pattern[2:])
        if s != "" and s[0] == pattern[0] or (pattern[0] == '.' and len(s) != 0):
            return self.matchCore(s[1:],pattern[1:])
        return False
