# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        jump1, jump2 = head, head

        while jump1 and jump2 and jump2.next:
            jump1 = jump1.next
            jump2 = jump2.next.next
            if jump1 == jump2:
                return True

        return False