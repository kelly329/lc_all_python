class TrieNode:
	def __init__(self):
		self.zero = None
		self.one = None
class Solution(object):
	def findMaximumXOR(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		root = TrieNode()
		
		for num in nums:
			node = root
			for i in range(31, -1, -1):
				tmp = num & 1 << i
				if tmp:
					if not node.one:
						node.one = TrieNode()
					node = node.one
				else:
					if not node.zero:
						node.zero = TrieNode()
					node = node.zero
		
		ans = 0
		for num in nums:
			tmp_val = 0
			node = root
			for i in range(31, -1, -1):
				tmp = num & 1 << i
				if node.one and node.zero:
					if tmp:
						node = node.zero
					else:
						node = node.one
					tmp_val += 1 << i
				else:
					if (node.one and not tmp) or (node.zero and tmp):
						tmp_val += 1 << i
					node = node.one or node.zero
					
				
			ans = max(ans, tmp_val)
		return ans
		