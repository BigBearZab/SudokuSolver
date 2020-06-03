#this is where the magic happens
import numpy as np

def FillOptions(GivernNumbers):
  StartingOptions = [1,2,3,4,5,6,7,8,9]
  for i in range (0,9):
      for j in range (0,9):
        if (GivernNumbers[i][j] == 0):
          GivernNumbers[i][j] = StartingOptions
  return(GivernNumbers)


def sudoku_solve(uncomplete_sudoku):
  nothing_changed = False
  counter =0
  uncomplete_sudoku = FillOptions(uncomplete_sudoku)
  while nothing_changed == False:
    nothing_changed = True
    for i in range (0,9):
      for j in range (0,9):
          if (isinstance(uncomplete_sudoku[i][j], list)):
            if(len(uncomplete_sudoku[i][j])>1):
              print(uncomplete_sudoku[i][j])
              uncomplete_sudoku[i][j] = check_system(uncomplete_sudoku,i,j)
              if(len(uncomplete_sudoku[i][j])==1):
                uncomplete_sudoku[i][j]=uncomplete_sudoku[i][j][0]
                nothing_changed = False
  return(uncomplete_sudoku)
          



def check_system(uncomplete_sudoku,i,j):
  #l_hor = uncomplete_sudoku[i]
  l_hor = [num for num in uncomplete_sudoku[i] if isinstance(num, int)==True]
  #print(l_hor)
  l_vert = [uncomplete_sudoku[x][j] for x in range(9)]
  l_vert = [num for num in l_vert if isinstance(num, int)==True]
  #print(l_vert)
  l_square = []
  #print(l_square)
  l_tot = l_hor +  l_vert
  #print(l_tot)
  rem_numbs = set([1,2,3,4,5,6,7,8,9])-set(l_tot)
  print(list(rem_numbs))
  return(list(rem_numbs))

#vert = [input_sud[x][0] for x in range(9)]  
