class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        N = len(s)
        prefix = [0] * N
        curr = Counter()
        chars = {}
        maxDiffs = {i:0 for i in ascii_lowercase}
    
        for i in range(N):
            curr[s[i]] += 1
            prefix[i] = curr.copy()
            if not s[i] in chars:
                chars[s[i]] = prefix[i]
            else:
                maxDiffs[s[i]] = max(maxDiffs[s[i]], len(prefix[i - 1] - chars[s[i]]))
        
        return sum(maxDiffs.values())