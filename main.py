import numpy as np
from functools import reduce


def resolve(game_map) -> list:
    if not np.isin(0, game_map):
        return game_map

    y,x =  np.where(game_map==0)
    y,x = y[0], x[0]

    values = right_numbers(game_map, x,y)
    for value in values:
        game_map[y,x] = value

        test = resolve(game_map)
        if not np.isin(0, test):
           return test

        game_map[y,x] = 0

    raise Exception("This sudoku table can not to be resolved")


def right_numbers(grid, x, y) -> list:
    row = grid[y,:]
    
    col = grid[:,x]

    sqr = grid[(y//3)*3:(3+(y//3)*3), (x//3)*3:(3+(x//3)*3)].reshape(9)
    
    return np.setdiff1d(np.arange(1,10), reduce(np.union1d,(row,col,sqr)))


def main():
    grid = np.array([[1, 0, 0, 1, 0, 0, 0, 0, 0],
                     [7, 3, 0, 2, 5, 6, 8, 4, 1],
                     [4, 6, 0, 3, 7, 1, 2, 9, 5],
                     [3, 8, 0, 1, 2, 4, 6, 5, 9],
                     [5, 9, 0, 7, 6, 3, 4, 2, 8],
                     [2, 4, 0, 8, 9, 5, 7, 1, 3],
                     [9, 1, 0, 6, 3, 7, 5, 8, 2],
                     [6, 2, 0, 9, 4, 8, 1, 3, 7],
                     [8, 7, 0, 5, 1, 2, 9, 6, 4]])

    resolved = resolve(grid)

    beautiful_print(resolved)

def beautiful_print(to_print):
    for i in range(3):
        for j in range(3):
            for n in range(3):
                print(to_print[j+i*3][n*3:n*3+3], end = " ")
            print()
        print()

if __name__ == '__main__':
    main()