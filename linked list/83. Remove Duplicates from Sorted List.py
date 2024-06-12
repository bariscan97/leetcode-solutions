# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:return 
        arr=[]
        while head:
            if arr==[]:arr.append(head.val)
            elif arr and arr[-1]!=head.val:arr.append(head.val)
            head=head.next
        head_=ListNode(arr[0])
        node=head_
        for i in arr[1:]:
            node.next=ListNode(i)
            node=node.next
        return  head_