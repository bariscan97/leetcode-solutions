class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root
        for i in word:
            if not i in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end_of_word = True

    def search(self,word):
        curr = self.root
        def dfs(i,node):
            if word[i] != "." and not word[i] in node.children:
                return False
            if i == len(word) - 1:
                if word[i] in node.children and node.children[word[i]].end_of_word:
                    return True
                if word[i] == "." :
                    for k in node.children.keys():
                        if node.children[k].end_of_word:
                            return True
                return False
            res = False
            
            if word[i] == ".":
                for key in node.children.keys():
                    res = res or dfs(i+1,node.children[key])
            else:
                res = res or dfs(i+1,node.children[word[i]])
            
            return res
        return dfs(0,curr)

class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        
    def addWord(self, word: str) -> None:
        self.trie.insert(word)
       
    def search(self, word: str) -> bool:
        
        return self.trie.search(word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)