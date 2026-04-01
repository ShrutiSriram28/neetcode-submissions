class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # visited = set()
        q = deque()

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c, 0])
                    # visited.add([r, c, 0])

        total_count = 0
        while q:
            v = q.popleft()
            r, c, count = v[0], v[1], v[2]
            total_count = count

            if r > 0 and grid[r - 1][c] == 1: 
                grid[r - 1][c] = 2
                q.append([r - 1, c, count + 1])
            
            if c > 0 and grid[r][c - 1] == 1: 
                grid[r][c - 1] = 2
                q.append([r, c - 1, count + 1])
            
            if r < rows - 1 and grid[r + 1][c] == 1: 
                grid[r + 1][c] = 2
                q.append([r + 1, c, count + 1])
            
            if c < cols - 1 and grid[r][c + 1] == 1: 
                grid[r][c + 1] = 2
                q.append([r, c + 1, count + 1])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return total_count