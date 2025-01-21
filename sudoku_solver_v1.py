import copy


# example sudoku 
example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1], 
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

# -1 represents an empty cell 

# checking 
# row 
    # there are multiple checks 
    # if there are 1 empty spot fill in the missing number in row / square 
# iteration: through all horizontal lists, verticial list, suares
    # then repeat

rows = 9
cols = 9 

def find_empty(board):
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == -1:
                empty_spot = (row, col)
                return empty_spot
    return False
    

square_1 = [(0,0), (0,1), (0,2),  (1,0), (1,1), (1,2),  (2,0), (2,1), (2,2)]

square_2 = [(0,4), (0,5), (0,6),  (1,4), (1,5), (1,6),  (2,4), (2,5), (2,6)]

square_3 = [(0,7), (0,8), (0,9),  (1,7), (1,8), (1,9),  (2,7), (2,8), (2,9)]

square_4 = [(4,0), (4,1), (4,2),  (5,0), (5,1), (5,2),  (6,0), (6,1), (6,2)]

square_5 = [(4,4), (4,5), (4,6),  (5,4), (5,5), (5,6),  (6,4), (6,5), (6,6)]

square_6 = [(4,7), (4,8), (4,9),  (5,7), (5,8), (5,9),  (6,7), (6,8), (6,9)]

square_7 = [(7,0), (7,1), (7,2),  (8,0), (8,1), (8,2),  (9,0), (9,1), (9,2)]

square_8 = [(7,4), (7,5), (7,6),  (8,4), (8,5), (8,6),  (9,4), (9,5), (9,6)] 

square_9 = [(7,7), (7,8), (7,9),  (8,7), (8,8), (8,9),  (9,7), (9,8), (9,9)]


def is_valid(board, empty_spot, num): 
    row, col = empty_spot

    # check row
    if num in board[row]: 
        return False

    # colum
    col_list = []
    col_list.clear()
    for row in range(rows):
        col_list.append(board[row][col])

    # check col
    if num in col_list: 
        return False
    
    # square
    square = None
    if (empty_spot) in square_1:
        square = square_1
    elif (empty_spot) in square_2:
        square = square_2
    elif (empty_spot) in square_3:
        square = square_3
    elif (empty_spot) in square_4:
        square = square_4
    elif (empty_spot) in square_5:
        square = square_5
    elif (empty_spot) in square_6:
        square = square_6
    elif (empty_spot) in square_7:
        square = square_7
    elif (empty_spot) in square_8:
        square = square_8
    elif (empty_spot) in square_9:
        square = square_9
    
    # square_list
    square_list = []
    square_list.clear()
    for elements in square:
        r, c = elements
        square_list.append(board[r][c])

    # check 3x3
    if num in square_list:
        return False
    return True 


def recursive_solving():
    empty_spot = find_empty(board_copy)
    row, col = empty_spot
    # set num in empty spot
    for num in range(10): # number from 1-9 
        if is_valid(board_copy, empty_spot, num) == True:
            board_copy[row][col] = num
            return True 
        else: 
            return False # not valid

while find_empty(board_copy) != False: 
    board_copy = copy.deepcopy(example_board)
    if recursive_solving() == True:
        recursive_solving()
    elif recursive_solving() == False:
        # 
        recursive_solving() # remove the latest move and go a different path

def game(): 
    # intro

    while True: 
        # input
        unsolved_board = input('Please insert your unsolved sudoku: ')

        # valide board
        if is_valid(unsolved_board) == True:
            break
        else:
            print('The input sudoku is invalid. Please insert again.')


    solution = recursive_solving() 
    print(solution)
    print('The Sudoku has been solved')
        