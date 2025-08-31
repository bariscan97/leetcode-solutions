class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        num = n
        res = None

        def f(val, arr, k):
            nonlocal res
            if not k and val == 1:
                if res is None or res[-1] - res[0] > arr[1] - arr[0]:
                    res = arr
                return
            
            for i in range(1, int(val) + 1):
                if not val % i and k and (not arr or i >= arr[-1]):
                    f(val / i, arr + [i], k - 1)
                    
        f(num, [], k)
        return res