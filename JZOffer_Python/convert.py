# -*- coding:utf-8 -*-
'''
题目描述：二叉搜索数与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

'''
解题思路：
https://blog.csdn.net/u010005281/article/details/79657259
1.核心算法依旧是中序遍历
2.不是从根节点开始，而是从中序遍历得到的第一个节点开始
3.定义两个辅助节点listHead(链表头节点)、listTail(链表尾节点)。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None
    def Convert(self,pRoot):
        if not pRoot:
            return None

        self.Convert(pRoot.left)
        if self.listHead == None:
            self.listHead = pRoot
            self.listTail = pRoot
        else:
            self.listTail.right = pRoot
            pRoot.left = self.listTail
            self.listTail = pRoot
        self.Convert(pRoot.right)
        return self.listHead
