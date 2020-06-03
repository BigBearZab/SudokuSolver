#this is the way of checking the sudoku is complete

import numpy as np

def array_check(comp_sudoku):
  comp_sudoku = np.array(comp_sudoku)
  print(comp_sudoku)
  counter = 0
  l = set(range(1,10))
  for i in range(9):
    if set(comp_sudoku[i]) == l:
      #print(f'Row {i+1} is correct')
      counter +=1
    else:
      print(f'Row {i+1} is incorrect')
  for i in range(9):
    if set(comp_sudoku[:,i]) == l:
      #print(f'Column {i+1} is correct')
      counter += 1
    else:
      print(f'Column {i+1} is incorrect')
  sq1 = comp_sudoku[0:3,0:3]
  sq2 = comp_sudoku[0:3,3:6]
  sq3 = comp_sudoku[0:3,6:9]
  sq4 = comp_sudoku[3:6,0:3]
  sq5 = comp_sudoku[3:6,3:6]
  sq6 = comp_sudoku[3:6,6:9]
  sq7 = comp_sudoku[6:9,0:3]
  sq8 = comp_sudoku[6:9,3:6] 
  sq9 = comp_sudoku[6:9,6:9]
  list_of_sqs = [sq1,sq2,sq3,sq4,sq5,sq6,sq7,sq8,sq9]
  for square in list_of_sqs:
    if set(square.flatten()) == l:
      #print(f'Square {square} is correct')
      counter += 1
    else:
      print(f'Square {square} is incorrect')
  
  if counter == 27:
    print('Woo you solved it!')
