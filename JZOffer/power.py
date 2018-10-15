# -*- coding:utf-8 -*-
'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''
'''
知识点：
>>表示带符号右移，如：int i=15; i>>2的结果是3，移出的部分将被抛弃。
转为二进制的形式可能更好理解，0000 1111(15)右移2位的结果是0000 0011(3)，0001 1010(18)右移3位的结果是0000 0011(3)。



n & 1 等价于 (n % 2) == 1

n >>= 1 等价于 n /= 2
'''
class Solution:

    #基本方法
    def Power(self, base, exponent):
        # 0的次幂无法求
        if base == 0:
            return 0
        e = abs(exponent)
        res = base
        if exponent == 0:
            return 1
        while e > 1:
            res *= base
            e -= 1
        return res if exponent > 0 else 1/res

    #快速幂排序

    def Powered(self, base, exponent):
        res = 1
        e = abs(exponent)
        tmp = base

        while e > 0:
            if e & 1 == 1:
                res = res * tmp
            e = e>>1
            tmp = tmp * tmp
        return res if exponent > 0 else 1/res



s = Solution()

print s.Power(2,3)
print s.Powered(2,3)