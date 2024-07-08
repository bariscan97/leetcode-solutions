class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False
        self.cost = inf

class Trie:
    def __init__(self,word):
        self.root = TrieNode()        
        self.word = word
    
    def insert(self, word: str, cost :int) -> None:
        curr = self.root
        for i in word:
            if not i in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i] 
        curr.end_of_word = True
        curr.cost = cost
    
    @cache
    def dfs(self,i):
        if i == len(self.word):
          return 0   
        
        val = inf
        curr = self.root
        
        for idx in range(i,len(self.word)):
            if not self.word[idx] in curr.children:
                break
            curr = curr.children[self.word[idx]]
            if curr.end_of_word:
                if val < curr.cost:
                    continue
                val = min(val, curr.cost + self.dfs(idx + 1))
                
        return val
    
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        dic = {i: inf for i in words}
        
        for i in range(len(words)):
            dic[words[i]] = min(costs[i] , dic[words[i]])
        
        v , c = [] ,[]
        
        for i ,j in dic.items():
            v.append(i)
            c.append(j)
        
        trie = Trie(target)
        
        for i, j in zip(v,c):
            trie.insert(i, j)
        
        res = trie.dfs(0)
        
        return res if res < inf else -1