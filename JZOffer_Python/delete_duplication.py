# -*- coding:utf-8 -*-
'''
题目描述：
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or pHead == None:
            return None

        preHead = None
        pNode = pHead
        while pNode != None:
            pNext = pNode.next
            needDelete = False
            if pNext != None and pNext.val == pNode.val:
                needDelete = True

            if needDelete == False:
                preHead = pNode
                pNode = pNode.next
            else:
                nodeVal = pNode.val
                pDelete = pNode
                while pDelete != None and pDelete.val == nodeVal:
                    pDelete = pDelete.next
                if preHead == None:
                    pHead = pDelete
                    preHead = pDelete
                    continue
                else:
                    preHead.next = pDelete
                pNode = preHead
                # pNode = pDelete 都可以通过
            return pHead
