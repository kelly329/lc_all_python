class TrieNode:
	def __init__(self):
		self.isEnd = False
		self.next = [None for i in range(26)]

class Trie:
	def __init__(self):
		self.root = TrieNode()
	
	def insert(self, word):
		node = self.root
		for i in range(len(word)):
			if node.next[ord(word[i]) - ord('a')] == None:
				node.next[ord(word[i]) - ord('a')] = TrieNode()
			node = node.next[ord(word[i]) - ord('a')]
		node.isEnd = True

class Solution(object):
	def findWords(self, board, words):
		"""
		:type board: List[List[str]]
		:type words: List[str]
		:rtype: List[str]
		"""
		res = []
		trie = Trie()
		node = trie.root
		for w in words:
			trie.insert(w)
		for i in range(len(board)):
			for j in range(len(board[0])):
				self.dfs(node, board, i, j, "", res)
		return res
	
	def dfs(self, node, board, i, j, path, res):
		if node.isEnd:
			res.append(path)
			node.isEnd = False
		if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '#':
			return 
		temp = board[i][j]
		node = node.next[ord(temp) - ord('a')]
		if node == None:
			return
		
		board[i][j] = '#'
		
		self.dfs(node, board, i, j + 1, path + temp, res)
		self.dfs(node, board, i, j - 1, path + temp, res)
		self.dfs(node, board, i + 1, j, path + temp, res)
		self.dfs(node, board, i - 1, j, path + temp, res)
		board[i][j] = temp
		
		