# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0 
        def dfs(node):
            nonlocal res
            if node is None:
                return 
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left == node.right == None:
                return [node.val,node.val]
            if node.left and node.right:
                res = max(res, abs(node.val-left[0]),abs(node.val-left[1]),abs(node.val-right[0]),abs(node.val-right[1]))
                return [min(node.val,left[0],right[0]),max(node.val,left[1],right[1])]
            if node.left:
                res = max(res,abs(node.val-left[0]),abs(node.val-left[1]))
                return [min(node.val,left[0]),max(node.val,left[1])]
            if node.right:
                res = max(res,abs(node.val-right[0]),abs(node.val-right[1]))
                return [min(node.val,right[0]),max(node.val,right[1])]
        dfs(root)
        return res