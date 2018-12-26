# -*- coding:utf-8 -*-
'''
题目描述：
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''

'''
解题思路：
http://cuijiahua.com/blog/2017/12/basis_23.html
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        length = len(sequence)
        if length == 1:
            return True
        root = sequence[-1]
        i = 0
        for i in range(length - 1):
            if sequence[i] < root:
                i = i + 1
        k = i
        #右子树的数都要比左子树大，存在小的结束返回fasle即可
        for i in range(k, length - 1):
            if sequence[i] < root:
                return False

        # python数组的范围前开后闭
        # 其实right就不用包括最后一个root
        left_s = sequence[:k]
        right_s = sequence[k:length-1]

        left = True
        right = True
        if len(left_s):
            left = self.VerifySquenceOfBST(left_s)
        if len(right_s):
            right = self.VerifySquenceOfBST(right_s)

        return left and right

