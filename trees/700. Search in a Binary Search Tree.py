# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None :return []
        stack,node=[],root
        while stack or node :
            if node :
                stack.append(node)
                node=node.left
            else:
                node=stack.pop()
                if val==node.val:
                    return node
                node=node.right
       