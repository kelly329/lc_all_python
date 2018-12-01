# -*- coding:utf-8 -*-
'''
约瑟夫环问题：
https://www.nowcoder.com/questionTerminal/f78a359491e64a50bce2d89cff857eb6
'''
class Solution:
	def LastRemaining_Solution(self, n, m):
		# write code here
		if n < 1 or m < 1:
			return -1
		last = 0
		for i in range(2,n + 1):
			last = (last + m) % i
		return last