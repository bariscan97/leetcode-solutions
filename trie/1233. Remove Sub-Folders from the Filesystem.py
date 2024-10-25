class TrieNode:
    
    def __init__(self):
        self.children = dict()
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()  
        self.res = []      

    def insert(self, word: str, splited: List[str]) -> None:
        curr = self.root
        for i in range(len(splited)):
            if not splited[i] in curr.children:
                curr.children[splited[i]] = TrieNode()
            curr = curr.children[splited[i]]
            if curr.end_of_word:
                return
        self.res.append(word) 
        curr.end_of_word = True
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = Trie()
        for i in folder:
            trie.insert(i, i.split("/"))
        return trie.res