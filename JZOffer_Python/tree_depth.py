# -*- coding:utf-8 -*-
'''
题目描述：
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    '''
    递归
    '''
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        leDepth = self.TreeDepth(pRoot.left)
        riDepth = self.TreeDepth(pRoot.right)
        return max(leDepth, riDepth) + 1
    '''
    非递归：http://www.cnblogs.com/GF66/p/9785463.html
    '''
