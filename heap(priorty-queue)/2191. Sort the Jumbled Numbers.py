class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        dic = {str(i) : str(mapping[i]) for i in range(len(mapping))}
        heap , res = [] , []
        heapify(heap)
        
        for i, num in enumerate(nums):
            str_num = list(str(num))
            for idx in range(len(str_num)):
                str_num[idx] = dic[str_num[idx]]
            heappush(heap ,[int("".join(str_num)),i])
        
        while heap:
            _, idx = heappop(heap)
            res.append(nums[idx])  

        return res