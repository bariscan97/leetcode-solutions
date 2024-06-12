# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def dfs(node,depth):
            if node is None:
                return inf
            left = dfs(node.left,depth + 1)
            right = dfs(node.right,depth + 1)
            if node.left == node.right == None:
                return depth
            return min(left,right)
        return dfs(root,1)