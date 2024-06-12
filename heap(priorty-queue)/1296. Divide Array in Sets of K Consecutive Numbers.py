class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        _heap = [[i,j] for i, j in Counter(nums).items()]
        heapify(_heap)
        cnt = 0
        
        while len(_heap) >= k:
            arr = []
            last_val = None
            for i in range(k):
                val , cnt = heappop(_heap)
                if last_val != None and val != last_val + 1:
                    return False    
                last_val = val    
                if cnt > 1:
                    arr.append([val, cnt - 1])
            for i in arr:
                heappush(_heap,i)
        
        return not _heap