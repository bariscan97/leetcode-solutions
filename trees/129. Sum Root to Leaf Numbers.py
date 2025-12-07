# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, num):
            if node is None:
                return
            if node.left == node.right == None:
                nonlocal res
                res += num * 10 + node.val
            dfs(node.left, num * 10 + node.val)
            dfs(node.right, num * 10 + node.val)
        
        res = 0
        dfs(root, 0)

        return res
