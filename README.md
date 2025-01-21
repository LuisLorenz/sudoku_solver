# sudoku_solver

# principle
- input a sudoku: 
    - format: nested list
- algorithm that checks:
    - in row
    - in square 
- print solution 


# valid check
- number in empty cell must not be present in row, col and 3x3 square

# plan
- find empty cell 
- try to place a num in that spot 
- recursively solve 
- backtrack it does not solve the sudoku
- so how save your tries so that you do not do it again 
