class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        cnts = Counter(nums)

        for i, j in cnts.items():
            dic[j].append(i)
        
        for num in nums:
            if len(dic[cnts[num]]) == 1:
                return num
        
        return -1