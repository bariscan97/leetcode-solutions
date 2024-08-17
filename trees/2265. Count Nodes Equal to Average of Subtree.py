# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def dfs(node):
            
            nonlocal res
            if node is None:
                return [0 ,0]
            left = dfs(node.left)
            right = dfs(node.right)
            if int((left[0] + right[0] + node.val) / (left[1] + right[1] + 1)) == node.val:
                res += 1
            return [left[0] + right[0] + node.val ,left[1] + right[1] + 1]
       
        res = 0
        dfs(root)
      
        return res        

            
                