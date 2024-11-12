class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prefix = [items[0][1]]
        max_val = items[0][1]
        res = []
        for _, beauty  in items[1:]:
            max_val = max(max_val, beauty)
            prefix.append(max_val)
        for query in queries:
            idx = bisect_right(items,[query,inf])
            if idx == len(items):
                res.append(prefix[-1])
                continue
            if items[idx][0] != query:
                if idx == 0:
                    res.append(0)
                else:
                    res.append(prefix[idx - 1])
        return res