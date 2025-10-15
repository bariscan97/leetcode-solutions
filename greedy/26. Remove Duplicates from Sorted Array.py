class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        N = len(nums)
        curr_idx = 1
        
        for i in range(1, N):
            if nums[i] != nums[prev]:
                nums[curr_idx] = nums[i]
                curr_idx += 1
                prev = i
        
        return curr_idx