# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert(self, root: Optional[TreeNode]):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        else:
            self.invert(root.left)
            self.invert(root.right)
            root.left, root.right = root.right, root.left

    def dfs(self, root: Optional[TreeNode]):
        if root is None:
            return
        if root.left is not None:
            self.dfs(root.left)
        print(root.val)
        if root.right is not None:
            self.dfs(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # self.dfs(root)
        self.invert(root)
        # self.dfs(root)
        return root
