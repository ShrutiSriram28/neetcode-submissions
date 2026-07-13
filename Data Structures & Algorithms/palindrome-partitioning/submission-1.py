class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def isPalindrome(s1):
            l, r = 0, len(s1) - 1

            while l < r:
                if s1[l] != s1[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        def dfs(i, j):
            if i >= len(s):
                if i == j and part not in res:
                    res.append(part.copy())
                return

            if isPalindrome(s[j: i + 1]):
                part.append(s[j: i + 1])
                dfs(i + 1, i + 1)
                part.pop()
            
            dfs(i + 1, j)

        dfs(0, 0)
        return res