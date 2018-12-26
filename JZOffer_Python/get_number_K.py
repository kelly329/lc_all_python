# -*- coding:utf-8 -*-
'''
题目描述：
统计一个数字在排序数组中出现的次数。
'''
class Solution:
    def GetNumberOfK(self, data, k):
        length = len(data)
        number = 0
        if length > 0:
            first = self.GetFirstK(data, k, length, 0, length - 1)
            end = self.GetEndK(data, k,length, 0, length-1)
            if first > -1 and end > -1:
                number = end - first + 1



        return number

    def GetFirstK(self, data, k, length, start, end):
        if start > end:
            return -1

        mid = (start + end) / 2
        midNumber = data[mid]

        if midNumber == k:
            # 数组只有一个数的情况
            if (data[mid - 1] != k and mid > 0) or mid == 0:
                return mid
            else:
                end = mid - 1
        elif midNumber > k:
            end = mid - 1
        else:
             start = mid + 1
        return self.GetFirstK(data, k, length, start, end)



    def GetEndK(self, data, k, length, start, end):
        if start > end:
            return -1

        mid = (start + end) / 2
        midNumber = data[mid]



        if midNumber == k:

            '''
            这种情况会出现：list index out of range（对于数组长度只有1的情况）
            把or两边的顺序变换一下就可以啦（and与or的使用问题）
            https://www.cnblogs.com/qiezizi/articles/6005055.html
            and 如果上下布尔值都为真，返回最后一个值，如果有一个为假则返回第一个假值
            or 如果上下文如果第一个为真，则or立刻返回该值，如果所有为假，则返回最后一个假值
            '''
            if (mid < length - 1 and data[mid + 1] != k ) or mid == length - 1 : # and（返回mid < length - 1）假之后再or 返回mid == length - 1
            # if (data[mid + 1] != k and mid < length - 1) or mid == length - 1 : # and中返回（第一个假data[mid + 1] != k）所以出现越界情况
            # 要考虑数组只有一个数的情况
            # if  mid == length - 1 or (data[mid + 1] != k and mid < length - 1):  #直接返回 mid == length - 1
                return mid
            else:
                start = mid + 1
        elif midNumber > k:
            start = mid + 1
        else:
            end = mid - 1



        return self.GetEndK(data, k, length, start, end)









s = Solution()
print s.GetNumberOfK([1,2,3,3,3,3,4,5],3)
print s.GetNumberOfK([3],3)
print s.GetNumberOfK([4],3)