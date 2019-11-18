# -*- coding:utf-8 -*-
'''
数组跳跃移动：
1. 处理参数，对于输入样例包括[, ]因此需要对输入做处理list(map(int, input()[1:-1].split(',')))
2. 越界的条件是当前下标+当前下标的值所得和大于等于数组长度或者小于0，即越界返回true；
永不越界条件，当前下标+当前下标的值所得和跳转到之前已经访问元素的下标，返回false
3. 使用临时数组记录当前元素是否已经访问。
'''

def is_skip(nums):
	if not nums or len(nums) == 0:
		return False
	temp = [0 for i in range(len(nums))]
	i = 0
	while i < len(nums):
		if temp[i] == 1:
			return False
		index = i + nums[i]
		if index >= len(nums) or index < 0:
			return True
		temp[i] = 1
		i = index
	return True


lists = list(map(int, input()[1:-1].split(',')))
if is_skip(lists):
	print("true")
else:
	print("false")