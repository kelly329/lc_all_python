# -*- coding:utf-8 -*-
'''
题目描述：
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值
分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
 {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
  {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

解题思路：
思路一：
遍历数组，从数组第w-1位开始，每次移动一位，并计算窗口w的最大值。

时间复杂度：

计算窗口的最大值需O(w)，移动n-w+1次，时间复杂度为O(nw)

思路二：双队列法
https://blog.csdn.net/qq_20141867/article/details/81088705
'''
class Solution:
    def maxInWindows(self, num, size):
        result = []
        numlength = len(num)
        if not num or numlength <= 0 or size == 0 or size > numlength:
            return result
        for i in range(0, numlength - size + 1):
            #curnum = self.getMax(num[i:], size)
            '''
             curnum = self.getMax(num[i:i + size - 1], size)
             数组越界，因为python数组的截取，不包括后面的[0:3]截取前3个元素，0，1，2
            '''
            curnum = self.getMax(num[i:i + size], size)
            result.append(curnum)
        return result


    def getMax(self, num, size):
        curmax = num[0]
        for i in range(size):
            if num[i] > curmax:
                curmax = num[i]
        return curmax



    def maxWindows(self, num, size):
        result = []
        numlength = len(num)
        if not num or numlength <= 0 or size == 0 or size > numlength:
            return result
        if size == 1:
            return num
        # 可能是最大值的下标
        maxqueue = []
        # 存放窗口中的最大值
        maxlist = []
        for i in range(len(num)):
            # 判断队列中的首下标是否已经超出滑动窗口
            if len(maxqueue) > 0 and i - size >= maxqueue[0]:
                maxqueue.pop(0)
            while len(maxqueue) > 0 and num[i] > num[maxqueue[-1]]:
                # 如果新来的元素比队列最后一个元素大，则将最后一个元素退出
                maxqueue.pop()

            maxqueue.append(i)
            if i >= size - 1:
                # 如果遍历的元素已经达到一个滑动窗口的大小，就开始提取窗口的最大值了
                maxlist.append(num[maxqueue[0]])
        return maxlist



s = Solution()
num = [2,3,4,2,6,2,5,1]
print s.maxInWindows(num,3)
print s.maxWindows(num,3)