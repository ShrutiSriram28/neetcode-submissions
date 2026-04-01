"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        cur = head
        nodemap = {}

        while cur:
            nodemap[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        newcur = nodemap[head]

        while cur:
            newcur.next = nodemap[cur.next] if cur.next else None
            newcur.random = nodemap[cur.random] if cur.random else None
            cur = cur.next
            newcur = newcur.next

        return nodemap[head]