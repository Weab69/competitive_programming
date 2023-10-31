# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l=head
        r=self.getMid(head)
        tmp=r.next
        r.next=None
        r=tmp
        
        l=self.sortList(l)
        r=self.sortList(r)
        return self.merge(l,r)
    
    def getMid(self,head):
        s,f=head,head.next
        while f and f.next:
            s=s.next
            f=f.next.next
        return s
    def merge(self,l,r):
        tail=dummy=ListNode()
        while l and r:
            if l.val <r.val:
                tail.next=l
                l=l.next
            else:
                tail.next=r
                r=r.next
            tail=tail.next
        if l:
            tail.next=l
        if r:
            tail.next=r
        return dummy.next
          
         