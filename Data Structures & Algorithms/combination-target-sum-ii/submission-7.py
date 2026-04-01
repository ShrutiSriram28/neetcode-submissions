class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        superset = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                if subset not in superset:
                    superset.append(subset.copy())
                return
            if i == len(candidates) or total > target:
                return
            
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            subset.pop()

            while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
                i += 1

            dfs(i + 1, total)
        
        dfs(0, 0)
        return superset