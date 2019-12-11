class TrieNode:
	def __init__(self):
		self.isEnd = False
		self.next = [None for i in range(26)]
		
class WordDictionary(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode()
		

	def addWord(self, word):
		"""
		Adds a word into the data structure.
		:type word: str
		:rtype: None
		"""
		node = self.root
		for i in range(len(word)):
			if node.next[ord(word[i]) - ord('a')] == None:
				node.next[ord(word[i]) - ord('a')] = TrieNode()
			node = node.next[ord(word[i]) - ord('a')]
		node.isEnd = True
		

	def search(self, word):
		"""
		Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
		:type word: str
		:rtype: bool
		"""
		
		return self.dfs(self.root, word, 0)
	
	def dfs(self, node, word, start):
		if start == len(word):
			return node.isEnd
		
		if word[start] != '.':
			if node.next[ord(word[start]) - ord('a')] == None:
				return False
			return self.dfs(node.next[ord(word[start]) - ord('a')], word, start + 1)
		else:
			# 当字符为‘.’时，需要遍历所有分支，当存在一个分支存在返回true，当所有分支走完不存在返回false
			for i in range(26):
				if node.next[i] and self.dfs(node.next[i], word, start + 1):
					return True
			return False
		
		


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)