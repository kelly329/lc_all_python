# -*- coding:utf-8 -*-
'''
题目描述：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == [] or k > len(tinput):
            return []
        tinput = self.quickSort(tinput)
        return tinput[:k]

    def quickSort(self, tinput):
        if len(tinput) < 2:
            return tinput
        else:
            pivot = tinput[0]
            less = [i for i in tinput[1:] if i < pivot]
            greater = [i for i in tinput[1:] if i > pivot]
            return self.quickSort(less) + [pivot] + self.quickSort(greater)


s = Solution()
tinput = [10, 5, 2, 3]
k = 3
print s.GetLeastNumbers_Solution(tinput, k)