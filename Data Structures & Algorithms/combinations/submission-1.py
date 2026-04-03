class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subset = []
        sub = []

        def dfs(i, j):
            if len(sub) == k and sub not in subset:
                subset.append(sub.copy())
                return
            if i > n or j > k:
                return
            
            sub.append(i)
            dfs(i + 1, j + 1)
            sub.pop()
            dfs(i + 1, j)

        dfs(1, 0)
        return subset