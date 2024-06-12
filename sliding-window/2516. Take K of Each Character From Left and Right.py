class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        dic = Counter(s)
        left = 0
        res = float("inf")
        size = len(s)
        if dic["a"] < k or dic["b"] < k or dic["c"] < k:
            return -1
        for i in range(len(s)):
            dic[s[i]] -= 1
            
            while left < size  and (dic["a"] < k or dic["b"] < k or dic["c"] < k ):
                dic[s[left]] += 1
                left += 1  
            
            res = min(res ,size - ((i - left) + 1))
        
        return res