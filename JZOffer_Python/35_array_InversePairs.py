#!/usr/bin/python

运行时间：3798ms

占用内存：23144k

在每次程序进入26行时，此时的data是最新的排序结果，copy是次新的结果。
	在最后一次进入26行以后时，copy为完整排序后的结果，data是次新的结果。
	然而这里第一个类内函数调用第二个函数时，data和copy的顺序没有改变，所以最后结果应该copy是完整排序的结果.data是差一步完成排序的结果。以输入[7,5,6,4], 最后的结果copy[4,5,6,7], data[5,7,4,6].
	
000000007 是最小的十位质数。模1000000007，可以保证值永远在int的范围内。
	
class Solution:
	def InversePairs(self, data):
		if not data:
			return 0
		copy = [i for i in data]
		return self.InverseCore(copy, data, 0, len(data) - 1) % 1000000007 
	def InverseCore(self, copy, data, start, end):
		if start >= end:
			copy[start] = data[start]
			return 0
		mid = (start + end) / 2
		left = self.InverseCore(data, copy, start, mid)
		right = self.InverseCore(data, copy, mid + 1,end)
		
		count = 0
		i = start
		j = mid + 1
		index = start
		
		while i <= mid and j <= end:
			if data[i] <= data[j]:
				copy[index] = data[i]
				i += 1
			else:
				copy[index] = data[j]
				count += mid - i + 1
				j += 1
			index += 1
		while i <= mid:
			copy[index] = data[i]
			index += 1
			i += 1
		while j <= end:
			copy[index] = data[j]
			index += 1
			j += 1
		return (left + right + count)
		