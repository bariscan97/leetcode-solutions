class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        p = len(str(n+1))
        res = sum([9*perm(9,i-1) for i in range(1,p)])
        cur_set = set()
        for j, c in enumerate(str(n+1)):
            for i in range(j==0, int(c)):
                if i not in cur_set:
                    res += perm(9-len(cur_set),p-1-j)
            if int(c) in cur_set: break
            cur_set.add(int(c))
        return res