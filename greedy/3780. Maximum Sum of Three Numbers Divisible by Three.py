class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {0: SortedList(), 1: SortedList(), 2: SortedList()}
        res = 0
        
        for num in nums:
            dic[num % 3].add(num)

        if len(dic[0]) > 2:
            res = max(res, sum(dic[0][-3:]))
        
        if len(dic[1]) > 2:
            res = max(res, sum(dic[1][-3:]))
        
        if len(dic[2]) > 2:
            res = max(res, sum(dic[2][-3:]))

        if dic[2] and dic[1] and dic[0]:
            res = max(res, dic[2][-1] + dic[1][-1] + dic[0][-1])

        return res
        