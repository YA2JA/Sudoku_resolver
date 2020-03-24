import inspect
import numpy as np

from functools import reduce
from random import choice, randint

def resolve(game_map) -> list:
    """This fonction is inputing only numpy array table and returning resolved sudoku table"""

    if not np.isin(0, game_map):#verify if table is completed
        return game_map

    y,x = np.where(game_map==0)
    y,x = y[0], x[0]

    values = right_numbers(game_map, x,y)#get numbers whiche are able to be insert
    
    for value in values:
        game_map[y,x] = value
        test = resolve(game_map)
        
        if not np.isin(0, test):
           return test

        game_map[y,x] = 0

    #This's the most slow part of the code, can be delet, but if you delet this part
    #and if table can't be resolved it will return input grid.
    #if verify call's recursive or not, if is it function will return game_map
    #else it will raise exception
    if inspect.stack()[1][3] == inspect.currentframe().f_code.co_name:#can delet

        return game_map#can't delet

    raise Exception("This sudoku table can not to be resolved")#can delet

def right_numbers(grid, x, y) -> list:
    """This function's returning list of all numbers whiche are able to be insert in the cell"""
    row = grid[y,:]#get list of all elemnts whiche have same row
    
    col = grid[:,x]# same for column

    sqr = grid[(y//3)*3:(3+(y//3)*3), (x//3)*3:(3+(x//3)*3)].reshape(9)#same for all elements around
    
    return np.setdiff1d(np.arange(1,10), reduce(np.union1d,(row,col,sqr)))#returning elements wiche are not in any of this 3 lists

def sudok_table_generator(N) -> list:
    """This function's creating the table and insert N numbers of random elements in random places of the table,
    random staying respect sudoku rules"""
    table = np.zeros((9,9))#(y,x)
    for i in range(N):#Much N is bigger more chance whiche table be irresolvable
        x,y = randint(0,8),randint(0,8)
        table[y,x] = choice(right_numbers(table, x, y))
    return table

def beautiful_print(to_print):
    for i in range(3):
        for j in range(3):
            for n in range(3):
                print(to_print[j+i*3][n*3:n*3+3], end = " ")
            print()
        print()

def main():
    #if you need personalized tests
    # grid = np.array([[1,5,2,1,8,9,3,0,6],
    #                  [7,3,9,2,5,6,8,0,1],
    #                  [4,6,8,3,7,1,2,0,5],
    #                  [3,8,7,1,2,4,6,0,9],
    #                  [5,9,1,7,6,3,4,0,8],
    #                  [2,4,6,8,9,5,7,0,3],
    #                  [9,1,4,6,3,7,5,0,2],
    #                  [6,2,5,9,4,8,1,0,7],
    #                  [8,7,3,5,1,2,9,0,4]])
    grid = sudok_table_generator(10)
    resolved = resolve(grid)
    beautiful_print(resolved)

if __name__ == '__main__':
    main()