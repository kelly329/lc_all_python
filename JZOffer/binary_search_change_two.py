# -*- coding:utf-8 -*-
def binary_serach_change(target, array):

    rows = len(array)
    cols = len(array[0]) - 1

    i = rows - 1
    j = 0
    # 在python中 &&使用and
    while i >= 0 and j <= cols:
        if array[i][j] < target:
            j +=  1
        elif array[i][j] > target:
            i -= 1
        else:
            # 在python中 true与false首字母要大写
            return True
    return False

mist_dict = [[1,2,8,9],[2,4,9,10],[4,7,10,13],[6,8,11,15]]
print binary_serach_change(7, mist_dict)
print binary_serach_change(20, mist_dict)