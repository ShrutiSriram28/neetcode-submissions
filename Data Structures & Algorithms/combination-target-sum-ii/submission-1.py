class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        sets = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.add(tuple(sets.copy()))
                return
            if i >= len(candidates) or total > target:
                return
            
            sets.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            sets.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        res = [list(i) for i in res]
        return res