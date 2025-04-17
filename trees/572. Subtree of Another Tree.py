# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def Equal(node1, node2):
            if node1 is None or node2 is None:
                return node1 == node2
            left = Equal(node1.left, node2.left)
            right = Equal(node1.right, node2.right)
            if node1.val != node2.val:
                return False
            return left and right   
        
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.val == subRoot.val and Equal(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False