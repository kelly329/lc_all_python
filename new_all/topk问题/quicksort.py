#-*- coding:utf-8 -*-
# 稳定性：排序后 2 个相等键值的顺序和排序之前它们的顺序相同
# 快速排序：不稳定，平均时间复杂度为O(NlogN) 最好：O(NlogN)， 最坏：O(N*N)空间复杂度O(logN)
# partition的时间复杂度是O(n)
def quicksort(array, left, right):
	if left < right:
		index = partition(array, left, right)
		quicksort(array, left, index - 1)
		quicksort(array, index + 1, right)
	return array

def partition(array, left, right):
	pivot = array[left]
	start = left
	while left < right:
		while left < right and array[right] > pivot:
			right -= 1
		while left < right and array[left] <= pivot:
			left += 1
		
		array[left], array[right] = array[right], array[left]
		
	array[start], array[left] = array[left], array[start]
	return left


array = [2,8,9,3,2,10,7,0,1,4,0]
print(quicksort(array, 0, len(array) - 1))