class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or board[r][c] == "X":
                return
            visited.add((r, c))
            board[r][c] = "U"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    dfs(r, c)
                    
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == "O" and (r, c) not in visited:
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "U":
                    board[r][c] = "O"