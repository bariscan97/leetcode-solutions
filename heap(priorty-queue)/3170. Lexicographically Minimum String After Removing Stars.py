class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        _heap = []
        for i in range(len(s)):
            if s[i] != "*":
                heappush(_heap,[s[i] ,i * (-1)])
            else:
                val ,idx  = heappop(_heap)
                s[idx * (-1)] = "*"
        
        res = "".join([i for i in s if i != "*"])
        
        return res