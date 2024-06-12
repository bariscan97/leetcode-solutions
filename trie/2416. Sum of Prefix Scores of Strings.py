class TrieNode:
    def __init__(self):
        self.children = dict()
        self.count = 0

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        
        curr = self.root
        for i in word:
            if not i in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
            curr.count += 1        

    def prefixCount (self,word):
        
        curr = self.root
        res = 0
        for i in word:
            res += curr.children[i].count
            curr = curr.children[i]
        return res
    


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()
        for i in words :
            trie.insert(i)
        
        return [trie.prefixCount (i) for i in words]