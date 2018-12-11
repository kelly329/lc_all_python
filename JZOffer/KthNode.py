# -*- coding:utf-8 -*-
'''
题目描述：
二叉搜索树的第k个结点。给定一棵二叉搜索树，请找出其中的第k小的结点。
例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。

题目思路：
中序遍历即可找到第k个结点
思路一：
1. 递归左子树，并判断有无返回节点。如果有，停止递归，返回所要返回的节点。
2. 当左子树没有返回节点时，判断当前的根节点是不是第k个遍历到的值（即第k大）。如果是，则返回该节点，停止递归。
3. 当左子树和根节点都没有返回节点时，递归右子树，并判断有无返回节点。如果有，停止递归，返回所要返回的节点。

思路二：
中序遍历二叉树，之后存储到数组中
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    count = 0

    def KthNode(self, pRoot, k):
        if not pRoot or k <= 0:
            return None
        return self.KthNodeCore(pRoot,k)
    def KthNodeCore(self,pRoot,k):
        target = None

        if pRoot.left != None:
            target = self.KthNodeCore(pRoot.left,k)

        if target == None:
            self.count += 1
            if self.count == k:
                return pRoot

        if target == None and pRoot.right != None:
            target = self.KthNodeCore(pRoot.right,k)

        return target


    '''
    思路二
    '''

    def KthNodes(self, pRoot, k):
        global result
        result = []
        target = self.KthNodeCores(pRoot)
        if k <= 0 or len(target) < k:
            return None
        else:
            return target[k-1]


    def KthNodeCores(self, pRoot):
        if not pRoot:
            return []
        self.KthNodeCores(pRoot.left)
        result.append(pRoot)
        self.KthNodeCores(pRoot.right)
        return result
        
