# -*- coding:utf-8 -*-
'''
题目描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

'''
题目分析:
对于本题，每次只有1阶，2阶两种跳法
1.假设第一次跳的是一阶，则剩余的(n-1)阶，有f(n-1)种跳法
2.假设第一次跳的是二阶，则剩余的(n-1)阶，有f(n-1)种跳法
3.则通过1和2可得，有n阶跳法有: f(n) = f(n -1) + f(n -2) 种跳法
4.通过实际情况，只有一阶的时候 f(1) = 1 ,只有两阶的时候可以有 f(2) = 2
5.可以发现最终得出的是一个斐波那契数列：
        
       | 1, (n=1)
f(n) = | 2, (n=2)
       | f(n-1)+f(n-2) ,(n>2,n为整数)
'''
class Solution:
    #递归的方式，此方法时间超时，时间复杂度高
    def jumpFloorI(self, number):
        if number <= 2:
            return number
        else:
            return self.jumpFloorI(number - 1) + self.jumpFloorI(number - 2)

    # 使用迭代方法 20ms
    def jumpFloorII(self, number):
        if number < 3:
            return number
        else:
            one, two = 1, 2
            for i in range(number - 2):
                one, two  = two, one + two
            return two

    # 使用数组的方式 30ms
    def jumpFloorIII(self, number):
        res = [1, 2]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        if number < 3:
            return number
        else:
            return res[number - 1]


