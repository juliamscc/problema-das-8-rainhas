countSolutions = 0

def swap(array, a, b):
    [array[a], array[b]] = [array[b], array[a]]

def validateSolution(rows):
    for i in range(8):
        x = i
        y = rows[i]
        xx = x
        yy = y

    while(1):
        xx += 1
        yy -= 1
        if(xx > 7 or yy < 0):
            break
        if(yy == rows[xx]):
            return 0
        
    xx = x
    yy = y
    while(1):
        xx -= 1
        yy -= 1
        if(xx < 0 or yy < 0): break
        if(yy == rows[xx]):
            return 0
    return 1

def solution(rows):
    board = []
    countSolutions += 1
    print("Solução: ", countSolutions)

    for i in range(8):
        for j in range(8):
            board[i][j] = "."
    
    for i in range(8):
        x = i
        y = rows[i]
        board[y][x] = 'Q'

    for i in range(8):
        for i in range(8):
            print(' {board[i][j]} ')
        print('\n')