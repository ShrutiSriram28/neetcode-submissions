# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0

        def diameter(root):
            nonlocal dia

            if root is None:
                return 0
            
            left = diameter(root.left)
            right = diameter(root.right)

            dia = max(dia, left + right)
            return 1 + max(left, right)

        diameter(root)
        return dia
        
        
        
        
        
        
        
        
        
        
        
        
        
        # diameter = 0

        # def depth(root):
        #     nonlocal diameter

        #     if not root:
        #         return 0
        #     left = depth(root.left)
        #     right = depth(root.right)

        #     diameter = max(diameter, left + right)
        #     return 1 + max(left, right)
        
        # depth(root)
        # return diameter