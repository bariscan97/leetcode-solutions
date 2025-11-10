class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        N = len(s)
        res = [inf] * N
        for i in range(N):
            if s[i] == c:
                res[i] = 0
                left = max(0,i - 1)
                right = min(N - 1, i + 1)
                while right < N and s[right] != c:  
                    res[right] = min(res[right], right - i)
                    right += 1
                while left > -1 and s[left] != c:  
                    res[left] = min(res[left], i - left)
                    left -= 1
        return res