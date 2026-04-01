# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr1 = curr2 = head
        count = 0
        if curr1.next == None:
            head = None
        else:
            while curr1.next != None:
                if count < n:
                    curr1 = curr1.next
                    count += 1
                else:
                    curr1 = curr1.next
                    curr2 = curr2.next
            if count < n:
                head = curr2.next
            else:
                curr2.next = curr2.next.next

        return head



#                         1 
#                 1   2   3   4   
# count = 0       c1
#                 c2
# count = 1           c1
#                 c2
# count = 2               c1
#                     c2
#                             c1
#                         c2

#                                     1 
#                 1   2   3   4   5   6   7   8   9 
# count = 0       c1
#                 c2
# count = 1           c1
#                 c2
# count = 2               c1
#                 c2
# count = 3                   c1
#                 c2
# count = 4                       c1
#                 c2
#                                     c1
#                     c2
#                                         c1
#                         c2
#                                             c1
#                             c2
#                                                 c1
#                                 c2
#                                                     c1
#                                     c2