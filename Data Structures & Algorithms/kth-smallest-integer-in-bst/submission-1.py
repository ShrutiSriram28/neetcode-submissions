# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []

        def traverse(root):
            nonlocal inorder
            if not root:
                return
            else:
                traverse(root.left)
                inorder.append(root.val)
                traverse(root.right)

        traverse(root)
        return inorder[k - 1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # inorder = []
        # def inorderTraversal(root):
        #     nonlocal inorder
        #     if root is None:
        #         return
        #     inorderTraversal(root.left)
        #     inorder.append(root.val)
        #     inorderTraversal(root.right)
        
        # inorderTraversal(root)
        # return inorder[k - 1]