# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validity(root, lb, ub):
            if not root:
                return True
            elif lb < root.val < ub:
                return validity(root.left, lb, root.val) and validity(root.right, root.val, ub)
            else:
                return False
        return validity(root, float("-inf"), float("inf"))































        # def validity(root, lb, ub):
        #     if root is None:
        #         return True
        #     elif lb < root.val < ub:
        #         return validity(root.left, lb, root.val) and validity(root.right, root.val, ub)
        #     else:
        #        return False
            
        # return validity(root, float("-inf"), float("inf"))
        