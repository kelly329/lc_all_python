# -*- coding:utf-8 -*-
'''
题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

'''
解题思路：
使用stack1临时存放push元素，当弹出元素时，如果stack2不为空，则直接弹出元素；
若是stack2为空，则把stack1的元素全部入栈stack2（刚开始时stack2为空）
'''
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self,node):
        self.stack1.append(node)
    def pop(self):
        if self.stack2:
            self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

