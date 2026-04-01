class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c, area):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r - 1, c, area + 1) + dfs(r, c - 1, area + 1) + dfs(r + 1, c, area + 1) + dfs(r, c + 1, area + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c, 0))
        
        return max_area
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not grid:
        #     return 0

        # rows = len(grid)
        # cols = len(grid[0])

        # island_area = 0

        # visited = set()

        # def bfs(r, c):
        #     q = deque()
        #     q.append([r, c])
        #     while q:
        #         v = q.popleft()
                
        #         visited.add(tuple(v))
                    
        #         if (v[0] < rows - 1) and (grid[v[0] + 1][v[1]] == 1) and (tuple([v[0] + 1, v[1]]) not in visited):
        #             q.append([v[0] + 1, v[1]])
        #         if (v[1] < cols - 1) and (grid[v[0]][v[1] + 1] == 1) and (tuple([v[0], v[1] + 1]) not in visited):
        #             q.append([v[0], v[1] + 1])
        #         if (v[0] > 0) and (grid[v[0] - 1][v[1]] == 1) and (tuple([v[0] - 1, v[1]]) not in visited):
        #             q.append([v[0] - 1, v[1]])
        #         if (v[1] > 0) and (grid[v[0]][v[1] - 1] == 1) and (tuple([v[0], v[1] - 1]) not in visited):
        #             q.append([v[0], v[1] - 1])

        # prev_area = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1 and tuple([r, c]) not in visited:
        #             bfs(r, c)
        #             area = len(visited)
        #             island_area = max(island_area, area - prev_area)
        #             prev_area = area
        
        # return island_area