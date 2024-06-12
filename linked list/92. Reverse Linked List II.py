# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr=arr[:left-1]+arr[left-1:right][::-1]+arr[right:]
        if arr==[]:return 
        head_=ListNode(arr[0])
        node=head_
        for i in arr[1:]:
            node.next=ListNode(i)
            node=node.next
        return head_