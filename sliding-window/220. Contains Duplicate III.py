from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff==0:
            dic=dict()
            for i in range(len(nums)):
                if nums[i] in dic and i-dic[nums[i]]<=indexDiff:
                    return True
                dic[nums[i]]=i
            return False
        
        sl=SortedList(nums[:indexDiff+1])
        left,right=0,indexDiff+1
        
        for i in range(len(nums)):
            
            left_diff=nums[i]-valueDiff 
            right_diff=nums[i]+valueDiff 
            ind=sl.bisect_right(left_diff)
            
            if ind<len(sl) and sl[ind]==left_diff:return True
            elif ind<len(sl)-1 and  sl[ind+1]<=right_diff:return True
            elif ind>0 and sl[ind-1]==left_diff:return True
            
            if i>=indexDiff:
                sl.discard(nums[left])
                left+=1
            if right<len(nums):
                sl.add(nums[right])
            right+=1
    
        return False