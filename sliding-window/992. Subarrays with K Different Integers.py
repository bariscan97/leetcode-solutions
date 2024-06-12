class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    
        cnt = 1
        val = None
        arr = []
        for i in range(len(nums)):
            if val is None:
                val = nums[i]
            elif val == nums[i]:
                cnt += 1
            else:
                arr.append([val,cnt])
                val = nums[i]
                cnt = 1
        arr.append([val,cnt])
        if k == 1:
            return sum(int((i[1] * (i[1] + 1)) / 2) for i in arr)
        res = 0
        total = 0
        dic = Counter()
        left = 0
       
        _set = set()
        for i in range(len(arr)):
            dic[arr[i][0]] += 1
            
            while len(dic) > k :
                dic[arr[left][0]] -= 1
                if dic[arr[left][0]] == 0:
                    dic.pop(arr[left][0])
                total = 0
                left += 1
                _set.clear()
            while len(dic) == k : 
                if not left in _set:
                    total += arr[left][1]
                _set.add(left)
                if dic[arr[left][0]] == 1:
                   
                    break
                dic[arr[left][0]] -= 1
                left += 1
            
            res += arr[i][1] * total
       
        return res
    