# -*- coding:utf-8 -*-
'''
题目描述：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

'''
解题思路：
https://www.nowcoder.com/questionTerminal/72a5a919508a4251859fb2cfb987a0e6
'''

class Solution:
    def rectCover(self, number):
        num = []
        num.append(0)
        num.append(1)
        num.append(2)
        for i in range(3, number + 1):
            num.append(num[i-1] + num[i-2])
        return num[number]
s = Solution()
print s.rectCover(6)

