def maxInWindows(nums, size):
	if not nums or size == 1:
		return nums
	res = []
	for i in range(len(nums) - size + 1):
		j = i
		count = size
		maxs = nums[i]
		while count > 0:
			if nums[j] > maxs:
				maxs = nums[j]
			j += 1
			count -= 1
		res.append(maxs)
	return res

def maxInWindowsQueue(nums, size):
	if not nums or len(nums) <= 0 or size == 0 or size > len(nums):
		return []
	
	maxqueue, maxlist = [], []
	for i in range(len(nums)):
		if maxqueue and  i - maxqueue[0] >= size:
			maxqueue.pop(0)
		while maxqueue and nums[i] >= nums[maxqueue[-1]]:
			maxqueue.pop()
		
		maxqueue.append(i)
		if i >= size - 1:
			maxlist.append(nums[maxqueue[0]])
	return maxlist

			
	
print(maxInWindowsQueue([2,3,4,2,6,2,5,1], 3))			
print(maxInWindows([2,3,4,2,6,2,5,1], 3))