import numpy as np 
from checker import array_check
from solver import sudoku_solve

#complete sudoku
complete_sud =[
[5, 1, 7, 6, 9, 8, 2, 3, 4],
[2, 8, 9, 1, 3, 4, 7, 5, 6],
[3, 4, 6, 2, 7, 5, 8, 9, 1],
[6, 7, 2, 8, 4, 9, 3, 1, 5],
[1, 3, 8, 5, 2, 6, 9, 4, 7],
[9, 5, 4, 7, 1, 3, 6, 8, 2],
[4, 9, 5, 3, 6, 2, 1, 7, 8],
[7, 2, 3, 4, 8, 1, 5, 6, 9],
[8, 6, 1, 9, 5, 7, 4, 2, 3]]

#test sudoku for the solver
input_sud =[
[5, 0, 0, 6, 9, 8, 2, 3, 4],
[2, 8, 9, 1, 3, 0, 0, 5, 6],
[3, 4, 6, 2, 7, 5, 0, 9, 1],
[6, 7, 2, 0, 4, 9, 3, 0, 5],
[1, 3, 8, 5, 2, 6, 9, 4, 7],
[9, 0, 4, 7, 1, 0, 6, 8, 2],
[4, 0, 5, 3, 6, 2, 1, 7, 8],
[7, 2, 3, 4, 8, 1, 5, 6, 9],
[8, 6, 1, 9, 5, 7, 4, 2, 3]]

test_sudoku = input_sud

#array_check(test_sudoku)

sudoku_solve(input_sud)
array_check(input_sud)
#print(input_sud)
#print(test_sudoku)
