# -*- coding:utf-8 -*-
'''
题目描述：
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

'''
解题思路：
https://www.jianshu.com/p/85eea9f1adf0
1.二叉树为空，返回空
2.此节点是否有右子树
  2.1 若有右子树，此节点的沿着右子树的找寻到的一个左叶子节点
  2.2 若没有右子树,此节点有父节点，如果没有跳转则跳转2.3
    2.2.1 此节点为父节点的左子树，则此节点的下一个节点即为父节点为新节点，跳转至2.2
    2.2.2 此节点为父节点的右子树，则需要输入
  2.3 若没有右子树，此节点无父节点，
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None

        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        # 没有右节点，但是有父节点
        else:
            while pNode.next:
                if pNode = pNode.next.left:
                    return pNode
                pNode = pNode.next

        # 没有右节点，也没有父节点
        return None
