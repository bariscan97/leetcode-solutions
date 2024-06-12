class Solution:
    def checkPartitioning(self, s: str) -> bool:
        @cache
        def is_pali(start, end):
            pali = s[start:end+1]
            return pali == pali[::-1]

        L = len(s)
        start = s[0]
        end = s[-1]
        for i in range(L-2):
            if s[i] != start:
                continue
            for j in range(L-1, i+1, -1):
                if s[j] != end:
                    continue
                if s[i+1] != s[j-1]:
                    continue
                
                if is_pali(0, i) and is_pali(j, L) and is_pali(i+1, j-1):
                    return True
        
        return False