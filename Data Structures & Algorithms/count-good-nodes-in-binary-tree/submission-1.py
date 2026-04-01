# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        gd = 0
        
        def dfs(root, maxval):
            nonlocal gd
            if not root:
                return
            if root.val >= maxval:
                gd += 1
                maxval = root.val
            dfs(root.left, maxval)
            dfs(root.right, maxval)
            
        dfs(root, -101)
        return gd
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # gn = 0
        # def good(root, maxval):
        #     nonlocal gn
        #     if not root:
        #         return 0
        #     elif root.val >= maxval:
        #         maxval = root.val
        #         gn += 1
        #     good(root.left, maxval)
        #     good(root.right, maxval)
        
        # good(root, root.val)
        # return gn
