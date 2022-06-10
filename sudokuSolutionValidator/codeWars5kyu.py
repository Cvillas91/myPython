'''
Did I Finish my Sudoku?
Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. 
If the board is valid return 'Finished!', otherwise return 'Try again!'

Examples:
print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                  ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                  ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                  ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                  ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                  ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                  ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                  ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                  ,[8, 7, 9, 6, 4, 2, 1, 5, 3]])--> 'Finished!'

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                  ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                  ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                  ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                  ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                  ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                  ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                  ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                  ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]) --> 'Try again!'
'''

def done_or_not(board):
    # Check rows
    for i in range(0, 9):
        row = ''
        for j in range(0, 9):
            row += str(board[i][j])
        if "".join(sorted(row)) != '123456789': return 'Try again!'
            
    # Check columns
    for i in range(0, 9):
        row = ''
        for j in range(0, 9):
            row += str(board[j][i])
        if "".join(sorted(row)) != '123456789': return 'Try again!'
                     
    # Check regions upper
    box = ''
    n = 0
    for y in range(0, 3):
        m = 0
        for x in range(0, 3):
            for i in range(n, n + 3):
                for j in range(m, m + 3):
                    box += str(board[i][j])
            if "".join(sorted(box)) != '123456789': return 'Try again!'
            box = ''
            m = m + 3
        n = n + 3
    return 'Finished!'
