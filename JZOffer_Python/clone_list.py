# -*- coding:utf-8 -*-
'''
题目描述：
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''

'''
解题思路：
https://blog.csdn.net/qq_33431368/article/details/79296360
1.复制每一个节点，并每一个复制的节点跟在原节点后 如: A A1 则 A.next = A1
2.遍历整个链表，判断是否存在随机指针，如果存在则复制随机指针：A1.random = A.random.next  
3.拆开为两个链表
'''
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None

        # 复制节点
        clone = pHead
        while clone:
            node = RandomListNode(clone.label)
            node.next = clone.next
            clone.next = node
            clone = node.next

        # 复制随机节点
        clone = pHead
        while clone:
            node = clone.next
            if clone.random:
                node.random = clone.random.next
            clone = node.next

        # 拆开链表
        clone = pHead
        pHead = pHead.next
        while clone.next:
            node = clone.next
            clone.next = node.next
            clone = node
        return pHead



