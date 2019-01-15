
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# 运行时间：31ms 占用内存：5732k
	# 返回从尾部到头部的列表值序列，例如[1,2,3]
	def printListFromTailToHeadI(self, listNode):
		# write code here
		list = []
		while listNode:
			# 使用列表的插入方法，每次从头不插入
			list.insert(0, listNode.val)
			listNode = listNode.next
		return list
	
	#运行时间：28ms 占用内存：5732k
	#使用堆的思想，先进后出
	def printListFromTailToHeadII(self, listNode):
		# write code here
		list = []
		while listNode:
			list.append(listNode.val)
			listNode = listNode.next
		return list[::-1]