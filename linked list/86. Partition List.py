# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt,gt=[],[]
        while head:
            if head.val<x:lt.append(head.val)
            else:gt.append(head.val)
            head=head.next
        arr=lt+gt
        if arr==[]:return 
        head_=ListNode(arr[0])
        node=head_
        for i in arr[1:]:
            node.next=ListNode(i)
            node=node.next
        return head_