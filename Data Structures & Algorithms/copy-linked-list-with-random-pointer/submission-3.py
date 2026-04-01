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
        cur = head
        nodemap = {None: None}

        while cur:
            nodemap[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        newcur = nodemap[head]

        while cur:
            newcur.next = nodemap[cur.next] 
            newcur.random = nodemap[cur.random]
            cur = cur.next
            newcur = newcur.next

        return nodemap[head]