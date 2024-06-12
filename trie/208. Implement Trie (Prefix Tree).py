class TrieNode:
    
    def __init__(self):
        self.children = dict()
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if not i in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i] 
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(i,node):
            if   i == len(word) - 1 :
                if word[i] in node.children and node.children[word[i]].end_of_word:
                    return True
                return False
            res = False
            if word[i] in node.children:
                res = res or dfs(i+1,node.children[word[i]])
            return res
        return dfs(0,curr)
        # for i in word:
        #     if not i in curr.children:
        #         return False
        #     curr = curr.children[i]
        # return curr.end_of_word 


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if not i in curr.children:
                return False
            curr = curr.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)