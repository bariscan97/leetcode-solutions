# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            nonlocal res
            if node is None:
                return 
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left == node.right == None:
                return [node.val,node.val]
            
            if node.left and node.right:
                print(node.val,"123123")
                
                if node.val>=right[0]:
                    res = False
                if node.val<=left[1]:
                    res = False
                
                return [min(node.val,left[0],right[0]) , max(node.val,left[1],right[1])]
            if node.left:
                
                if node.val<=left[1]:
                    # print(node.val,left,"asd")
                    res = False 
                return [min(node.val,left[0]) , node.val]
            if node.right:
                if node.val>=right[0]:
                        res  = False
                return  [right[0],max(right[1],node.val)]


        dfs(root)

       
        return res