# -*- coding:utf-8 -*-
'''
题目描述：
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

class Solution:
    def Sum_Solution(self, n):
        # write code here
        return sum(list(range(1,n+1)))



    def Sum(self, n):
        # write code here
        # and的话在n == 0 的时候就直接短路返回0了，就结束递归了
        return n and (n + self.Sum(n-1))
