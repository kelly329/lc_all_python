# -*- coding:utf-8 -*-
'''
题目描述：
输入一个链表，反转链表后，输出新链表的表头。
'''
class Solution:
    '''
    方法：使用三个指针
    tmp保存phead的下一个节点，newHead新的头节点，pHead.next指向newHead，再移动一下三个节点即可
    https://blog.csdn.net/fuxuemingzhu/article/details/79516154
    '''
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        newHead = None

        while pHead:
            tmp = pHead.next
            pHead.next = newHead
            newHead = pHead
            pHead = tmp
        return newHead
    '''
    TODO:递归不太懂现在
    '''
