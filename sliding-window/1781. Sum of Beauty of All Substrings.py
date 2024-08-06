from sortedcontainers import SortedList
class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            dic = dict()
            sl = SortedList()
            for j in range(i ,len(s)):
                if s[j] in dic:
                    sl.discard(dic[s[j]])
                    dic[s[j]] += 1
                else:
                    dic[s[j]] = 1
                sl.add(dic[s[j]])
                res += sl[-1] - sl[0]
           
        return res