"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        visited = []

        def postorder(root):
            if not root:
                return
            
            if len(root.children):
                for child in root.children:
                    postorder(child)
            visited.append(root.val)

        postorder(root)
        return visited