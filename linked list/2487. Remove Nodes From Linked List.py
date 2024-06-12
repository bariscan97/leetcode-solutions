# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        while head:
            if stack==[]:stack.append(head.val)
            else:
                while stack and head.val>stack[-1]:stack.pop()
                stack.append(head.val)
            head=head.next
        if stack==[]:return 
        head_=ListNode(stack[0])
        node=head_
        for i in stack[1:]:
            node.next=ListNode(i)
            node=node.next
        return head_