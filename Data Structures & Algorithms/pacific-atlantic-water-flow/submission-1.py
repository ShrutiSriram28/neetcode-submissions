class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        both = []
        pacific = []
        atlantic = []

        def dfs(r, c, prev_height, visited):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or heights[r][c] < prev_height:
                return
            visited.append((r, c))
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)

        for r in range(rows):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, cols - 1, heights[r][cols - 1], atlantic)
        
        for c in range(cols):
            dfs(0, c, heights[0][c], pacific)
            dfs(rows - 1, c, heights[rows - 1][c], atlantic)

        for i in pacific:
            if i in atlantic:
                both.append(i)

        return both