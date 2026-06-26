class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            column = set()
            if i % 3 == 0:
                box1 = set()
                box2 = set()
                box3 = set()
            for j in range(9):
                rcurrent = board[i][j]
                ccurrent = board[j][i]
                if rcurrent != ".":
                    if rcurrent in row:
                        return False
                    row.add(rcurrent)
                    if j < 3:
                        if rcurrent in box1:
                            return False
                        box1.add(rcurrent)
                    elif j < 6:
                        if rcurrent in box2:
                            return False
                        box2.add(rcurrent)
                    else:
                        if rcurrent in box3:
                            return False
                        box3.add(rcurrent)
                if ccurrent != ".":
                    if ccurrent in column:
                        return False
                    column.add(ccurrent)
        return True

                
                