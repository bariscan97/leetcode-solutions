# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res,node.val,node.val+left+right,node.val+right,node.val+left)
            val = max(left,right)
            if node.val + val>=0:
                return node.val + val
            return 0
        dfs(root)
        return res