class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        visited = []
        orig = image[sr][sc]
        def dfs(r, c):
            if r < 0 or c < 0 or r == row or c == col or [r, c] in visited or image[r][c] != orig:
                return
            visited.append([r, c])
            image[r][c] = color

            return dfs(r - 1, c) or dfs(r + 1, c) or dfs(r, c - 1) or dfs(r, c + 1)

        dfs(sr, sc)
        return image