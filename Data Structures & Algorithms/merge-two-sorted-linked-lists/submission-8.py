# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        c1, c2, cres = list1, list2, res

        while c1 and c2:
            if c1.val <= c2.val:
                cres.next = c1
                c1 = c1.next
            elif c1.val > c2.val:
                cres.next = c2
                c2 = c2.next
            cres = cres.next
        cres.next = c1 or c2
        return res.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = ListNode()
        # c1, c2, cres = list1, list2, res

        # while c1 or c2:
        #     if c1 and c2:
        #         if c1.val <= c2.val:
        #             cres.next = c1
        #             c1 = c1.next
        #         elif c1.val > c2.val:
        #             cres.next = c2
        #             c2 = c2.next
        #         cres = cres.next
        #     elif c1:
        #         cres.next = c1
        #         break
        #     elif c2:
        #         cres.next = c2
        #         break
        # return res.next




















        
        # c1 = list1
        # c2 = list2
        # ret = None
        # if c1.val <= c2.val:
        #     ret = list1
        # else:
        #     ret = list2

        # while c1 and c2:
        #     if c2.val > c1.val:
        #         c1, c2 = c2, c1
        #     t = c1.next
        #     c1.next = c2
        #     c1 = t
        
        # return ret