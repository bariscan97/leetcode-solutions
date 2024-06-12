# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        dic=Counter()
        def dfs(node,dep):
            if node is None:return
            dic[dep]+=node.val
            dfs(node.left,dep+1)
            dfs(node.right,dep+1)
        dfs(root,1)
        heap=[-i for i in dic.values()]
        heapify(heap)
        if len(dic)<k:return -1
        for i in range(k):
            val=heappop(heap)
        return -val