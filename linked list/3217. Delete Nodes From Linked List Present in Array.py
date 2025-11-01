# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        res = ListNode(val = -1)
        prev = None
        
        while head:
            if not head.val in nums:
                if prev is None:
                    prev = res
                    prev.val = head.val
                else:
                    prev.next = ListNode(val = head.val)
                    prev = prev.next
            head = head.next
        
        return res
            
                 