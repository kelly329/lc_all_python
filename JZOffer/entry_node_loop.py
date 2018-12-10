# -*- coding:utf-8 -*-
'''
题目描述：
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。


解题思路：
https://blog.csdn.net/qq_20141867/article/details/80931915
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        slow, fast = pHead, pHead
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast