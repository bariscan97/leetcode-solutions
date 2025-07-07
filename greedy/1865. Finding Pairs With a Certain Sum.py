class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.dic1 = Counter(nums1)
        self.dic2 = Counter(nums2)        

    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        self.dic2[prev] -= 1
        self.nums2[index] += val
        self.dic2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for i, j in self.dic1.items():
            diff = tot - i
            if diff in self.dic2:
                res += int(j * self.dic2[diff])
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)