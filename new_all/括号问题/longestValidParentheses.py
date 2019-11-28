# -*- coding:utf-8 -*-
'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
第一种方法：使用栈, 栈顶元素即为未匹配的开始起点；时间复杂度O(n), 空间复杂度O(n)
第二种方法：计数 时间复杂度O(n), 空间复杂度O(1) 从左向右一次，再从右向左一次
第三种方法：动态规划（待补充吧）
'''
def longestValidParentheses_1(s):
	maxLen = 0
	stacks = [-1]
	for i in range(len(s)):
		if s[i] == '(':
			stacks.append(i)
		else:
			stacks.pop()
			if len(stacks) == 0:
				stacks.append(i)
			else:
				maxLen = max(maxLen, i - stacks[-1])
			
	return  maxLen
'''
从从左到右遍历字符串的过程中，用 left 记录 '(' 的数量，用 right 记录 ')' 的数量。并且在遍历的过程中：

1、如果 left == right，显然这个时候 right 个 ')' 都将一定能够得到匹配。所以当前的有效括号长度为 2 * right。然后更新 max。

2、如果 left < right，显然这个时候部分 ')' 一定得不到匹配，此时我们把 left 和 right 都置为 0。
'''
def longestValidParentheses_2(s):
	maxlen = 0
	# 从左向右遍历
	left, right = 0, 0
	for i in range(len(s)):
		if s[i] == '(':
			left += 1
		else:
			right += 1
		if left == right:
			maxlen = max(maxlen, right * 2)
		elif right > left:
			left, right = 0, 0
	# 从右向左遍历
	left, right = 0, 0
	for i in range(len(s) - 1, -1, -1):
		if s[i] == '(':
			left += 1
		else:
			right += 1
		if left == right:
			maxlen = max(maxlen, 2 * right)
		elif left > right:
			left, right = 0, 0
	return maxlen
			

	
	