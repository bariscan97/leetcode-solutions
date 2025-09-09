class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aioeu")
        dic = Counter()
        j = 0
        res = 0
        unvowels_cnt = 0
        
        v = 1
        for i in range(len(word)):
            
            dic[word[i]] += 1
            if not word[i] in vowels:
                unvowels_cnt += 1
            
            
            while unvowels_cnt > k:
                dic[word[j]] -= 1
                if not word[j] in vowels:
                    unvowels_cnt -= 1
               
                v = 1
                j += 1    
              
            while all(dic[c] > 0 for c in vowels) and unvowels_cnt == k:
                if not word[j] in vowels or dic[word[j]] == 1:
                    break
                dic[word[j]] -= 1
               
                v += 1
                j += 1
            if all(dic[c] > 0 for c in vowels) and unvowels_cnt == k:
                res += v  
            
        
        return res
            