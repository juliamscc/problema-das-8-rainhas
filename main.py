countSolutions = 0


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def validateSolution(rows):
    for i in range(8):
        x = i
        y = rows[i]
        xx = x
        yy = y
        while (True):
            xx += 1
            yy -= 1
            if (xx > 7 or yy < 0):
                break
            if (yy == rows[xx]):
                return False
        xx = x
        yy = y
        while (True):
            xx -= 1
            yy -= 1
            if (xx < 0 or yy < 0):
                break
            if (yy == rows[xx]):
                return False
    return True


def solution(rows):
    global countSolutions
    countSolutions += 1
    print("Solucao: ", countSolutions)
    board = [['.'] * 8 for _ in range(8)]
    for i in range(8):
        x = i
        y = rows[i]
        board[y][x] = 'Q'
    for i in range(8):
        for j in range(8):
            print(f" {board[i][j]} ", end=" ")
        print('\n')


def testPermutations(rows, n):
    if (n == 8):
        if (validateSolution(rows)):
            solution(rows)
    else:
        i = n
        while (i < 8):
            swap(rows, n, i)
            testPermutations(rows, n+1)
            swap(rows, i, n)
            i += 1


def solve8queens():
    row = list(range(8))
    testPermutations(row, 0)


solve8queens()
