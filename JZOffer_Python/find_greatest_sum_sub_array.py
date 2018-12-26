# -*- coding:utf-8 -*-
'''
题目描述：
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和
'''
'''
解题思路：动态规划
需要考虑的问题：最大和为0 以及 数组长度为0时返回的区别
功能测试：全是正数，负数，正负都有
分析：{6,-3,-2,7,-15,1,2,2}
F(i): 以array[i]为末尾元素的子数组的和的最大值，子数组的元素的相对位置不变
F(i) = max(F(i-1) + array[i], array[i])
所有子数组和的最大值
res = max(res, F(i))
F(0) = 6
res = 6

F(1) = max(F(0) -3, -3) = max(3,-3) = 3
res = max(6, 3) = 6

F(2) = max(F(1) - 2, -2) = max(1, -2) = 1
res = max(6, 1) = 6

F(3) = max(F(2) + 7, 7) = max(8, 7) = 8
res = max(6, 8) = 8

F(4) = max(F(3) - 15, -15) = max(-7, -15) = -7
res = max(8, -7) = 8

F(5) = max(F(4) + 1, 1) = max(-6, 1) = 1
res = max(8, 1) = 8

F(6) = max(F(5) + 2, 2) = max(3, 2) = 3
res = max(8, 3) = 8

F(7) = max(F(6) + 2, 2) = max(5, 2) = 5
res = max(8, 3) = 8
最终res = 8

'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == []:
            return False
        # 记录当前所有子数组的和的最大值
        res = array[0]
        # 包含array[i]的连续数组最大值
        fx = array[0]
        for i in range(1, len(array)):
            fx = max(fx + array[i], array[i])
            res = max(res, fx)
        return res

