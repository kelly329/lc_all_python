# -*- coding:utf-8 -*-
'''
题目描述：
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

题目思路：
这道题和之字打印二叉树类似,两个栈，一个存储当前层遍历树的值，另一个是存储下一层需要遍历的节点。
完成两个栈的存储后，把当前栈存储的节点值存储到结果中，之后遍历nextStack中的节点。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        result = []
        nodes = [pRoot]

        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node)
                if node.right:
                    nextStack.append(node)
            result.append(curStack)
            nodes = nextStack
        return result