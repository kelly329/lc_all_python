# -*- coding:utf-8 -*-
'''
题目描述：
请实现两个函数，分别用来序列化和反序列化二叉树

解题思路：
序列化：
首先看二叉树的序列化，可以根据谦虚遍历的顺序序列化二叉树，因为前序遍历是从根节点开始的。
在遍历二叉树遇到左节点或者右节点为空时，可以把空的节点序列化为一个特殊的字符（如：'#'）。另外节点的数值之间要一个特殊的字符','隔开。
举例：（剑指offer中的图）
二叉树被序列化为字符串"1，2，4，#，#，#，3，5，#，#，6，#，#"

反序列化：
以字符串"1，2，4，#，#，#，3，5，#，#，6，#，#"为例。第一个读出的数字是1。由于前序遍历是从根节点开始，这就是根节点的值。
接下来读出2，根节点的左节点，同样4是值为2的节点的左节点，接下来两个'#'为值为4的左右节点，依次类推。

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    flag = -1

    def Serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)



    def Deserialize(self, s):
        # 每次加1，从0开始，不能超过字符串长度，否则返回None
        self.flag += 1
        l = s.split(',')

        if self.flag >= len(s):
            return None

        root = None
        # 新建一个树对象来反序列化字符串
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            #往树中存值，递归输入s没有问题，因为l[self.flag]是不断向后取值的
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

