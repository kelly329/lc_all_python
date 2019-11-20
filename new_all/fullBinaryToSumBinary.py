# -*- coding:utf-8 -*-
'''
满二叉树转换为求和二叉树
1.构建二叉树
2.后序遍历二叉树进行求和
3.中序遍历二叉树
'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.sum = 0
class Solution:
	def constructTree(self, pre, tin):
		if not pre or not tin:
			return None
		
		root = TreeNode(pre[0])
		index = tin.index(pre[0])
		root.left = self.constructTree(pre[1 : index + 1], tin[:index + 1])
		root.right = self.constructTree(pre[index + 1:], tin[index + 1:])
		return root
	def postOrderSum(self, root):
		if not root:
			return
		self.postOrderSum(root.left)
		self.postOrderSum(root.right)
		if (root.left != None and root.right != None):
			root.sum = root.left.sum + root.left.val + root.right.sum + root.right.val
		elif (root.left != None):
			root.sum = root.left.sum + root.left.val
		elif(root.right != None):
			root.sum = root.right.sum + root.right.val
	# 后序遍历 进行求和
	def inOrder(self, root):
		if not root:
			return
		self.inOrder(root.left)
		print(root.sum, end = '\t')
		self.inOrder(root.right)
		
	def endResult(self, pre, tin):
		root = self.constructTree(pre, tin)
		self.postOrderSum(root)
		self.inOrder(root)
		
			
if __name__ == '__main__':
	solution = Solution()
	pre = list(map(int, input().split()))
	tin = list(map(int, input().split()))
	tree = solution.endResult(pre, tin)

#pre = [10, -2, 8, -4, 6, 7, 5]
#tin = [8, -2, -4, 10, 7, 6, 5]




		