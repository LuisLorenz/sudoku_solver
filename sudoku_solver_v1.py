
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

# checking 
# row 
    # there are multiple checks 
    # if there are 1 empty spot fill in the missing number in row / square 
# iteration: through all horizontal lists, verticial list, suares
    # then repeat

def is_valid(): 
    pass 

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