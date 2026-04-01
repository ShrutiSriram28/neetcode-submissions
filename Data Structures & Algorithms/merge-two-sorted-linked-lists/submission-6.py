# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()

        cur1, cur2 = list1, list2
        cur = merged

        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next     
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        
        if cur1 != None:
            cur.next = cur1
        
        if cur2 != None:
            cur.next = cur2

        return merged.next
                

