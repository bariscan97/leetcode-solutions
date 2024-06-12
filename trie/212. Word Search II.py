class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for i in word:
            if not i in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        
        curr.word = word



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        def dfs(i,j,trie_node):
            nonlocal m,n 
            if i == -1 or j == -1 or i == m or  j == n or (i,j) in seens  or not board[i][j] in trie_node.children:
                return 
            
            trie_node = trie_node.children[board[i][j]]
            
            if trie_node.word != None:
                res.add(trie_node.word)
            
            seens.add((i,j))
           
            dfs(i + 1 , j,trie_node)
            dfs(i - 1 , j,trie_node)
            dfs(i , j +1,trie_node)
            dfs(i , j - 1,trie_node)
           
            seens.remove((i,j))
        
        res , seens = set() , set()
        m ,n = len(board) , len(board[0])
        trie = Trie()
        for i in words:
            trie.insert(i)

        for i in range(m):
            for j in range(n):
                dfs(i,j,trie.root)
        
        return res
