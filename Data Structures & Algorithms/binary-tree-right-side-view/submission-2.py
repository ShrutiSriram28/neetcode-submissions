# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        
        def depth(root, level):
            nonlocal levels
            if root is None:
                return
            if len(levels) == level:
                levels.append([])
            levels[level].append(root.val)
            depth(root.left, level + 1)
            depth(root.right, level + 1)
        
        depth(root, 0)
        
        right = []
        for level in levels:
            right.append(level[-1])

        return right
