class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        globs = Counter()
        res = []
        for word in words2:
            for i, j in Counter(word).items():
                globs[i] = max(globs[i], j)
        for word in words1:
            flag = True
            cnt = 0
            for i, j in Counter(word).items():
                if i in globs:
                    if j < globs[i]:
                        flag = False
                        break
                    else:
                        cnt += 1
            if flag and cnt == len(globs):
                res.append(word)
        return res