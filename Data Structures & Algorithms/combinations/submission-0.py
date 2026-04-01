class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subset = []
        superset = []

        def dfs(nc, kc):
            if kc == k:
                if subset not in superset:
                    superset.append(subset.copy())
                return
            if nc > n or kc > k:
                return
            
            subset.append(nc)
            dfs(nc + 1, kc + 1)
            subset.pop()
            dfs(nc + 1, kc)
        
        dfs(1, 0)
        return superset