class Solution:
    def clearStars(self, s: str) -> str:
        arr = list(s[:])
        _heap = []
        N = len(s)
        for i in range(N):
            if s[i] == "*":
                _, idx = heappop(_heap)
                idx = -(idx + 1)
                arr[idx] = "*"
            else:
                heappush(_heap,[s[i], -(i + 1)])    
        return "".join([i for i in arr if i != "*"])