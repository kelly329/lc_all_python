# -*- coding:utf-8 -*-

'''
题目描述：
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''
class Solution:

    '''
    方法一：时间复杂度为O(nlogn)
    '''
    def NumberOf1Between1AndN_Solution(self, n):
        number = 0

        for i in range(n + 1):
            number += self.CountOne(i)
        return number

    def CountOne(self, n):
        count = 0
        while n:
            if n % 10 == 1:
                count += 1
            n = n / 10
        return count

    '''
    方法二：找规律
    https://www.cnblogs.com/wangkundentisy/p/8946858.html
    '''

    def NumberOf1AndN(self, n):
        if n < 0:
            return 0
        high = n
        cnt = 0
        i = 1
        while high:
            # high表示当前位的高位
            high = n / pow(10, i)
            temp = n / pow(10, i - 1)
            # cur表示第i位上的值，从1开始计算
            cur = temp % 10
            # low表示当前位的低位
            low = n - temp * pow(10, i - 1)

            if cur < 1:
                cnt += high * pow(10, i - 1)
            elif cur > 1:
                cnt += (high + 1) * pow(10, i - 1)
            else:
                cnt += high * pow(10, i - 1)
                cnt += (low + 1)
            i += 1
        return cnt