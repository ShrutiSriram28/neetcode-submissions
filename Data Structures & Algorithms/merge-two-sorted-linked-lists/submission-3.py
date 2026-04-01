# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        curr = list3

        while list1 and list2:
            new_node = ListNode()
            if list1.val <= list2.val:
                new_node = ListNode(list1.val)
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                list2 = list2.next
            curr.next = new_node
            curr = curr.next

        while list1:
            new_node = ListNode(list1.val)
            curr.next = new_node
            curr = curr.next
            list1 = list1.next
        
        while list2:
            new_node = ListNode(list2.val)
            curr.next = new_node
            curr = curr.next
            list2 = list2.next
        
        list3 = list3.next

        return list3
