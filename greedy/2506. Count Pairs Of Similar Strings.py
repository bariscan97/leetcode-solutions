class Solution:
    def similarPairs(self, words: List[str]) -> int:
        dic = defaultdict(int)
        res = 0
        for word in words:
            key = frozenset(word)
            dic[key] += 1
            res += dic[key] - 1
        return res
