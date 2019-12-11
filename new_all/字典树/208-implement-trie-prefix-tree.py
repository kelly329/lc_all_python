class TrieNode(object):
	def __init__(self):
		self.isEnd = False
		self.next = [None for i in range(26)]
class Trie(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode()

	def insert(self, word):
		"""
		Inserts a word into the trie.
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
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		node = self.root
		for i in range(len(word)):
			if node.next[ord(word[i]) - ord('a')] == None:
				return False
			node = node.next[ord(word[i]) - ord('a')] 
		return node.isEnd
	
		

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		node = self.root
		for i in range(len(prefix)):
			if node.next[ord(prefix[i]) - ord('a')] == None:
				return False
			node = node.next[ord(prefix[i]) - ord('a')] 
		return True
		


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)