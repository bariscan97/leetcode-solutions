def backtrack(num, total, idx):
    if idx == len(num):
        return int(num) ** 0.5 == total
    num_str = ""
    val = False
    for i in  range(idx, len(num)):
        num_str += num[i]
        val = val or backtrack(num, total + int(num_str), i + 1)
    return val

class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        for i in range(1,n + 1):
            num = int(i * i)
            if backtrack(str(num), 0, 0):
                res += num
        return res    
    