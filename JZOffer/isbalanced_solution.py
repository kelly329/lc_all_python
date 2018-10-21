# -*- coding:utf-8 -*-
'''
题目描述：
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True

        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)

        if abs(left-right) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        leDepth = self.TreeDepth(pRoot.left)
        riDepth = self.TreeDepth(pRoot.right)
        return max(leDepth, riDepth) + 1