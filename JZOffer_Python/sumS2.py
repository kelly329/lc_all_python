# -*- coding:utf-8 -*-
'''
题目描述：
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
例如，输入15，由于1+2+3+4+5 = 4+5+6 = 7+8 = 15，所以打印输出3个连续序列1-5，4-6，7-8。

'''

class Solution:

    def sumS2(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        curSum = small + big
        middle = (1 + tsum) / 2
        while small < middle:
            if curSum == tsum:
                self.PrintConSeq(small,big)
            while(curSum > tsum and small < middle):
                curSum = curSum - small
                small = small + 1
                if curSum == tsum:
                    self.PrintConSeq(small,big)
            big = big + 1
            curSum = curSum + big


    def PrintConSeq(self,small, big):
        # print (list(range(small,big+1)))
        for i in range(small, big + 1):
            print i,
        print " "
s = Solution()
print s.sumS2(15)

'''
解题思路：
1.使用big,small分别表示连个数表述序列的最大值和最小值, 初始化small = 1， big = 2
2.如果从small到big的序列和大于s，则可以从序列中去掉最小的值，也就是增大small的值
3.如果从small到big的和小于s，可以增大big，包含更多的数字。这个序列至少要有两个数，所以small一直增加到（1+s）/2
4.如果序列和正好为s，则存储，下一次，直接增加big，重复上面的过程

'''
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (1 + tsum) / 2
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(list(range(small, big + 1)))
            while curSum > tsum and small < middle:
                curSum = curSum - small
                small = small + 1
                if curSum == tsum:
                    output.append(list(range(small, big + 1)))
            big = big + 1
            curSum = curSum + big
        return output


