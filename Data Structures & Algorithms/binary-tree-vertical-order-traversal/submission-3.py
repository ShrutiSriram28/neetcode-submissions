# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = collections.defaultdict(lambda: [])
        check = []

        def preorder(root, row, col):
            if not root:
                return
            nodes[col].append([row, root.val])
            preorder(root.left, row + 1, col - 1)
            preorder(root.right, row + 1, col + 1)
        
        preorder(root, 0, 0)

        vertical = []
        for node in sorted(nodes):
            node_vals = sorted(nodes[node], key=lambda x: x[0])
            vertical.append([val for _, val in node_vals])

        return vertical