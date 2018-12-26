# -*- coding:utf-8 -*-
'''
题目描述：
输入两个链表，找出它们的第一个公共结点。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
解题思路： 参考剑指offer书
这道题有三种解题思路
1.蛮力的方法
2.使用栈的方法，但是时间复杂度和空间复杂度均为O(M+N)
3.使用现在这种先遍历两个链表的长度仔一次遍历公共节点

总结：
链表没有办法通过头节点使用len()函数求长度
还有剑指offer的分析，其实两个都是单链表，第一个公共的节点也是唯一的公共相交点，Y字形不是X
'''
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        length1 = self.getLength(pHead1)
        length2 = self.getLength(pHead2)
        headLong = ListNode(None)
        headShort = ListNode(None)

        if length1 > length2:
            headLong = pHead1
            headShort = pHead2
            difLen = length1 - length2
        else:
            headLong = pHead2
            headShort = pHead1
            difLen = length2 - length1

        for i in range(difLen):
            headLong = headLong.next

        while headLong and headShort and headLong != headShort:
            headLong = headLong.next
            headShort = headShort.next

        return headLong


    def getLength(self,pHead):
        length = 0
        while pHead:
            length = length + 1
            pHead = pHead.next
        return length




