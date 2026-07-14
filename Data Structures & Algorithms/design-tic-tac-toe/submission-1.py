class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.grid = [[0 for j in range(self.n)] for i in range(self.n)
        ]
        self.winner = 0

    def move(self, row: int, col: int, player: int) -> int:
        self.grid[row][col] = player
        
        # for r in range(self.n):
        #     for c in range(self.n):
        #         print(self.grid[r][c], end=' ')
        #     print()

        # checking winner along the row 
        self.winner = player
        for c in range(self.n):
            if self.grid[row][c] != player:
                self.winner = 0
                break
        if self.winner == player:
            return self.winner 

        # checking winner along the col
        self.winner = player
        for r in range(self.n):
            if self.grid[r][col] != player:
                self.winner = 0
                break
        if self.winner == player:
            return self.winner 
    
        # checking winner along the diagonal
        self.winner = player
        for i in range(self.n):
            if self.grid[i][i] != player:
                self.winner = 0
                break
        if self.winner == player:
            return self.winner 

        # checking winner along the anti diagonal
        self.winner = player
        for i in range(self.n):
            if self.grid[self.n - i - 1][i] != player:
                self.winner = 0
                break

        return self.winner

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
