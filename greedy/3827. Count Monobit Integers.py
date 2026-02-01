class Solution:
    def countMonobit(self, n: int) -> int:
        res = 0
        
        for i in range(n + 1):
            if 1 == len(set(bin(i)[2:])):
                res += 1
        
        return res