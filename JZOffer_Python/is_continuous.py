# -*- coding:utf-8 -*-
'''
题目描述：扑克牌中的顺子
题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即5张牌是不是连续的。
2-10为数字本身，A:1 J:11 Q:12 K:13,而大小王可以看成任意数字，为0。

解题思路：
1. 首先把数组排序
2.统计数组中0的个数
3.最后统计排序之后的数组中相邻数字之间的空缺总数，如果空缺总数小于或者等于0的个数，那么数组就是连续的；反之则不连续
注意：输入数组中非0数字重复出现，则该数组时不连续的。

'''
class Solution:
    def IsContinuous(self, numbers):
	# write code here
	numZero = 0
	numInterval = 0
	length = len(numbers)
	if length <= 0:
		return False
	numbers.sort()
	for i in range(0,length-1):
		if numbers[i] == 0:
			numZero += 1
			continue
		if numbers[i] == numbers[i+1]:
			return False
		 numInterval += numbers[i + 1] - numbers[i] - 1
		if numInterval > 4:
			return False
	if numZero >= numInterval:
		return True
	return False
			
		
	