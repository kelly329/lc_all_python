# -*- coding:utf-8 -*-
'''
题目描述：现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
'''

class Solution:
    '''
    思路：不使用递归，把时间复杂度 O(n)
    '''
    def Fibonacci(self, n):
        a, b = 0, 1
        for i in range(n):
            # print i
            a, b = b, a+b
        return a
    '''
    思路：使用递归 此方法在剑纸offer不通过
    ，当使用递归方法实现时，时间复杂度和空间复杂度都太大。
    由于函数调用自身，而函数调用是有时间和空间消耗的：
    每一次函数调用，都需要在内存栈中分配空间以保存参数，返回地址及临时变量，而且往栈里压入数据和弹出数据都需要时间。
    '''
    def Fibonaccis(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.Fibonaccis(n - 1) + self.Fibonaccis(n - 2)

solution = Solution()
print solution.Fibonacci(3)
print solution.Fibonaccis(3)