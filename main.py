import inspect
import numpy as np

from functools import reduce
from random import choice, randint

def resolve(game_map) -> list:
    """inputing only numpy array table and returning resolved sudoku table"""
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
    if inspect.stack()[1][3] == inspect.currentframe().f_code.co_name:#if calling function's name's same that function name

        return game_map#can't delet

    raise Exception("This sudoku table can not to be resolved")

def right_numbers(grid, x, y) -> list:
    """This function's returning list of all numbers whiche are able to be insert in the cell"""
    row = grid[y,:]#get list of all elemnts whiche have same row
    
    col = grid[:,x]# same for column

    sqr = grid[(y//3)*3:(3+(y//3)*3), (x//3)*3:(3+(x//3)*3)].reshape(9)#same for all elements around
    
    return np.setdiff1d(np.arange(1,10), reduce(np.union1d,(row,col,sqr)))#returning elements wiche are not in any of this 3 lists

def sudok_table_generator(N) -> list:
    """Creating the table and insert N numbers of random elements in random places of the table,
    random staying respect sudoku rules"""
    table = np.zeros((9,9))#(y,x)
    for i in range(N):#Much N is bigger more chance whiche table be irresolvable
        x,y = randint(0,8),randint(0,8)
        table[y,x] = choice(right_numbers(table, x, y))
    return table

def beautiful_print(to_print):
    print("-"*32)
    for i in range(3):
        for j in range(3):
            for n in range(3):
                print(to_print[j+i*3][n*3:n*3+3], end = " ")
            print()
        print()
    print("-"*32)

def printExemple(data):
    print('[', end = "")
    for i in data:
        print(str(i)+",")
    print("]")

def main():
    #if you need personalized tests
    # grid = np.array([[1,1,1,0,0,0,0,0,0],
    #                  [1,0,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,0,0,0]])
    grid = sudok_table_generator(6)
    # beautiful_print(grid)
    resolved = resolve(grid)
    # beautiful_print(resolved)
    printExemple(resolved)

if __name__ == '__main__':
    main()