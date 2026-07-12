class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}

        def dfs(i, j, k):
            if (i, j) in cache:
                return cache[(i, j)]

            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))
            
            cache[(i, j)] = False
            if i < len(s1) and s3[k] == s1[i]:
                if dfs(i + 1, j, k + 1):
                    cache[(i, j)] = True
            
            if (j < len(s2) and s3[k] == s2[j]):
                if dfs(i, j + 1, k + 1):
                    cache[(i, j)] = True

            return cache[(i, j)]

        return dfs(0, 0, 0) 