class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {i: [] for i in range(len(board))}
        colMap = {i: [] for i in range(len(board[0]))}
        squareMap = {i: [] for i in range(len(board))}
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != ".":
                    if board[r][c] in rowMap[r] or board[r][c] in colMap[c] or board[r][c] in squareMap[(r//3)*3+(c//3)]:
                        print(r,c,board[r][c])
                        return False
                    rowMap[r].append(board[r][c])
                    colMap[c].append(board[r][c])
                    squareMap[(r//3)*3+(c//3)].append(board[r][c])
        return True
                    
    # [036]
    # [147]
    # [258]

    # [ 
    # [1 2 . . 3 . . . .]
    # [4 . . 5 . . . . .]
    # [. 9 8 . . . . . 3]
    # [. . . . . . . . .]
    # [. . . . . . . . .]
    # [. . . . . . . . .]
    # [. . . . . . . . .]
    # [. . . . . . . . .]
    # [. . . . . . . . .]
    # ]