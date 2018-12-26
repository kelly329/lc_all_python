# -*- coding:utf-8 -*-
'''
二分查找：时间复杂度：O(logn)
'''
def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

mist_dict = [1,4,7,9,10,20,40,60,89,100,120]
print binary_search(mist_dict, 20)
print binary_search(mist_dict, 111)