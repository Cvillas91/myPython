def valid_solution(board):
    board2 = draw_board(board)
    board3 = draw_board(board)
    board4 = draw_board(board)
    
    #First check --- Rows
    for i in range(0,8):
        if valid_array(board2[i]) == False:
            return False
    
    #Second check --- Columns
    for i in range(0,9):
        vector = []
        for j in range(0,9):
            vector.append(board3[j][i])
        if valid_array(vector) == False:
            return False

    #Third check --- 3x3 sub grids
    vector = []
    for i in range(0,3):
        for j in range(0,3):
            vector = []
            for k in range(0,3):
                for l in range (0,3):
                    vector.append(board4[i*3+k][j * 3 + l])
            print(vector)
            if valid_array(vector) == False:
                return False

    return True

def valid_array(vector):
    vector_aux = vector
    vector_aux.sort()
    return True if vector_aux == [1, 2, 3, 4, 5, 6, 7, 8, 9] else False

def draw_board(board):
    board2 =[]
    for i in range(0,9):
        vector = []
        for j in range(0,9):
            vector.append(board[i][j])
        board2.append(vector)
    return board2



print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
