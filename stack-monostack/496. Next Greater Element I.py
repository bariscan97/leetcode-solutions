class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1]*(len(nums1))
        hashMap = {c: i for i, c in enumerate(nums1)}
        for n in nums2:
            while stack and stack[-1] < n:
                val = stack.pop()
                res[hashMap[val]] = n
            if n in hashMap:
                stack.append(n)
        return res