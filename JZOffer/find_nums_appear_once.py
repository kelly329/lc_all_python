# -*- coding:utf-8 -*-
'''
题目描述：
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
'''

'''
解题思路：
https://blog.csdn.net/lrs1353281004/article/details/81187971
https://blog.csdn.net/fuxuemingzhu/article/details/79688059
1.异或运算，两个相同的数异或为0，一个数和0异或仍未本身，所以整个数组最后的异或结果即为两个只出现一次数的异或结果
依照这个思路，我们来看两个数（我们假设是AB）出现一次的数组。我们首先还是先异或，剩下的数字肯定是A、B异或的结果，
这个结果的二进制中的1，表现的是A和B的不同的位。我们就取第一个1所在的位数，假设是第3位，接着把原数组分成两组，分组标准是第3位是否为1。
如此，相同的数肯定在一个组，因为相同数字所有位都相同，而不同的数，肯定不在一组。
然后把这两个组按照最开始的思路，依次异或，剩余的两个结果就是这两个只出现一次的数字。
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array:
            return 0
        # 得出两个不同数字的异或结果
        xor = 0
        for e in array:
            xor = xor ^ e
        mask = 1
        # 算出异或结果为1位 1010 & 0001 = 0   1011 & 0001 = 0001
        while xor & 1 == 0:
            mask <<= 1 # 0010

        num1, num2 = 0, 0

        # 把数组分为两个部分，第几位是否为1（两个不同的数字不可能第几位同时为1）
        for ele in array:
            if mask & ele == 0:
                num1 = ele ^ num1
            else:
                num2 = ele ^ num2
        return [num1, num2]

