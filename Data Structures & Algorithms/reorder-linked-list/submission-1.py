# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        cur = head
        count = 0

        while cur:
            count += 1
            cur = cur.next

        half = 0
        
        prev = head
        while half < (count - 1)//2:
            prev = prev.next
            half += 1
        
        cur = prev.next
        prev.next = None
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        start = head
        end = prev

        while start and end:
            temp_start = start.next
            start.next = end
            start = temp_start

            temp_end = end.next
            end.next = start
            end = temp_end

        return 