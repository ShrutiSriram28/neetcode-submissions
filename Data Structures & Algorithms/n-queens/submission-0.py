class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posd = set()
        negd = set()

        board = [["." for i in range(n)] for i in range(n)]

        res = []

        def dfs(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                pos = r + c
                neg = r - c
                if c not in cols and pos not in posd and neg not in negd:
                    board[r][c] = "Q"
                    cols.add(c)
                    posd.add(pos)
                    negd.add(neg)
                    dfs(r + 1)
                    board[r][c] = "."
                    cols.remove(c)
                    posd.remove(pos)
                    negd.remove(neg)
        
        dfs(0)
        return res