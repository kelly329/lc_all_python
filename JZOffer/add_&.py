# -*- coding:utf-8 -*-
class Solution:

    '''
    思路二：
        首先看十进制是如何做的： 5+7=12，三步走
        第一步：相加各位的值，不算进位，得到2。
        第二步：计算进位值，得到10. 如果这一步的进位值为0，那么第一步得到的值就是最终结果。
        第三步：重复上述两步，只是相加的值变成上述两步的得到的结果2和10，得到12。
        同样我们可以用三步走的方式计算二进制值相加： 5-101，7-111 第一步：相加各位的值，不算进位，得到010，
        二进制每位相加就相当于各位做异或操作，101^111。
        第二步：计算进位值，得到1010，相当于各位做与操作得到101，再向左移一位得到1010，(101&111)<<1。
        第三步重复上述两步， 各位相加 010^1010=1000，进位值为100=(010&1010)<<1。
             继续重复上述两步：1000^100 = 1100，进位值为0，跳出循环，1100为最终结果。
    超时了
    '''
    def Add(self, num1, num2):
        while num2:
            num1, num2 = (num1 ^ num2), (num1 & num2) << 1
        return num1

    '''
    正确解法: 加法是异或，进位是与<<1
    python无符号又移位操作，需要建超越界
    python2.7中整数又int和long两种类型，int是固定位数的数，long则是理论上可以存储无限大数的数据类型，当数大到要溢出的时，为了避免溢出，
    python会把int转换为long。所以会使程序无限的算下去，这也是Python效率低的一个原因
    把num1规定成一个32位的数
    '''
    def AddSum(self, num1, num2):
        while num2:
            # 负数 负数& 0xFFFFFFFF 返回的数就成一个正数
            num1, num2 = (num1 ^ num2) & 0xFFFFFFFF, ((num1 & num2) << 1) & 0xFFFFFFFF

        # 0x7FFFFFFF long int的最大范围
        # ～取反 https://blog.csdn.net/u012559520/article/details/65630436
        return num1 if num1 <= 0x7FFFFFFF else ~(num1 ^ 0xFFFFFFFF)
        # -(~(num1 - 1) & 0xFFFFFFFF)


S = Solution()
print S.AddSum(2,-3)