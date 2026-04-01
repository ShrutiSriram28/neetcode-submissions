class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if row.get(r, 0) == 0:
                    row[r] = [board[r][c]]
                elif board[r][c] not in row[r]:
                    row[r].append(board[r][c])
                else:
                    return False

                if col.get(c, 0) == 0:
                    col[c] = [board[r][c]]
                elif board[r][c] not in col[c]:
                    col[c].append(board[r][c])
                else:
                    return False

                if box.get((r//3, c//3), 0) == 0:
                    box[(r//3, c//3)] = [board[r][c]]
                elif board[r][c] not in box[(r//3, c//3)]:
                    box[(r//3, c//3)].append(board[r][c])
                else:
                    return False
        return True

        