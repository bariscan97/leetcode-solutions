class TrieNodePrefix:
    def __init__(self):
        self.children = dict()
        self.own = None
        self.cnt = 0
class TrieNodesuffix:
    def __init__(self):
        self.children = dict()
        self.own = None
        self.cnt =  0

class Trie:
    def __init__(self):
        self.pref =  TrieNodePrefix()
        self.suff = TrieNodesuffix()
        self.dic = Counter()
    def insert(self,word):
        currPref = self.pref
        currSuff = self.suff
        x , y = set() , set()
        
        for i in range(len(word)):
            
            if not word[i] in currPref.children:
                currPref.children[word[i]] = TrieNodePrefix()
            currPref = currPref.children[word[i]]
            if not word[(len(word) - 1) - i] in currSuff.children:
                currSuff.children[word[(len(word) - 1) - i]] = TrieNodesuffix()
            currSuff = currSuff.children[word[(len(word) - 1) - i]]
            if currPref.own :
                x.add(currPref.own)
            if currSuff.own:
                y.add(currSuff.own)
        
        currPref.own = word
        currSuff.own = word
        currPref.cnt += 1
        currSuff.cnt += 1
        self.dic[word] += 1
        common = x & y
        res = 0
        for i in common:
            if i == word:
                res += (self.dic[i] - 1)
            else:
                res += self.dic[i]
        return res
   
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        res = 0
        for i in words: 
            res += trie.insert(i)
        return res