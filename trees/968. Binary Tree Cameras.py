# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        if root.left == root.right == None:
            return 1
        res = 0
        
        def dfs(node,dep):
            
            nonlocal res
            
            if node is None:
                return 0    
            
            dfs(node.left,dep+1)
            dfs(node.right,dep+1)
            
            if node.left == node.right == None:
                
                node.val == 0
            
            elif node.left and node.right:
                
                if node.left.val == node.right.val == 0:
                    node.val = 2
                    res+=1
                elif node.left.val == node.right.val == 1 and dep==0:
                    node.val = 2
                    res+=1
                elif node.left.val == 0 or node.right.val ==0:
                    node.val = 2
                    res+=1
                elif node.left.val == 2 or node.right.val == 2:
                    node.val = 1
            elif node.left:
                
                if node.left.val == 0 :
                    node.val=2
                    res+=1
                elif node.left.val == 1 and dep == 0:
                    node.val = 2
                    res+=1
               
                elif node.left.val == 2:
                    node.val = 1
               
            elif node.right:
                
                if node.right.val == 0:
                    node.val=2
                    res+=1
                elif node.right.val == 1 and dep == 0:
                    node.val = 2
                    res+=1
                elif node.right.val == 2:
                    node.val = 1
                
        dfs(root,0)
        
        return res