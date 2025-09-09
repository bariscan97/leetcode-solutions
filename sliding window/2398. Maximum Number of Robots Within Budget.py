from sortedcontainers import SortedList
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
       
        running ,res , j = 0 ,0 ,0
       
        sl = SortedList()
        
        for i in range(len(chargeTimes)):
            
            sl.add(chargeTimes[i])
            running += runningCosts[i]
            
            while sl and  (sl[-1] + (((i - j) + 1) * (running))) > budget:
            
                sl.discard(chargeTimes[j])
                running -= runningCosts[j]
                j += 1
            
            res = max(res, (i - j) + 1)
       
        return res