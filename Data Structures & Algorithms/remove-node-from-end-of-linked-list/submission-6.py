# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cn = head
        c = dummy = ListNode()
        c.next = head
        
        count = 0

        while cn:
            if count == n:
                c = c.next
            else:
                count += 1
            cn = cn.next
            
        c.next = c.next.next

        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dummy = ListNode(0, head)
        # c1 = head
        # c2 = dummy

        # while n > 0:
        #     c1 = c1.next
        #     n -= 1

        # while c1:
        #     c1 = c1.next
        #     c2 = c2.next
        
        # c2.next = c2.next.next
        # return dummy.next