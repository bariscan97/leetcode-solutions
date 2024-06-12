# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def dfs(node):
            nonlocal res
            if node is None:
                return
            left = dfs(node.left)
            right = dfs(node.right)
            
           
            if node.left == node.right == None:
                res = max(res,node.val)
                return [node.val,node.val,True,node.val]
            
            if node.left and node.right:
                
                if left[2] is None or right[2] is None or node.val>=right[0] or node.val<=left[1]:
                    res = max(res,max(left[3],right[3]))
                    return [0,0,None,max(left[3],right[3])]
                res = max(res,left[3]+node.val+right[3])
                return [min(node.val,left[0],right[0]),max(node.val,left[1],right[1]),True,left[3]+right[3]+node.val]
            if node.left:
                
                if left[2] is None or node.val<=left[1]:
                    res = max(res,left[3])
                    return [0,0,None,left[3]]
                res = max(res,left[3]+node.val)
                return [min(node.val,left[0]),max(node.val,left[1]),True,left[3]+node.val]
            if node.right:
               
                if right[2] is None or node.val>=right[0] :
                    res = max(res,right[3])
                    return [0,0,None,right[3]]

                res = max(res,right[3]+node.val)
                return [min(node.val,right[0]),max(node.val,right[1]),True,right[3]+node.val]
        dfs(root)
        return res