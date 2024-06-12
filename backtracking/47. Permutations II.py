class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list()
        def perms(arr,sub):
            if len(arr) == 0:
                res.append(sub)
            check = []
            for i in range(len(arr)):
                if not arr[i] in check:
                    perms(arr[:i]+arr[i+1:],sub+[arr[i]])
                check.append(arr[i])
        perms(nums,[])
        return res