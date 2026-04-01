class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = 0
        def dfs(r, c):
            nonlocal paths
            if r == m - 1 and c == n - 1:
                paths += 1
                return
            if r == m or c == n:
                return
            
            dfs(r + 1, c)
            dfs(r, c + 1)
        dfs(0, 0)
        return paths