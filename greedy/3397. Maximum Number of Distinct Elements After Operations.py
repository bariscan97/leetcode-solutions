class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = 0
        val = -k
        arr = [*nums]
        arr[0] += val
        res = 1
        
        for curr in range(1, len(nums)):
            if nums[prev] != nums[curr]:
                diff = arr[prev] - nums[curr]
                val = max(diff + 1, - k)
            else:
               val = min(val + 1, k)
            arr[curr] += val   
            if arr[prev] != arr[curr]:
                res += 1
            prev = curr
        
        return res