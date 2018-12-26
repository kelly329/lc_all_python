# -*- coding:utf-8 -*-
'''
题目描述：
和为s的两个数字
输入一个递增的排序数组和一个数字s，在数组中查找两个数，使得它们的和正好为s。
如果有多对数和等于s，则输出任意一对即可。

例如输入数组{1,2,4,7,11,15}和数字15.
思路：1.时间复杂度为O(n^2),两个for循环嵌套
2.时间复杂度为O(n)
声明两个指针，一个在数组头部，一个在尾部，如果两个数和大于s，则尾部指针向前移动，如果和小于s，头部指针向前移动，知道连个指针相遇
'''

class Solution:

    def sumS1(self, data, s):
        if not data:
            return False
        found = False
        left = 0
        right = len(data) - 1
        while left < right:

            curSum = data[left] + data[right]
            if curSum == s:
                return data[left], data[right]
                # found = True
                # break
            elif curSum > s:
                right = right - 1
            else:
                left = left + 1
        return found

s = Solution()
print s.sumS1([1,2,4,7,11,15],15)

'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
其实这种方法找到的就是两个数乘积最小的。
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if array == None or len(array) <= 0 or array[-1] + array[-2] < tsum:
            return []
        left = 0
        right = len(array) - 1

        while left < right:
            curSum = array[left] + array[right]
            if curSum == tsum:
                return array[left], array[right]
            elif curSum > tsum:
                right -= 1
            else:
                left += 1
        return []


