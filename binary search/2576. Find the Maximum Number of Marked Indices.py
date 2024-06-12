class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        mid = int(size / 2)
        left = 0
        res = 0
        for i in range(mid,size):
            if nums[i] >= nums[left] * 2:
                res += 2
                left += 1
            if left == mid :
                break
        return res
       