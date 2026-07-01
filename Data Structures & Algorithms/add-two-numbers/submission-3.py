# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        tens = 0
        rescur = res = ListNode()

        while c1 or c2 or tens:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0

            val = v1 + v2 + tens
            ones = val % 10
            tens = val // 10
            rescur.next = ListNode(ones)

            rescur = rescur.next
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None

        return res.next

        
        # c1 = l1
        # c2 = l2
        # tens = 0
        # rescur = res = ListNode(0)
        
        # while c1 and c2:
        #     sum_val = c1.val + c2.val + tens
        #     tens = sum_val // 10
        #     ones = sum_val % 10
        #     res.next = ListNode(ones)
        #     res = res.next
        #     c1 = c1.next
        #     c2 = c2.next

        # while c1:
        #     sum_val = c1.val + tens
        #     tens = sum_val // 10
        #     ones = sum_val % 10
        #     res.next = ListNode(ones)
        #     res = res.next
        #     c1 = c1.next

        # while c2:
        #     sum_val = c2.val + tens
        #     tens = sum_val // 10
        #     ones = sum_val % 10
        #     res.next = ListNode(ones)
        #     res = res.next
        #     c2 = c2.next

        # while tens:
        #     res.next = ListNode(tens)
        #     tens = 0


        # return rescur.next