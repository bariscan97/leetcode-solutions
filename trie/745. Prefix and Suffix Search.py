class WordFilter:

    def __init__(self, words: List[str]):
        self.pref = dict()
        self.suff = dict()
        self.idx = {words[i]:i for i in range(len(words))} 
        for i in range(len(words)):
            size = len(words[i]) - 1
            for j in range(len(words[i])):
                word1 = words[i][:j+1]
                word2 = words[i][j:]
                if word1 in self.pref:self.pref[word1].add(words[i])
                else:
                    self.pref[word1] = set({words[i]})
                if word2 in self.suff:self.suff[word2].add(words[i])
                else:
                    self.suff[word2] = set({words[i]})
                

    def f(self, pref: str, suff: str) -> int:
        if not pref in self.pref or not suff in self.suff:
            return -1
        arr = [self.idx[i] for i in self.pref[pref] & self.suff[suff]]
        res = -1
        for i in arr :
            res = max(res,i)
        return res


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)