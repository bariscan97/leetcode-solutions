class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        
        def calc(arr, v, cnt):
            N = len(arr)
            for i in range(N - 1):
                if arr[i] == v:
                    arr[i] = -v
                    arr[i + 1] *= -1
                    cnt -= 1
                if not cnt:
                    break
            return sum(arr) == N * -v

        return calc(nums[:],1, k) or calc(nums[:],-1, k)