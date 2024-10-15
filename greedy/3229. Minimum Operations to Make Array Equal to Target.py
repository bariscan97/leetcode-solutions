class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        N = len(nums)
        arr = [target[i] - nums[i] for i in range(N)]
        res = 0
        prev = 0
        flag = True if arr[0] >= 0 else False
        
        for i in  arr :
            if i >= 0 :
                if not flag :
                    prev = 0
                    flag = not flag
            else:
                i = abs(i)
                if flag :
                    prev = 0
                    flag = not flag
            res += max(i - prev ,0)
            prev = i
        
        return res