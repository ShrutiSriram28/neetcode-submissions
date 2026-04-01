class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        for word in words:
            if self.exists(board, word):
                res.append(word)
        return res

    def exists(self, board, word):
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(i, r, c):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r == rows or c == cols or visited[r][c] or board[r][c] != word[i]:
                return False
            
            visited[r][c] = True
            res = dfs(i + 1, r - 1, c) or dfs(i + 1, r, c - 1) or dfs(i + 1, r + 1, c) or dfs(i + 1, r, c + 1)
            visited[r][c] = False
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                    return True
        
        return False