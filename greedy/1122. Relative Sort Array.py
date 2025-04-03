class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = Counter(arr1) 
        res = []
        for i in arr2:
            res.extend([i] * dic[i])
            del dic[i]
        for i in sorted(dic.keys()):
            res.extend([i] * dic[i])
        return res