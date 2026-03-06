class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        sl = SortedList()
        res = total = j = 0

        for i in range(N):
            sl.add(nums[i])
            total += nums[i]

            while (sl[-1] - sl[0]) * len(sl) > k:
                sl.discard(nums[j])
                total -= nums[j]
                j += 1
            
            res += len(sl)
        
        return res