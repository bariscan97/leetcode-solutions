class Solution:
    def minimumArea(self, nums: List[List[int]]) -> int:
        v = [inf, -inf]
        h = [inf, -inf] 
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] == 1:
                    v[0] = min(i, v[0])
                    v[1] = max(i, v[1])
                    h[0] = min(j, h[0])
                    h[1] = max(j, h[1])
        
        return (v[1] - v[0] + 1) * (h[1] - h[0] + 1)