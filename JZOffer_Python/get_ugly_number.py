# -*- coding:utf-8 -*-
'''
题目描述：
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
class Solution:
    # 算法效率低，很大程度上不管一个数是不是丑数都要尽心计算
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 0:
            return 0
        number  = 0
        uglyFound = 0

        while uglyFound < index:
            number = number + 1
            if self.IsUgly(number):
                uglyFound = uglyFound + 1

        return number

    def IsUgly(self,number):

        while number % 2 == 0:
            number = number / 2
        while number % 3 == 0:
            number = number / 3
        while number % 5 == 0:
            number = number / 5

        if number == 1:
            return 1
        else:
            return 0


    # 只计算丑数，不在非丑数上花费时间,但需要一个数组存储丑数
    def FindTheKUgly(self,index):
        if index == 0:
            return 0
        curnum = 1
        min2 = min3 = min5 = 0
        ugly = [1]
        while curnum < index:
            minnum = min(ugly[min2] * 2, ugly[min3] * 3, ugly[min5] * 5)
            ugly.append(minnum)
            while ugly[min2] * 2 <= minnum:
                min2 = min2 + 1
            while ugly[min3] * 3 <= minnum:
                min3 = min3 + 1
            while ugly[min5] * 5 <= minnum:
                min5 = min5 + 1
            curnum = curnum + 1
        return ugly[-1]






s = Solution()
n = 10
print s.GetUglyNumber_Solution(n)
print s.FindTheKUgly(n)