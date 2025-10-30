class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def f(start, N, dic):
            res = 0
            curr = Counter()
            for i in range(start, N):
                if dic[s[i]] + curr[s[i]] < k:
                    res = max(res, f(start, i, Counter(curr)))
                    curr.clear()
                    start = i + 1
                    flag = False
                else:
                    if not s[i] in curr:
                        curr[s[i]] = 0
                    curr[s[i]] += 1
                    dic[s[i]] -= 1
            return max(res, N - start)

        return f(0, len(s), Counter(s))