# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)
        
        
        
        
        
        
        
        
        
        
        
        
        
        # height = 0

        # def depth(root):
        #     nonlocal height

        #     if not root:
        #         return 0
        #     left = depth(root.left) + 1
        #     right = depth(root.right) + 1

        #     return max(left, right)
        
        # return depth(root)