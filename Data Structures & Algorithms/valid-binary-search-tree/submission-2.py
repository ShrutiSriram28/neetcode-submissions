# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        
        def validity(root, lb, ub):
            nonlocal valid
            if root is None:
                return valid
            elif lb < root.val < ub:
                validity(root.left, lb, root.val)
                validity(root.right, root.val, ub)
            else:
                valid = False
            
        validity(root, float("-inf"), float("inf"))
        return valid
        