# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(root):
            nonlocal diameter
            if not root:
                return 0
            else:
                l = height(root.left)
                r = height(root.right)
                diameter = max(diameter, l + r)
                return 1 + max(l, r)
        
        height(root)
        return diameter
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # diameter = 0
        # depth = 0

        # def height(root):
        #     nonlocal depth
        #     if root is None:
        #         return 0
        #     else:
        #         depth = max(depth, height(root.left) + height(root.right))
        #         return 1 + max(height(root.left), height(root.right))
        
        # height(root)
        # return depth
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # diameter = 0

        # def height(curr):   
        #     nonlocal diameter
        #     if curr is None:
        #         return 0
        #     leftDepth = height(curr.left)
        #     rightDepth = height(curr.right)
        #     diameter = max(diameter, leftDepth + rightDepth)
        #     return 1 + max(leftDepth, rightDepth)
        
        # height(root)
        # return diameter