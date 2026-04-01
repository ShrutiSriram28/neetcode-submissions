# class Solution:
#     def climbStairs(self, n: int) -> int:
#         res = []
#         sets = []

#         def dfs(total):
#             if  total == n:
#                 res.append(sets.copy())
#                 return
#             if total > n:
#                 return
            
#             for i in range(1, 3):
#                 sets.append(i)
#                 dfs(total + i)
#                 sets.pop()
        
#         dfs(0)
#         print(res)
#         return len(res)



class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
            
        return dfs(0)