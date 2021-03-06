# -*- coding:utf-8 -*-
'''
题目描述：
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''

'''
解题思路：
我们可以设计两个栈：Stack和StackMin，一个就是普通的栈，另外一个存储push进来的最小值。
首先是push操作：
每次压入的数据newNum都push进Stack中，然后判断StackMin是否为空，如果为空那也把newNum同步压入StackMin里；
如果不为空，就先比较newNum和StackMin中栈顶元素的大小，如果newNum较大，那就不压入StackMin里，只压入一个最小值
否则就同步压入StackMin里。弹出时，同步弹出，这是一个栈结构。
'''
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def pop(self):
        if self.stack == [] or self.minstack == []:
            return None
        self.stack.pop()
        self.minstack.pop()
    def push(self,node):
        self.stack.append(node)
        if self.minstack == [] and node < self.minstack[-1]:
            self.minstack.append(node)
        else:
            self.minstack.append(self.min())
    def top(self):
        return self.stack[-1]
    def min(self):
        return self.minstack[-1]
