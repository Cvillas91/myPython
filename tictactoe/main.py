
# | | 
#-----
# | | 
#-----
# | | 

def drawField(field) :
    for row in range(5) :
        if row % 2 == 0 :
            practicalRow = int(row/2)
            for col in range(5) :
                if col % 2 == 0 :
                    practicalCol = int(col/2)
                    if col != 4 :
                        print(field[practicalCol][practicalRow], end="")
                    else : 
                        print(field[practicalCol][practicalRow])
                else :
                    print("|",end="")
        else : 
            print("-----")

Player = 1
currentField = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
drawField(currentField)

while (True):
    print("Players Turn :", Player)
    MoveRow = int(input("Please enter the row: \n"))
    MoveCol = int(input("Please enter the column: \n"))
    if Player == 1 :
        if currentField[MoveCol-1][MoveRow-1] == " " :
            currentField[MoveCol-1][MoveRow-1] = "X"
            Player = 2
    else : 
        if currentField[MoveCol-1][MoveRow-1] == " " :
            currentField[MoveCol-1][MoveRow-1] = "O"
            Player = 1
    drawField(currentField)
