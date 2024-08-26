# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if node is None:
                return 
            left = dfs(node.left)
            right = dfs(node.right)
            if not left and node.left and node.left.val == target:
                node.left = None
            if not right and node.right and node.right.val == target:
                node.right = None
            if not left and not right and target == node.val:
                return False
            return True
       
        dfs(root)
        
        return None if root and root.left == root.right == None and root.val == target else root
        