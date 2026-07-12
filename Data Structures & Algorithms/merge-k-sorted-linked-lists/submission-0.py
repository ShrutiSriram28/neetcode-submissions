# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def merge(list1, list2):
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            
            res = head = ListNode()

            while list1 and list2:
                if list1.val <= list2.val:
                    res.next = list1
                    list1 = list1.next
                else:
                    res.next = list2
                    list2 = list2.next
                res = res.next
            
            res.next = list1 if list1 else list2

            return head.next

        while len(lists) > 1:
            mergelist = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                merged = merge(list1, list2)
                mergelist.append(merged)
            lists = mergelist
        
        return lists[0]

        