class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        x, y = 0, len(nums) - 1
        sorted_nums = sorted(nums)
        while x < y:
            current_sum = sorted_nums[x] + sorted_nums[y]
            if current_sum < target:
                count += y - x
                x += 1
            else:
                y -= 1
        return count
                