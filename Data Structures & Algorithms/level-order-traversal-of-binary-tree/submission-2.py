# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        def dfs(root, level):
            nonlocal levels
            if not root:
                return 
            if level == len(levels):
                levels.append([])
            levels[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        return levels
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # def height(root):
        #     if not root:
        #         return 0
        #     return 1 + max(height(root.left), height(root.right))
        
        # root_height = height(root)

        # levels = {}

        # def dfs(root):
        #     if not root:
        #         return 
        #     else:
        #         if root_height - height(root) not in levels:
        #             levels[root_height - height(root)] = [root.val]
        #         else:
        #             levels[root_height - height(root)].append(root.val)
        #         dfs(root.left)
        #         dfs(root.right)

        # dfs(root)

        # levelorder = []
        # for val in levels.values():
        #     levelorder.append(val)

        # return levelorder
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # levels = []

        # def depth(root, level):
        #     if not root: 
        #         return 0
        #     if len(levels) == level:
        #         levels.append([])
            
        #     levels[level].append(root.val)
        #     depth(root.left, level + 1)
        #     depth(root.right, level + 1)
        
        # depth(root, 0)
        # return levels