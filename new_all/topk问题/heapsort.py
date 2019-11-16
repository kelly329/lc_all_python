#-*- coding:utf-8 -*-
# 稳定性：排序后 2 个相等键值的顺序和排序之前它们的顺序相同
# 堆排序：不稳定 
# 平均时间复杂度为O(NlogN) 最好：O(NlogN) 最坏：O(NlogN)  空间复杂度O(1)
def heap_sort(array):
	if not array or len(array) == 1:
		return array
	for i in range(len(array) // 2 - 1, -1, -1):
		heap_detail(array, i, len(array))
	
	for i in range(len(array) - 1, 0, -1):
		array[0], array[i] = array[i], array[0]
		heap_detail(array, 0, i)
	return array


def heap_detail(array, start, end):
	index = start
	left = 2 * index + 1
	right = 2 * index + 2
	if left < end and array[index] > array[left]:
		index = left
	if right < end and array[index] > array[right]:
		index = right
	if index != start:
		array[index], array[start] = array[start], array[index]
		heap_detail(array, index, end)
	
	
array = [2,8,9,3,10,7,0,6,2,9]
print(heap_sort(array))