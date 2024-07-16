# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
       
        kids = set()
        dic = dict()
       
        for  i in descriptions:
            dic[i[0]] = [None, None]
            kids.add(i[1]) 
       
        for  parent ,children ,flag in descriptions:
            dic[parent][0 if flag else 1] = children
            if not parent in kids:
                root = parent

        def dfs(node):
            if node is None:
                return
            if not node in dic:
                return TreeNode(node)
            left = dfs(dic[node][0])
            right = dfs(dic[node][1])
            curr = TreeNode(node)
            curr.left = left
            curr.right = right
            return curr

        return dfs(root)