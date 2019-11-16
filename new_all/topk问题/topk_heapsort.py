# -*- coding:utf-8 -*-
# topk使用堆排序，时间复杂度为O(n*logk)
def heap_sort_topk(array, k):
	for i in range(k // 2 - 1, -1, -1):
		heap_detail(array, i, k)
	for i in range(k, len(array)):
		if array[i] > array[0]:
			array[i], array[0] = array[0], array[i]
			heap_detail(array, 0, k - 1)
	return array[:k]

def heap_detail(array, start, end):
	index = start
	left = 2 * index + 1
	right = 2 * index + 2
	if left < end and array[index] > array[left]:
		index = left
	if right < end and array[index] > array[right]:
		index = right
	if index != start:
		array[start], array[index] = array[index], array[start]
		heap_detail(array, index, end)


array = [5,3,7,1,8,2,9,4,7,2,6,6]
print(heap_sort_topk(array, 5))
	