class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)

        prefix = nums[:]
        suffix = nums[:]
        
        mini, maxi = inf, -inf

        for i in range(N):
            maxi = max(maxi, nums[i])
            mini = min(mini, nums[N - 1 - i])
            
            prefix[i] = maxi
            suffix[N - 1 - i] = mini
        
        left = right = None
        for i in range(N):
            if nums[i] > suffix[i]:
                left = i
                break

        for i in range(N - 1, -1, -1):
            if nums[i] < prefix[i]:
                right = i
                break
        
        if left == right ==  None:
            return 0
            
        return (right - left) + 1