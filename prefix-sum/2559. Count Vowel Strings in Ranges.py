class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(["a","e","u","i","o"])
        N = len(words)
        prefix = [0] * N
        val = 0
        res = []
        for i in range(N) :
            if words[i][0] in vowels and words[i][-1] in vowels:
                val += 1
            prefix[i] = val
        for i ,j in queries:
            res.append(prefix[j] - (prefix[i - 1]  if i else 0))
        return res