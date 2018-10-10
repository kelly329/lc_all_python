# -*- coding:utf-8 -*-
'''
题目描述：找寻旋转数组中的最小值
给定一个按照已经旋转后数组，通过观察可以看出此数组并不是完全无需，其实要返回的数组中的最小值即为分开左右两边数组的分界值
'''

'''
思路：二分查找法
'''


# -*- coding:utf-8 -*-
class Solution:
    def MinNumber(self, rotateArray, left, right):
        res = rotateArray[left]
        for i in range(left, right + 1):
            if rotateArray[i] < res:
                res = rotateArray[i]
        return res

    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length == 0:
            return 0
        else:
            left = 0
            right = length - 1
            while left <= right:
                # 不做此处理时间会超时
                if (right - left) == 1:
                    return rotateArray[right]
                mid = (left + right) / 2
                # 如果出现大量重复(例如：[1,0,1,1,1])，只能顺序查找
                if rotateArray[mid] == rotateArray[left] and rotateArray[mid] == rotateArray[right]:
                    return self.MinNumber(rotateArray, left, right)
                elif rotateArray[mid] >= rotateArray[left]:
                    left = mid
                elif rotateArray[mid] <= rotateArray[right]:
                    right = mid
            return rotateArray[right]


s = Solution()
print s.minNumberInRotateArray([1, 0, 1, 1, 1])
print s.minNumberInRotateArray([3, 4, 5, 1, 2])
