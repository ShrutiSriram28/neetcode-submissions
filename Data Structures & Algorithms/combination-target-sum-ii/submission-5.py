class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        superset = set()
        subset = []

        def dfs(s, i):
            if s == target:
                superset.add(tuple(subset.copy()))
                return
            if s > target or i >= len(candidates):
                return

            subset.append(candidates[i])
            dfs(s + candidates[i], i + 1)
            subset.pop()

            while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(s, i + 1)

        dfs(0, 0)
        superset = [list(i) for i in superset]
        return superset