class Solution:
    def minOperations(self, s: str) -> int:
        N = len(s)
        sortedS = "".join(sorted(s))
        print(s, sortedS)
        if N == 2 and sortedS != s:
            return -1
        if sortedS == s:
            return 0
        mini = min(s)
        maxi = max(s)
        if s[0] == mini or s[-1] == maxi:
            return 1
        if (
            (s[-1] == mini and s[0] == maxi ) and 
            ("".join(sorted(s[1:])) != s[1:] and "".join(sorted(s[:-1])) != s[:-1]) and 
            s.count(mini) == 1 and 
            s.count(maxi) == 1
        ):
            return 3
        
        
        return 2