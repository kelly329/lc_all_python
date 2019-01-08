# -*- coding:utf-8 -*-
'''
题目描述：
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

'''
'''
解题思路：
https://www.cnblogs.com/lliuye/p/9159152.html
https://www.jianshu.com/p/f809287268f5
1.把数据数组转换为字符串数组
2.比较str1+str2 与 str2+str1 转换为整型的大小比较
3.python2.7 sorted() sort()函数
转换成int型
① intnum1 > intnum2 str1>str2
② intnum1 < intnum2 str2>str1
③ intnum1==intnum2 str1=str2
cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
'''
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        string = [str(num) for num in numbers]
        string.sort(self.theMax, reverse=False)
        return "".join(string)



    def theMax(self,str1,str2):
        str1str2 = int(str1 + str2)
        str2str1 = int(str2 + str1)
        return 1 if str1str2 > str2str1 else -1
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers or len(numbers) <= 0:
            return ''
        
        compares = lambda x, y : cmp(str(x) + str(y), str(y) + str(x))
        min_string = sorted(numbers, cmp = compares)
        return ''.join(str(s) for s in min_string)
s = Solution()
print(s.PrintMinNumber([3, 32, 321]))
s = Solution()
print s.PrintMinNumber([3,4,2,123,456,12,11,27])