# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        res=[]
        a,b,size=0,k,len(arr)
        for i in range(len(arr)-k+1):
            if size-a<k:res+=arr[a:b]
            else:res+=arr[a:b][::-1]
            a+=k
            b+=k
        head_=ListNode(res[0])
        node=head_
        for i in res[1:]:
            node.next=ListNode(i)
            node=node.next
        return head_
            