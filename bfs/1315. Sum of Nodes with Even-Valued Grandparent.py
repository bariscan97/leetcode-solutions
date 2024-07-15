# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = deque()
        q.append([[], root])
        res = 0
        while q:
            arr ,node = q.popleft()
            if node is None:
                continue
            if len(arr) == 2:
                val = arr[0]
                if val % 2 == 0:
                    res += node.val
            if node.left:
                q.append([arr[1 if len(arr) == 2 else 0:] + [node.val], node.left])
            if node.right:
                q.append([arr[1 if len(arr) == 2 else 0:] + [node.val], node.right])
        return res