class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        pos = [i for i in nums if i > -1]
        if len(pos) == 0:
            return nums
        d = k % len(pos)
        n = pos[d:] + pos[:d]
        idx = 0
        for i in range(len(nums)):
            if nums[i] > -1:
                nums[i] = n[idx]
                idx += 1
        return nums