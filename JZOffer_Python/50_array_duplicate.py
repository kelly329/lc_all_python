#!/usr/bin/python

# -*- coding:utf-8 -*-
class Solution:
	def duplicate(self, numbers, duplication):
		# write code here
		if not numbers or len(numbers) <= 0:
			return False
	
		for num in numbers:
			count = 0
			for item in numbers:
				
				if num == item:
					count += 1
				if count > 1:
					duplication[0] = item
					return duplication[0]
					break
		return False
		
#	运行时间：29ms
#
#	占用内存：5736k
	def duplications(self, nums, dups):
		if not nums or len(dups) <= 0:
			return False
		for i in range(len(nums)):
			    if (nums[i] < 0 ) or (nums[i] > len(nums) - 1):
				return False
		for i in range(len(nums)):
			
			while i != nums[i]:
				if nums[i] == nums[nums[i]]:
					dups[0] = nums[i]
					return True
		
				temp = nums[i]
				nums[i] = nums[temp]
				nums[temp] = temp
			
		return False
			
			
s = Solution()
print s.duplicate([2,1,3,0,4], [0])
print s.duplications([2,3,1,0,2,5,3], [0])			