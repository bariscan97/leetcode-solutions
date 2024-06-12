class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False
        self.idx = None
class Trie:
    def __init__(self):
        self.prefix = TrieNode()
        self.suffix = TrieNode()
    def pre_insert(self,word,idx):
        curr = self.prefix
        if word == "":
            curr.children[""] = TrieNode()
            curr = curr.children[""]
        for i in word:
            if not i in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end_of_word = True
        curr.idx = idx
    def suff_insert(self,word,idx):
        curr = self.suffix
        if word == "":
            curr.children[""] = TrieNode()
            curr = curr.children[""]
            
            
        for i in word[::-1]:
            if not i in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end_of_word = True
        curr.idx = idx
    def pre_search(self,word,idx):
        arr = []
        curr = self.suffix
        for i in range(len(word)):
            if curr.end_of_word:
                
                if self.is_palindrome(i,len(word) - 1,word):
                    if curr.idx != idx:
                        arr.append([idx,curr.idx])
            if not word[i] in curr.children:
                break
            
            curr = curr.children[word[i]]
        # if curr.end_of_word:
        #     if curr.idx != idx:
        #         arr.append([curr.idx ,idx])
        return arr
    
    def suff_search(self,word,idx):
        arr = []
        curr = self.prefix
        if "" in curr.children and self.is_palindrome(0,len(word) - 1,word) and idx !=  curr.children[""].idx :
            arr.append([curr.children[""].idx ,idx])
            arr.append([idx , curr.children[""].idx])
        for i in range(len(word) -1 , -1, -1):
            
            if curr.end_of_word: 
              
                if self.is_palindrome(0,i ,word):
                    if curr.idx != idx:
                        arr.append([curr.idx , idx])
            if not word[i] in curr.children:
                break
            
            curr = curr.children[word[i]]
        return arr
    
    def is_palindrome(self,l, r ,s):
        
        while r >= l:
            if s[r] != s[l]:
                return False
            r -= 1
            l += 1
        return True
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic = dict()
        
        
        trie = Trie()
        res = []
        for i in range(len(words)):
            rev = words[i][::-1]
            if rev in dic:
                res.append([i , dic[rev]])
                res.append([dic[rev] ,i])
                dic.pop(rev)
            dic[words[i]] = i
        for i in range(len(words)):
            trie.pre_insert(words[i],i)
            trie.suff_insert(words[i],i)
        for i in range(len(words)):
            res.extend(trie.pre_search(words[i],i))
            res.extend(trie.suff_search(words[i],i))
        
        
        
        return res
    

        