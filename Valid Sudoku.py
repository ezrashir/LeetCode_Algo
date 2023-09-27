# Link to submission:
    # https://leetcode.com/problems/valid-sudoku/submissions/1060533000/

# Link to problem:
    # https://leetcode.com/problems/valid-sudoku/description/


def isValidSudoku(board):
    k=0
    inx = [[0,1,2],[3,4,5],[6,7,8]]
    
    # Check blocks:
    for n in range(3):
        i_inx = inx[n]
        for m in range(3):
            j_inx = inx[m]
            sub = [board[i][j] for i in i_inx for j in j_inx if board[i][j] != '.']
            if sorted(sub) != sorted(set(sub)):
                return False
    
    # check horizontal:
    for i in range(9):
        sub = [board[i][j] for j in range(9) if board[i][j] !='.']
        if sorted(sub) != sorted(set(sub)):
                return False

    # check vertical:
    for i in range(9):
        sub = [board[j][i] for j in range(9) if board[j][i] !='.']
        if sorted(sub) != sorted(set(sub)):
                return False        
            
    return True


# Example:
board = [
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9",".",".",".",".",".","6","."]
,["1",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))