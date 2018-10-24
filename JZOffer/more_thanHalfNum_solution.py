# -*- coding:utf-8 -*-
'''
题目描述：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0。
'''

'''
解题思路：
https://blog.csdn.net/u011489043/article/details/76422965
首先是输入是数字，介于0～9之间。
所以我们可以首先建立一个含有10个元素的数组，然后用输入的数字作为下标以统计每个数字出现的次数。再对这个数组与长度的一半进行比较，输出结果。
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        length = len(numbers)

        arr = [0 for i in range(10)]
        for ele in numbers:
            arr[ele] = arr[ele] + 1

        for i in range(0, 10):
            if arr[i] > length / 2:
                return i
        return 0


