def maxThird(nums):
	nums = sorted(nums, reverse = True)
	print(nums[2])
'''
先从右边开始移动再移动左边！！！！！
'''
def maxThirdPartition(nums, start, end, k):
	if start == end:
		return nums[start]
	pivot = nums[start]
	left, right = start, end
	while left < right:
		while left < right and nums[right] < pivot:
			right -= 1
		while left < right and nums[left] >= pivot:
			left += 1
		nums[left], nums[right] = nums[right], nums[left]
	nums[start], nums[left] = nums[left], nums[start]
	print(nums)
	if (left - start + 1) > k:
		return maxThirdPartition(nums, start, left - 1, k)
	elif (left - start + 1 == k):
		return nums[left]
	else:
		return maxThirdPartition(nums, left + 1, end, k - (left - start + 1))
	

	
nums = list(map(int, input()[1:-1].split(',')))
print(maxThirdPartition(nums, 0, len(nums) - 1, 3))
