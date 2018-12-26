# -*- coding:utf-8 -*-
class Solution:

    '''
    思路一：常规方法


    def __init__(self):
        self.array = []

    def Insert(self, num):
        self.array.append(num)
        self.array.sort()


    def GetMedian(self):
        length = len(self.array)

        if length % 2 == 1:
            return self.array[length // 2]
        return (self.array[length // 2] + self.array[length // 2 - 1]) / 2.0
    '''




    '''
    思路二：最大堆 + 最小堆
    为了保证插入新数据和取中位数的时间效率都高效，使用最大堆与最小堆容器，并且满足：
    1.两个堆中的数据数目不能超过1，这样使中位数只出现两个堆的交接处；
    2.大顶堆的所有数据都小于小顶堆，这样满足排序要求。
    
    -构建一个最大堆和一个最小堆，分别存储比中位数小的数和大的数
    -当目前两个堆的总数为偶数的时候，把数字存入最大堆，然后宠排最大堆，如果最大堆的堆顶数字大于最小堆的顶数字，
    则把两个堆顶元素交换，重新排序两堆，此时两个堆的总数为奇数，直接输出最大堆顶数字即为中位数；
    -当目前两个堆的总数为奇数的时候，把数字存入最小堆，重新排堆，如果最大堆的堆顶数字大于最小堆的顶数字，
    则把两个堆顶元素交换，重新排序两堆，此时两个堆的总数为偶数，取两堆堆顶数字做平均即为中位数。
    
    最大堆堆顶元素要小于最小堆的堆顶元素，最大堆，堆顶元素最大，最小堆堆顶元素最小，从小到大，这样最大堆所有元素均小于最小堆，
    中位数一定出现在两堆交替之间。
    
    '''
    def __init__(self):
        self.left = []
        self.righ = []
        self.count = 0
    def Insert(self, num):
        # 1 & 1 == 1
        if self.count & 1 == 0:
            self.left.append(num)
        else:
            self.righ.append(num)
        self.count += 1

    def GetMedian(self, x):
        if self.count == 1:
            return self.left[0]

        self.MaxHeap(self.left)
        self.MinHeap(self.righ)
        if self.left[0] > self.righ[0]:
            self.left[0], self.righ[0] = self.righ[0], self.left[0]

        self.MaxHeap(self.left)
        self.MinHeap(self.righ)

        '''
        1 & 1 == 1
        1 & 0 == 0
        0 & 1 == 0
        0 & 0 == 0
        '''
        if self.count & 1 == 0:
            return (self.left[0] + self.righ[0]) / 2.0
        else:
            return self.left[0]


    def MaxHeap(self,alist):
        length = len(alist)

        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        # 最大堆排序 非叶子节点（从最后一个非叶子节点开始）
        '''
        最后一个非叶结点：length / 2 - 1 k
        非叶结点的子结点：2k + 1 2k + 2
        range(start, stop, step)

        从-1开始， 到-5结束， 每次增加-1

        那么就是 
        [-1, -2, -3, -4]
        '''
        for i in range(length // 2 - 1, -1, -1):
            # print i alist[i]
            k = i
            temp = alist[k]
            heap = False

            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] < alist[index + 1]:
                        index += 1
                if temp >= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp

    def MinHeap(self,alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist

        for i in range(length // 2 - 1, -1, -1):
            k = i
            temp = alist[k]
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] > alist[index + 1]:
                        index += 1
                if temp <= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp







s = Solution()
s.MaxHeap([4,6,8,5,9])