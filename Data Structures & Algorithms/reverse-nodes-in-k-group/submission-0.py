# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        groupprev = dummy

        def getkth(dummy, k):
            cur = dummy

            while cur and k:
                k -= 1
                cur = cur.next
            
            return cur

        while True:
            kth = getkth(groupprev, k)
            if not kth:
                break
            groupnext = kth.next

            prev, cur = kth.next, groupprev.next
            while cur != groupnext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            temp = groupprev.next
            groupprev.next = kth
            groupprev = temp
        
        return dummy.next