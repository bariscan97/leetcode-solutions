class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        A = sorted(
            [[i, j] for i, j in Counter(arr).items()],
            key = lambda x:x[1] 
        )
        size = len(A)
        cnt = 0
        for _, i in A:
            if k >= i:
                k -= i
            else:
                break
            cnt += 1
            
        return size - cnt 