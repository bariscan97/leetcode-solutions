class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        prefix = chalk[:]

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        
        last_val = prefix[-1]

        k %= last_val

        return bisect_right(prefix ,k) 