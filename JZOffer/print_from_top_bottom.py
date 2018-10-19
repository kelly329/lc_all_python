# -*- coding:utf-8 -*-
'''
题目描述：
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []

        result = []
        temp = [root]

        while len(temp):
            cur = temp.pop(0)
            result.append(cur.val)

            if cur.left:
                temp.append(cur.left)

            if cur.right:
                temp.append(cur.right)
        return result
