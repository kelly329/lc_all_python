# -*- coding:utf-8 -*-
'''
leetcode20:括号匹配问题
存在多种括号：(),[],{}
'''
def isValid(s):
	"""
	:type s: str
	:rtype: bool
	"""
	# 如果stacks = []，s字符串为‘]’,则在第一次判断时就无元素出栈会发生错误
	# 在只出现一种括号的问题中，有另一种解决办法
	stacks = [None]
	dicts = {')' : '(', ']' : '[', '}':'{'}
	for ch in s:
		if ch in dicts:
			if dicts[ch] != stacks.pop():
				return False
		else:
			stacks.append(ch)
	# 可以简化 直接 return len(stacks) == 1
	if len(stacks) == 1:
		return True
	else:
		return False
print(isValid('()'))

'''
只存在一种括号：() 
时间复杂度为O(n), 空间复杂度为O(n)
'''
def isValid_1(s):
	"""
	:type s: str
	:rtype: bool
	"""
	# 如果stacks = []，s字符串为‘]’,则在第一次判断时就无元素出栈会发生错误
	stacks = []
	for ch in s:
		if ch == '(':
			stacks.append(ch)
		else:
			if len(stacks) == 0:
				return False
			else:
				stacks.pop()
	if len(stacks) == 0:
		return True
	else:
		return False
print(isValid_1('(())'))				
'''
因为只有一种括号，所以可以不用使用栈，使用计数器
时间复杂度为O(n), 空间复杂度为O(1)
'''
def isValid_2(s):
	"""
	:type s: str
	:rtype: bool
	"""
	count = 0
	for ch in s:
		if ch == '(':
			count += 1
		else:
			if count == 0:
				return False
			else:
				count -= 1
	if count== 0:
		return True
	else:
		return False
print(isValid_2('())'))	


				
			
		