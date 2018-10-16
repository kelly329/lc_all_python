# -*- coding:utf-8 -*-
'''
题目描述：
输入一个链表，输出该链表中倒数第k个结点。
'''

'''
解题思路：
https://blog.csdn.net/fuxuemingzhu/article/details/79515252
考虑程序的鲁棒性
1.链表头节点的不存在
2.k为0
3.链表长度小于k

使用两个指针，前一个指针比后一个多有k-1步，这样当前一个指针走到头时，后一个指针刚好走到倒数第k个位置
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or not k:
            return None
        left, right = head, head

        for i in range(k-1):
            # 当k大于链表的长度时返回为空，否则继续走
            if not right.next:
                return None
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        return left