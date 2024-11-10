class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1 and len(nums) > 1:
            return True
        cnt = 1
        prev = nums[0]
        flag = False
        for num in nums[1:]:
            if num > prev:
                cnt += 1
                if cnt == k and flag:
                    return True
                if cnt == int(k * 2):
                    return True
            else:
                if cnt >= k:
                    flag = True
                else:
                    flag = False
                cnt = 1
            prev = num
        
        return False