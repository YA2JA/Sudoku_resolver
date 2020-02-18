def resolve(game_map) -> list:
    for y in range(9):
        for x in range(9):
            if game_map[y][x] == 0:
                for i in range(1,10):
                    if autorize(game_map,x,y,i):
                        game_map[y][x] = i
                        game_map = resolve(game_map)
                        if 0 in [item for sublist in game_map for item in sublist]:
                            game_map[y][x] = 0
    return game_map

def autorize(_map,x,y,value) -> bool:
    if value in _map[y]:
        return False

    if value in [obj[x] for obj in _map]:
        return False

    x_start = (x//3)*3
    y_start = (y//3)*3
    for i in range(3):
        for j in range(3):
            if _map[y_start+i][x_start+j] == value:
                return False
    return True

def gen_grid(size_x=9, size_y=9) -> list:
    _grid_form = [[0 for i in range(size_x)] for j in range(size_y)]
    return _grid_form

def main():
    grid = [[1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, 4]]

    resolved = resolve(grid)
    for  i in resolved:
        print(i, end = ",\n")

    # beautiful_print(resolved)


def beautiful_print(to_print):
    for i in range(3):
        for j in range(3):
            for n in range(3):
                print(to_print[j+i*3][n*3:n*3+3], end = " ")
            print()
        print()

if __name__ == '__main__':
    main()