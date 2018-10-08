# -*- coding:utf-8 -*-
'''
题目描述：
输入一个链表，从尾到头打印链表每个节点的值。
'''
class Solution:
    # 在尾部插入 30ms
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        list = []
        while listNode:
            list.append(listNode.val)
            listNode = listNode.next

        # list.reverse()
        # return list
        return list[::-1]
    # 使用栈的思想，先进后出  比第一种快一点 27ms
    def printListFromTailToHeadStack(self, listNode):
        if not listNode:
            return []
        p = listNode
        stack = []
        res = []
        while p:
            stack.append(p.val)
            p = p.next
        for i in range(len(stack)-1, -1, -1):
            res.append(stack[i])
        return res
    # 使用头部插入的方法 28ms
    def printListFromTailToHeadStack(self, listNode):
        if not listNode:
            return []
        p = listNode
        res = []
        while p:
            res.insert(0, p.val)
            p = p.next
        return res
    # 递归实现 30ms
    def printListFromTailToHeadF(self, listNode):
        if not listNode:
            return []
        return self.printListFromTailToHeadF(listNode.next) + [listNode.val]