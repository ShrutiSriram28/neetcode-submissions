class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        sum_row = {i:0 for i in range(rows)}
        sum_col = {j:0 for j in range(cols)}

        for r in range(rows):
            total = 0
            for c in range(cols):
                total += grid[r][c]
            sum_row[r] = total

        for c in range(cols):
            total = 0
            for r in range(rows):
                total += grid[r][c]
            sum_col[c] = total

        comm_servers = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (sum_row[r] > 1 or sum_col[c] > 1):
                    comm_servers += 1
        
        return comm_servers
    