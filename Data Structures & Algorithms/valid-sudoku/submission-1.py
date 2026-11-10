class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for i in range(1,10):
            rows[i] = []
            cols[i] = []
            squares[i] = []
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    
                    if val in rows[i+1]:
                        return False
                    else:
                        rows[i+1].append(val)
                    
                    if val in cols[j+1]:
                        return False
                    else: 
                        cols[j+1].append(val)
                    
                    square_num = (i//3) * 3 + j//3 + 1
                    if val in squares[square_num]:
                        return False
                    else:
                        squares[square_num].append(val)
        
        return True

                    