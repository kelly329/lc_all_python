# -*-coding:utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
参考学习：https://www.cnblogs.com/eilearn/p/9394203.html
'''
class Solution(object):
	'''
	问题一：是否存在路径和 leetcode112
	'''
	def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		if not root:
			return False
		
		if not root.left and not root.right and sum == root.val:
			return True
		left = self.hasPathSum(root.left, sum - root.val)
		right = self.hasPathSum(root.right, sum - root.val)
		return left or right
	'''
	问题二：返回所有和路径 leetcode113
	一定涉及回溯问题
	'''	
	def pathSum(self, root, sum):
		if not root:
			return []
		res, path = [], []
		self.findPath(self, root, res, path, sum)
		return res
	def findPath(self, root, res, path, sum):
		if not root:
			return
		
		path.append(root.val)
	
		if not root.left and not root.right and sum == root.val:
			# 一定要是list(path)
			res.append(list(path))
		
		self.findPath(root.left, res, path, sum - root.val)
		self.findPath(root.right, res, path, sum - root.val)
		
		path.pop()
	
	
	'''
	问题三：返回所有路径   leetcode257
	第一种：深度优先遍历 dfs
	第二种：dfs + stack
	'''	
	def binaryTreePaths_1(root):
		if not root:
			return []
		
		self.dfs(root, res, "")
		return res
	
	def dfs(root, res, path):
		if not root.left and not root.right:
			res.append(path + str(root.val))
		
		if root.left:
			dfs(root.left, res, path + str(root.val) + "->")
		if root.right:
			dfs(root.right, res, path + str(root.val) + "->")

	def binaryTreePaths_2(root):
		if not root:
			return []
		res, stacks = [], [(root, "")]
		while stacks:
			node, cur = stacks.pop()
			if not node.left and not node.right:
				res.append(cur + str(node.val))
			if node.left:
				stacks.append((root.left, cur + str(node.val) + "->"))
			if node.right:
				stacks.append((root.right, cur + str(node.val) + "->"))
		return res
	'''
	问题四：最大路径和 leetcode124
	参考学习：
	https://segmentfault.com/a/1190000018809913?utm_source=tag-newest
	https://www.jianshu.com/p/705f36310339
	'''
	import sys
	maxsum = -sys.maxsize
	def maxPathSum(root):
		maxSumDFS(root)
		return maxsum
	
	def maxSumDFS(root):
		if not root:
			return 0
		
		leftSum = max(0, maxSumDFS(root.left))
		rightSum = max(0, maxSumDFS(root.right))
		
		#以当前节点为最大路径和的根与全局变量最大值相比，尝试更新
		maxsum = max(maxsum, leftSum + rightSum + root.val)
		# 当前节点不为最大路径和根节点时，需要向父级节点返回此节点路径的最大和
		# 返回的是左右子树中最大的 + 当前结点的值作为这棵树的路径。因为必须要走根节点。
		return max(max(left, right) + root.val, 0)
		
		
		
			
		
	
		