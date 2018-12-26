# -*- coding:utf-8 -*-
'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

'''
知识点：
0xffffffff  十六进制数 
换算为二进制： 1111 1111 1111 1111 1111 1111 1111 1111     32位都是1


&是二进制“与”运算，参加运算的两个数的二进制按位进行运算，运算的规律是：
0 & 0=0
0 & 1=0
1 & 0=0
1 & 1=1


给定数的补码：
正整数的补码是其二进制表示，与原码相同
求负整数的补码，将其对应正数二进制表示所有位取反（包括符号位，0变1，1变0）后加1
【例2】求-5的补码。
-5对应正数5（00000101）→所有位取反（11111010）→加1(11111011)
python要使用n & 0xffffffff得到一个数的补码
'''


'''
思路：
思路二：把一个整数n减去1，再和原来的整数与运算，会把该整数的最右边的1变成0，
那么，一个整数的二进制中有多少个1，就可以进行多少次这样的操作。循环结束的条件是n为0；
'''

class Solution:
    def NumberOf1(self, number):
        return bin(number & 0xffffffff).count('1')

    def NumberOf1s(self, number):
        count = 0
        while number & 0xffffff != 0:
            count += 1
            number = number & (number - 1)
        return count
s = Solution()
print s.NumberOf1(7)
print s.NumberOf1s(7)
