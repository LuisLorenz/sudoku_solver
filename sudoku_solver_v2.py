def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == -1:
                return (row, col)
    return None  # No empty spots


def is_valid(board, position, num):
    row, col = position

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(len(board))]:
        return False

    # Check 3x3 square
    square_row = row // 3 * 3
    square_col = col // 3 * 3
    for i in range(square_row, square_row + 3):
        for j in range(square_col, square_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # Solved
        # the first True return
    row, col = empty

    for num in range(1, 10):  # Numbers 1-9
        if is_valid(board, (row, col), num):
            board[row][col] = num  # Place the number

            if solve(board):  # Recurse
                return True
                # the second True return
                # returns until the out of the func

                # the next empty is filled 
                # is there is no option with the placed num then the solution must be different



            board[row][col] = -1  # Undo (backtrack)
                # as a result set it to -1
                # then the next letter is tried: 2 for the spot 
                # at starting with any position and going through all the options in that structure 
                #   lead to the solution if there is one 

                # it is important to set it back to -1
                # when the number is invalid reset the board
                # when all the numbers from 1-9 are invalid 
                #   move one layer back and mark e.g. 1 as invalid and go in the iteration with 2 

    return False  # Trigger backtracking
    # then the algo has run completely through and there was not solution the last return is False



# Example board
example_board = [
    [3, 9, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    [-1, -1, -1, 7, 1, 9, -1, 8, -1],
    [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    [2, -1, 6, -1, -1, 3, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],
    [5, -1, -1, -1, -1, -1, -1, -1, -1],
    [6, 7, -1, 1, -1, 5, -1, 4, -1],
    [1, -1, 9, -1, -1, -1, 2, -1, -1]
]

example_board_False = [
    [3, 3, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    [-1, -1, -1, 7, 1, 9, -1, 8, -1],
    [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    [2, -1, 6, -1, -1, 3, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],
    [5, -1, -1, -1, -1, -1, -1, -1, -1],
    [6, 7, -1, 1, -1, 5, -1, 4, -1],
    [1, -1, 9, -1, -1, -1, 2, -1, -1]
]

# Solve and print
def solver(board): 
    if solve(board):
        # true returns the last time 

        # the board is mutable 
        # the algo makes changes to the board 
        for row in example_board:
            print(row)
    else:
        print("No solution exists")
        # return False

solver(example_board_False) # No solution exists

solver(example_board)
    # [3, 9, 1, 8, 5, 6, 4, 2, 7]
    # [8, 6, 7, 2, 3, 4, 9, 1, 5]
    # [4, 2, 5, 7, 1, 9, 6, 8, 3]
    # [7, 5, 4, 9, 6, 8, 1, 3, 2]
    # [2, 1, 6, 4, 7, 3, 5, 9, 8]
    # [9, 3, 8, 5, 2, 1, 7, 6, 4]
    # [5, 4, 3, 6, 9, 2, 8, 7, 1]
    # [6, 7, 2, 1, 8, 5, 3, 4, 9]
    # [1, 8, 9, 3, 4, 7, 2, 5, 6]