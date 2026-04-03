class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sub = []
        subset = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                if sub not in subset:
                    subset.append(sub.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            sub.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            sub.pop()
            while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return subset