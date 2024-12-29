class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dic = {}
        for word in words:
            for i in range(len(word)):
                if not i in dic:
                    dic[i] = Counter()
                dic[i][word[i]] += 1
        @cache
        def dp(i,size):
            if i == len(dic):
                if size == len(target):
                    return 1
                return 0
            if size == len(target):
                return 1
            val = 0
            if target[size] in dic[i]:
                val += (dp(i + 1, size + 1) * dic[i][target[size]])
            return val + dp(i + 1, size)
        
        return dp(0,0) % (10 ** 9 + 7)
            