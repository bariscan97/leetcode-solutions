# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        m_set=set((x,y))
        res = False
        dep = None 
        def dfs(node,depth):
            nonlocal res,dep
            if node is None:return 
            if node.left and node.right:
                if node.left.val in m_set and node.right.val in m_set:
                    m_set.remove(node.left.val)
                    m_set.remove(node.right.val)
                    return
            if node.val in m_set:
                if dep is None:
                    dep=depth
                elif depth==dep:
                    res=True
                m_set.remove(node.val)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return res