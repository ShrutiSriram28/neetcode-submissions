# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        list3 = ListNode()
        curr3 = list3

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                new_node = ListNode(curr1.val)
                curr3.next = new_node
                curr3 = curr3.next
                curr1 = curr1.next
            else:
                new_node = ListNode(curr2.val)
                curr3.next = new_node
                curr3 = curr3.next
                curr2 = curr2.next

        while curr1:
            new_node = ListNode(curr1.val)
            curr3.next = new_node
            curr3 = curr3.next
            curr1 = curr1.next
        
        while curr2:
            new_node = ListNode(curr2.val)
            curr3.next = new_node
            curr3 = curr3.next
            curr2 = curr2.next
        
        list3 = list3.next

        return list3
