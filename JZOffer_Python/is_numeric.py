# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.index = 0

    # s字符串
    def isNumeric(self, s):
        if not s or len(s) <= 0:
            return False

        flag = self.scanInteger(s)
        # 如果出现'.'，则接下来是数字的小数部分
        if self.index < len(s) and s[self.index] == '.':
            self.index += 1
            '''
            or的原因:
            1.小数部分可以没有整数部分，如.123 
            2.小数点后面可以没有数字 233.
            3.小数点前后都可以有数字 23.66
            '''
            flag = self.scanUnsignedInteger(s) or flag

        if self.index < len(s) and (s[self.index] == 'e' or s[self.index] == 'E'):
            self.index += 1
            '''
            and原因：
            1.当e或者E前面没有数字时，整个字符不能表示数字 如.e1 e1
            2.当e或者E后面没有整数时，整个字符不能表示数字 如 12e 12e+5.4
            '''
            flag = self.scanInteger(s) and flag

        return flag and self.index == len(s)




    def scanInteger(self, s):
        if self.index < len(s) and (s[self.index] == '+' or s[self.index] == '-'):
            self.index += 1
        return self.scanUnsignedInteger(s)


    def scanUnsignedInteger(self, s):
        start = self.index
        while(self.index < len(s) and s[self.index] >= '0' and s[self.index] <= '9'):
            self.index += 1

        # 是否存在整数
        return start < self.index







