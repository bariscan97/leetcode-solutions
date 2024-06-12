# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and  node.right:
                
                if node.left.val == node.val == node.right.val:
                    # print(node.val,"1123123",right,left)
                    res = max (res,left+right+2)
                    return 1 + max(left,right)
                if node.left.val == node.val:
                    res = max (res,left+1)
                    # print(node.val,"1123123",right,left)
                    return left+1
                if node.right.val == node.val:
                    # print(node.val,"1123123",right,left)
                    res = max (res,right+1)
                    return right+1
                return 0
            elif node.left:
                if node.left.val == node.val:
                    res = max (res,left+1)
                    return left+1
                return 0
            elif node.right:
                
                if node.right.val == node.val:
                    res = max (res,right+1)
                    return right+1
                return 0
            else:
                return 0
            
        dfs(root)
        
        return res