class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        dic = Counter(word2)
        match = len(dic)
        j = res = 0
        for i in range(len(word1)):
            dic[word1[i]] -= 1
            match -= dic[word1[i]] == 0
            while not match:
                match += dic[word1[j]] == 0
                dic[word1[j]] += 1
                j += 1
            res += j
        return res  
        