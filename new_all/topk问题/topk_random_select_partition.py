# -*- coding:utf-8 -*- 
# 平均的时间复杂度是O(nlogk), 期望时间复杂度为O(n)
# partition的时间复杂度为O(n)
def randomized_sort_topk(array, start, end, k):
	if start == end:
		return array[start]
	left, right = start, end
	pivot = array[start]
	while left < right:
		while left < right and array[right] < pivot:
			right -= 1
		while left < right and array[left] >= pivot:
			left += 1
		array[left], array[right] = array[right], array[left]
	array[start], array[left] = array[left], array[start]

	if (left - start + 1 > k):
		return randomized_sort_topk(array, start, left - 1, k)
	elif (left - start + 1 == k):
		return array[left]
	else:
		return randomized_sort_topk(array, left + 1, end, k - (left - start + 1))

def topk(array, start, end, k):
	k_value = randomized_sort_topk(array, start, end, k)
	while start < end:
		while start < end and array[end] < k_value:
			end -= 1
		while start < end and array[start] >= k_value:
			start += 1
		array[start], array[end] = array[end], array[start]
	
	return array[:k]

array = [5,3,7,1,8,2,9,4,7,2,6,6]
print(topk(array, 0, len(array) - 1, 5))