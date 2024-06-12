class TrieNode:
    def __init__(self):
        self.children = dict()
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        curr = self.root
        for i in range(len(word)):
            if not word[i] in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
    def search(self,word):
        curr = self.root
        for i in range(len(word)):
            if not word[i] in curr.children:
                return i 
            curr = curr.children[word[i]]
        return len(word) 
                

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res = -1 
        trie = Trie()
        for i in arr1:
            trie.insert(str(i))
        for i in arr2:
            res = max(res , trie.search(str(i)))
        return res