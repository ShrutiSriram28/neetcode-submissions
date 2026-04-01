class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2c = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        part = []

        def dfs(i, j):
            if i >= len(digits):
                if len(part.copy()) > 0:
                    res.append("".join(part.copy()))
                return
            for j in range(len(d2c[digits[i]])):
                part.append(d2c[digits[i]][j])
                dfs(i + 1, j)
                part.pop()
        
        dfs(0, 0)
        return res
        
