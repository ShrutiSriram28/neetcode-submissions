"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloning = {}

        def dfs(node):
            if not node:
                return None

            if node in cloning:
                return cloning[node]

            newnode = Node(node.val)
            newnode.neighbors = []
            cloning[node] = newnode
            for neighbor in node.neighbors:
                newnode.neighbors.append(dfs(neighbor))
            return newnode
        
        return dfs(node)