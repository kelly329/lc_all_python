# -*- coding:utf-8 -*-
'''
题目描述：
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

解题思路：
   B[0] = A[1] * A[2] * A[3] * A[4] *....*A[n-1] ;（没有A[0]）
   B[1 ]= A[0] * A[2] * A[3] * A[4] *....*A[n-1] ;（没有A[1]）
   B[2] = A[0] * A[1] * A[3] * A[4] *....*A[n-1] ;（没有A[2]）
   相当于一个矩形，被省去的那个数字设为1，这样的话，先把上三角的数一行一行撑起来，接着在和下三角的数相乘，节省空间



对于第一个for循环
上三角型
第一步：b[0] = 1;
第二步：b[1] = b[0] * a[0] = a[0]
第三步：b[2] = b[1] * a[1] = a[0] * a[1];
第四步：b[3] = b[2] * a[2] = a[0] * a[1] * a[2];
第五步：b[4] = b[3] * a[3] = a[0] * a[1] * a[2] * a[3];

下三角型，自下向上
第一步
temp *= a[4] = a[4];
b[3] = b[3] * temp = a[0] * a[1] * a[2] * a[4];
第二步
temp *= a[3] = a[4] * a[3];
b[2] = b[2] * temp = a[0] * a[1] * a[4] * a[3];
第三步
temp *= a[2] = a[4] * a[3] * a[2];
b[1] = b[1] * temp = a[0] * a[4] * a[3] * a[2];
第四步
temp *= a[1] = a[4] * a[3] * a[2] * a[1];
b[0] = b[0] * temp = a[4] * a[3] * a[2] * a[1];


运行时间：28ms

占用内存：5732k
'''
class Solution:
    def multiply(self, A):
        if not A or len(A)<0:
            return 0
        length = len(A)
        B = [1] * length
        # 上三角
        for i in range(1, length):
            B[i] = B[i - 1] * A[i - 1]
        temp = 1
        for i in range(length - 2, -1, -1):
            temp = temp * A[i + 1]
            B[i] *= temp
        return B

S = Solution()
print S.multiply([1,2,3,4,5])
