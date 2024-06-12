from sortedcontainers import SortedList
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        
        sl = SortedList(nums[1:dist+2])
        rang = len(nums)-(dist+1)
        tot = sum(sl[:k-1])
        l_ind = dist+1
        val = tot
        for i in range(dist+2,len(nums)):
            
            if k-1 == dist + 1:
                
                tot -= nums[i -l_ind]
                tot += nums[i]
                val = min(val,tot)
                continue
            
            idx = sl.bisect_left(nums[i - l_ind])
          
            sl.discard(nums[i - l_ind])
            
            if k-1 != dist+1  and idx <= k-2 :
                
                tot -= nums[i - l_ind]
                tot += sl[k-2]
           
            idx = sl.bisect_left(nums[i])
            
            if k-1 != dist+1   and idx <= k-2:
                
                tot -= sl[k-2]
                tot += nums[i]
            
            sl.add(nums[i])
            val = min(val,tot)
        return val+nums[0]