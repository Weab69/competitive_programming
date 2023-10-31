# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        p,c=head,head.next
        
        while c:
            if c.val >= p.val:
                p,c=c,c.next 
                continue 
            
            temp=dummy
            while c.val > temp.next.val:
                temp=temp.next
            p.next=c.next
            c.next=temp.next
            temp.next=c
            c=p.next
        return dummy.next
          
        
        