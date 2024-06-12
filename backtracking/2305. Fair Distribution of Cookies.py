class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        def f(arr,subs):
            nonlocal res
            if len(arr)==0:
                res = min(res,max(subs))
            for i in range(len(arr)):
                f(arr[:i]+arr[i+1:],sorted([subs[0] + arr[i]]+subs[1:]))
        res = inf
        f(cookies,[0 for i in range(k)])
        return res 
        