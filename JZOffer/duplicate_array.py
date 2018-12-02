# -*- coding:utf-8 -*-
'''
题目描述：
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

解题思路：
1.如果数组中没有重复元素，当排好序后数字i将出现下标为i的位置。由于数组中有重复元素，有些位置可能存在多个数字，有些位置可能没有数组。
2.从头扫到尾，只要当前元素值与下标不同，就做一次判断,numbers[i]与numbers[numbers[i]]，相等就认为找到了
重复元素，返回true,否则就交换两者，继续循环。直到最后还没找到认为没找到重复元素，返回false
'''
class Solution:
	# 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
	# 函数返回True/False
	def duplicate(self, numbers, duplication):
		# write code here
		if not numbers or len(numbers) <= 0:
			return False
		for i in range(0, len(numbers)):
			if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
				return False
		for i in range(0, len(numbers)):
			while numbers[i] != i:
				if numbers[i] == numbers[numbers[i]]:
					duplication[0] = numbers[i]
					return True
				temp = numbers[i]
				numbers[i] = numbers[temp]
				numbers[temp] = temp
		return False
s = Solution()
print(s.duplicate([2,3,1,0,2,5,3], [0]))