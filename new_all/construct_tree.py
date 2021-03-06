# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
构建二叉树==》 在pre，tin为空时，返回值的处理none
'''
class Solution:
	# 返回构造的TreeNode根节点
	def reConstructBinaryTree(self, pre, tin):
		# write code here
		if not pre or not tin:
			return None
		root = TreeNode(pre[0])
		index = tin.index(pre[0])
		root.left = self.reConstructBinaryTree(pre[1:index + 1], tin[:index])
		root.right = self.reConstructBinaryTree(pre[index + 1:], tin[index+1:])
		return root
		
		 