# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(root):
            if not root: return 0
            l, r = dfs(root.left), dfs(root.right)
            if l == r >= 0:
                res.append(l + 1)
                return l + 1
            return -1
        dfs(root)
        return (1 << sorted(res)[-k]) - 1 if k <= len(res) else -1