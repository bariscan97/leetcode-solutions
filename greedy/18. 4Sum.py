class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        dic = defaultdict(set)
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                total = nums[i] + nums[j]
                dic[total].add((j,nums[i], nums[j]))
        res = set()
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                total = nums[i] + nums[j] 
                diff = target - total 
                for k in dic[diff]:
                    if k[0] < i:
                        res.add((nums[i], nums[j], k[1], k[2]))
        return [*res]