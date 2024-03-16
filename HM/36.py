'''
We need 3 checking loops. 
for each loop, we are going to use a hashmap to track frequencies. 

The first loop is checking if rows are valid 
Second loop is checking if columns are valid 

Third is checking the 3x3 blocks.

The sudoku is always 9x9. We will always have 9*(3x3) blocks 

[[".",".","4",".",".",".","6","3","."]
,[".",".",".",".",".",".",".",".","."]
,["5",".",".",".",".",".",".","9","."]
,[".",".",".","5","6",".",".",".","."]
,["4",".","3",".",".",".",".",".","1"]
,[".",".",".","7",".",".",".",".","."]
,[".",".",".","5",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]]
'''
import math

def isValidSudoku(board: List[List[str]]) -> bool:
    rows = dict()
    cols = dict()
    blocks = dict()

    for i in range(len(board)):
        for j in range(len(board[i])):
            curr_cell = board[i][j]
            blockTuple = (math.floor(i/3), math.floor(j/3))
            if curr_cell != ".":
                if curr_cell in rows.get(i, []):
                    return False
                if curr_cell in cols.get(j, []):
                    return False
                if curr_cell in blocks.get(blockTuple, []):
                    return False
                
                rows[i] = rows.get(i, []) + [curr_cell]
                cols[j] = cols.get(j, []) + [curr_cell]
                blocks[blockTuple] = blocks.get(blockTuple, []) + [curr_cell]
    return True



 
