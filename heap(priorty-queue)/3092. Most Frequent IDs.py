from sortedcontainers import SortedList
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        sl = SortedList()
        dic = Counter()
        ans = []
        for i in  range(len(nums)):
            sl.discard(dic[nums[i]])
            dic[nums[i]] += freq[i]
            sl.add(dic[nums[i]])
            ans.append(sl[-1])
        return ans