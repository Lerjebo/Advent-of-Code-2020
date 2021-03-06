# x = 0, y = 0 top left corner
#every move is x+3 and y+1
import math
def tree_watch(data, x_move, y_move):
    x = 0
    y = 0
    trees = 0
    grid = data.copy()
    while y < len(data)-1:
        x += x_move
        y += y_move
        times = math.ceil(x/(len(grid[y])-1))
        grid[y] = data[y]*times
        if grid[y][x] == '#':
            trees += 1
    return trees







file = open(r'C:\Python\Advent_of_code_2020\Day3.txt')
text = file.read()
rows = text.split('\n')
print("3.1: ", tree_watch(rows, 3, 1))
total_trees = tree_watch(rows, 1, 1)*tree_watch(rows, 3, 1)*tree_watch(rows, 5, 1)*tree_watch(rows, 7, 1)*tree_watch(rows, 1, 2)
print("3.2: ", total_trees)
