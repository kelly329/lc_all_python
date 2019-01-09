# -*- coding:utf-8 -*-
运行时间：26ms

占用内存：5728k
# -*- coding:utf-8 -*-
class Solution:
	# 返回[a,b] 其中ab是出现一次的两个数字
	def FindNumsAppearOnce(self, array):
		# write code here
		if not array or len(array) <= 0:
			return []
		resOR = 0
		for arr in array:
			resOR ^= arr
#		print(bin(resOR).replace('0b',''))
		# 二进制从右向左 右为最地位 从0开始计数
		findOneLocation = self.FindLocationOne(resOR)
#		print(findOneLocation)
		num1, num2 = 0, 0
		for arr in array:
			if self.IsSameLocation(arr, findOneLocation):
				num1 ^= arr
			else:
				num2 ^= arr
		return num1, num2
		
	def FindLocationOne(self, num):
		bitCount = 0
		while num & 1 == 0 and bitCount <= 32:
			bitCount += 1
			num = num >> 1
		return bitCount
	def IsSameLocation(self, num, location):
		num = num >> location
		return num & 1
s = Solution()
print(s.FindNumsAppearOnce([2,4,3,6,3,2,5,5]))
			