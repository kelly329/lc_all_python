# -*- coding:utf-8 -*-
'''
题目描述：
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
复制
+2147483647
    1a33
输出
复制
2147483647
    0
'''

'''
题目思路（主要针对特殊情况的处理）：
1."   1123    " 对字符串前空格的处理
2."+" "-" 对正负的处理
3. 结果 = 上一次结果*10 + 现在值（注意现在得到的是字符类型，要进行转换）ASKII码-48就是实际数值；
4.对最大/最小数值的考虑

'''
class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s) == 0 or s == "":
            return 0
        newc = []
        for c in s:
            if c != '':
                newc.append(c)
        flag = 1
        result = 0
        for i in range(len(newc)):
            if newc[i] == '+':
                continue
            elif newc[i] == '-':
                flag = -1
                continue
            elif newc[i] >= '0' and newc[i] <= '9':
                # ord()字符的ascii转换 ASKII码-48就是实际数值；
                result = result * 10 + (ord(newc[i])-48)
            else:
                return 0
        # 最小的负整数
        # if (result < 0x80000000 or result > 0x7fffffff):
        #     return 0;

        return result * flag

s = Solution()
print s.StrToInt('123')









