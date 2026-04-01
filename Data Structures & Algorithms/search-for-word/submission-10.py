class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        def dfs(i, r, c):
            if i == len(word):
                return True

            if (r < 0) or (c < 0) or (r >= len(board)) or (c >= len(board[0])) or (visited[r][c]) or (board[r][c] != word[i]):
                return False

            visited[r][c] = True
            res = (dfs(i + 1, r - 1, c)) or (dfs(i + 1, r + 1, c)) or (dfs(i + 1, r, c - 1)) or (dfs(i + 1, r, c + 1))
            visited[r][c] = False
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(0, r, c):
                    return True
        return False