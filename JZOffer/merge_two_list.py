# -*- coding:utf-8 -*-
'''
题目描述：
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    '''
    非递归：两个链表是有序的，所以合并后仍保持有序，使用双指针法。
    1.声明两个指针，分别指向两个链表的头部并声明一个新链表
    2.比较两个指针指向节点数值的大小，小的节点插入到新链表的后面，新链表的指针移动，原链表的指针也移动
    3.一直比较，直到到达其中一个链表的尾部，把另一个链表剩余的元素直接插入到新链表尾部即可。

    '''
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        p = pHead1
        q = pHead2

        h = newhead = ListNode(None)

        while p and q:
            if p.val <= q.val:
                h.next = p
                p = p.next
            else:
                h.next = q
                q = q.next
            h = h.next
        if p:
            h.next = p
        if q:
            h.next = q
        return newhead.next

    '''
    递归
    '''

    def MergeI(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        if pHead1.val < pHead2.val:
            res = pHead1
            res.next = self.MergeI(pHead1.next, pHead2)
        else:
            res = pHead2
            res.next = self.MergeI(pHead1, pHead2.next)
        return res

