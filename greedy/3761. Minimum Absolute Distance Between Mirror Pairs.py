def f(num):
    return int(str(num)[::-1])

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        dic = {}
        res = inf
        
        for i in range(len(nums)):
            v = f(nums[i])
            if nums[i] in dic and i != dic[nums[i]]:
                res = min(res, i - dic[nums[i]])
            dic[v] = i
            
        return res if res < inf else -1