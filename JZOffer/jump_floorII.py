# -*- coding:utf-8 -*-
'''
题目描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

'''
题目思路：链接：https://www.nowcoder.com/questionTerminal/22243d016f6b47f2a6928b4313c85387 
1.根据题目的题意可知,第一次跳有 1, 2, 3, 4 ..... n种跳法
2.若第一次跳1，则剩余的(n-1)阶，有f(n-1)种跳法
  若第一次跳2，则剩余的(n-2)阶，有f(n-2)种跳法
  所以f(n)=f(n-1)+f(n-2)+...+f(1)
  因为f(n-1)=f(n-2)+f(n-3)+...+f(1)
  所以f(n)=2*f(n-1)
'''

class Solution:
    '''
    递归的方式： 27ms 5728k
    '''
    def jumpFloorI(self, number):
        if number <= 0:
            return -1
        elif number == 1:
            return 1
        else:
            return 2 * self.jumpFloorI(number - 1)

    '''
    第二种做法：f(n)=2f(n-1)是等比数列，首项为1，比例 为2，f(n)=2^(n-1)  23ms 5748k
    '''
    def jumpFloorII(self, number):
        return 2**(number - 1)