class Solution:
    def isPossible(self, target: List[int]) -> bool:
       
        total = sum(target)
        heap = []
        
        for i in target:
            heappush(heap, -i)
        
        while True:
           
            val = heappop(heap)
            if val == -1:
                return True
            
            others = total + val 

            if val + others > -1 or others == 0 :
                return False
            
            elem = ((val * (-1)) % others)
           
            if elem == 0:
               elem = others
           
            heappush(heap ,elem * (-1))
            
            total = others + elem

        
            