class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        max_val = min_val = nums[0]
        prev = bin(nums[0]).count("1")
        prev_interval = []
        for i in nums[1:]:
            bit_cnt = bin(i).count("1")
            if bit_cnt == prev:
                max_val = max(max_val, i)
                min_val = min(min_val, i)
            else:
                prev_interval = [min_val, max_val]
                max_val = min_val = i 
            if prev_interval and prev_interval[-1] >= min_val:
                return False 
            prev = bit_cnt 
        return True