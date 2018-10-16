# -*- coding:utf-8 -*-
'''
题目描述：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

class Solution:
    '''
    方法一：（空间换时间）使用一个新的数组先遍历原来数组把奇数存入，再次遍历把偶数存入，最后返回新数组即可
    '''
    def reOrderArrayI(self, array):
        res = []
        for i in range(len(array)):
            if array[i] % 2 == 1:
                res.append(array[i])
        for i in range(len(array)):
            if array[i] % 2 == 0:
                res.append(array[i])
        return res


    def reOrderArrayII(self, array):

        res = []
        out = []
        for i in range(len(array)):
            if array[i] % 2 == 1:
                res.append(array[i])
            else:
                out.append(array[i])
        return res + out

    '''
    方法三：类似冒泡排序的思想，前偶后奇进行交换
    '''
    def reOrderArrayIII(self, array):
        length = len(array)
        for i in range(length):
            for j in range(length - 1, i, -1):
                if array[j-1] % 2 == 0 and array[j] % 2 == 1:
                    change = array[j-1]
                    array[j-1] = array[j]
                    array[j] = change
        return array


s = Solution()
array = [2,3,8,9,11,23,14,19,20,20,32,11,17,19,33,55]
print s.reOrderArrayI(array)
print s.reOrderArrayII(array)
print s.reOrderArrayIII(array)