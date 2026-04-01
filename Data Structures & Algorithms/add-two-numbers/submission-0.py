# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(l1.val)
        print(l2.val)
        sumll = ListNode()
        curr = sumll
        carry = 0
        while l1 and l2:
            new_node = ListNode()
            new_node.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            curr.next = new_node
            curr = curr.next
        
        while l1:
            new_node = ListNode()
            new_node.val = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            l1 = l1.next
            curr.next = new_node
            curr = curr.next
        
        while l2:
            new_node = ListNode()
            new_node.val = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            l2 = l2.next
            curr.next = new_node
            curr = curr.next

        if carry > 0:
            carry_node = ListNode(carry)
            curr.next = carry_node

        sumll = sumll.next

        return sumll