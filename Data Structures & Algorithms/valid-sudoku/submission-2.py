class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                row[r] = row.get(r, [])
                if board[r][c] in row[r]:
                    return False
                else:
                    row[r].append(board[r][c])
                
                col[c] = col.get(c, [])
                if board[r][c] in col[c]:
                    return False
                else:
                    col[c].append(board[r][c])
                
                box[(r//3, c//3)] = box.get((r//3, c//3), [])
                if board[r][c] in box[(r//3, c//3)]:
                    return False
                else:
                    box[(r//3, c//3)].append(board[r][c])

        return True