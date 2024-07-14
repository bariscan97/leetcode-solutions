# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        val = None
        while q:
            node = q.popleft()
            if node :
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if val != None and val != node.val:
                    return False
                if val is None:
                    val = node.val
        return True