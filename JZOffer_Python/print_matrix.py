# -*- coding:utf-8 -*-
'''
题目描述：
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

'''
解题思路：
https://www.cnblogs.com/wanglei5205/p/8617424.html
'''

class Solution:

    def printMatrix(self,matrix):

        if not matrix:
            return matrix

        result = []
        length = len(matrix)

        top = 0
        left = 0
        right = len(matrix[0]) - 1
        btm = length - 1

        while top <= btm and left <= right:

            for i in range(left, right+1):
                result.append(matrix[top][i])
            if top < btm:
                for i in range(top + 1,btm + 1):
                    result.append(matrix[i][right])
            if top < btm and left < right:
                for i in range(right-1, left, -1):
                    result.append(matrix[btm][i])
            if top + 1 < btm and left < right:
                for i in range(btm - 1, top, -1):
                    result.append(matrix[i][left])

            left = left + 1
            right = right - 1
            top = top + 1
            btm = btm - 1

        return result





