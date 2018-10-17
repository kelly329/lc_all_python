# -*- coding:utf-8 -*-
''''
题目描述：
操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点

    '''
    递归：
    1. 判断根节点是否存在
    2. 存在，对换左右节点
    3. 左，右子树递归交换左右子树
    '''
    def Mirror(self, root):
        if not root:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
        return root
    '''
    非递归：todo
    '''