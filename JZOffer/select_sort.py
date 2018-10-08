# -*- coding:utf-8 -*-
'''
选择排序：时间复杂度：O(n^2)
'''
def findMin(array):
    min = array[0]
    min_index = 0
    # for循环实现
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
            min_index = i
    return min_index
    # while循环实现
    # i = 1
    # while i <= len(array) - 1:
    #     if array[i] >= min:
    #         i += 1
    #     else:
    #         min = array[i]
    #         min_index = i
    # return min_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        minIndex = findMin(arr)
        print minIndex
        newArr.append(arr.pop(minIndex))
    return newArr


list = [1,4,2,7,9,0,-1]
print selectionSort(list)