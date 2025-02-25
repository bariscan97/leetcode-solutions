class Solution:
    def findOriginalArray(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        res = []
        if 0 in dic and dic[0] % 2:
            return []
        for i in sorted(dic.keys()):
            doubled = int(i * 2)
            if dic[i] > dic[doubled]:
                return []
            if dic[i] < dic[doubled]:
                dic[doubled] -= dic[i]
            elif dic[i] == dic[doubled]:
                if not i:
                    res.extend([i] * (dic[i] // 2))
                    continue
                dic[doubled] = 0
            res.extend([i] * dic[i])
            dic[i] = 0
        return res