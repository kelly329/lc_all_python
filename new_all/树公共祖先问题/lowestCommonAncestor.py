# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	'''
	问题一：二叉搜索树最近公共祖先
	'''
	def lowestCommonAncestor_1(self, root, p, q):
		if not root:
			return None
		
		if root.val > p.val and root.val > q.val:
			return self.lowestCommonAncestor(root.left, p, q)
		if root.val < p.val and root.val < q.val:
			return self.lowestCommonAncestor(root.right, p, q)
		
		return root
	'''
	问题二：普通二叉树最近公共祖先
	- 如果根节点为空，直接返回空
	- 如果根节点为其中一个节点，直接返回根节点
	- 如果查找的两个节点在根节点的两侧，直接返回根节点
	- 如果在根节点的一侧，那么这一侧重复以上操作
	对树深度遍历感受：针对一个根节点，完成完整的操作逻辑，之后左，右节点直接重复，递归即可
	'''
	def lowestCommonAncestor_2(self, root, p, q):
		# 如果当前节点为空，直接返回None
		if not root:
			return None
		
		# 如果当前节点为其中一个节点，则返回当前节点
		if root == p or root == q:
			return root
		left = self.lowestCommonAncestor_2(root.left, p, q)
		right = self.lowestCommonAncestor_2(root.right, p, q)
		
		if left and right:
			return root
		
		return left if left else right
	