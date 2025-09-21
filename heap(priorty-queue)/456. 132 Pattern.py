class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        sl1 = SortedList([nums[0]])
        sl2 = SortedList(nums[1:])
        
        for num in nums[1:-1]:
            sl2.discard(num)
            if num > sl1[0]:
                idx = sl2.bisect_left(sl1[0] + 1)
                if idx < len(sl2) and sl2[idx] > sl1[0] and num > sl2[idx]:
                    return True
            sl1.add(num)
        
        return False