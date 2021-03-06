def seating(data):
    current_state = data.copy()
    prev_state = []
    i = 0
    tot = 0
    while current_state != prev_state:
        prev_state = current_state
        if i % 2 == 0:
            current_state = occupy(prev_state)
        else:
            current_state, tot = clear(prev_state)
        i += 1
    return tot


def seating2(data):
    current_state = data.copy()
    prev_state = []
    i = 0
    tot = 0
    while current_state != prev_state:
        prev_state = current_state
        if i % 2 == 0:
            current_state = occupy(prev_state, False)
        else:
            current_state, tot = clear(prev_state, 1)
        i += 1
    return tot

def clear(data, part1=0):
    prev_state = data
    next_state = []
    neigh = []
    tot_count = 0
    for r, row in enumerate(prev_state):
        next_row = []
        for c, col in enumerate(row):
            if col == "#":
                if part1 == 0:
                    neigh = check_neighbors(prev_state, r, c)
                else:
                    neigh = next_neighbor(prev_state, [r, c])
                count = ''.join(neigh).count("#")
                if count >= 4+part1:
                    next_row.append("L")
                else:
                    tot_count += 1
                    next_row.append(col)
            else:
                next_row.append(col)
        next_state.append(next_row)
    return next_state, tot_count

def occupy(data, part1=True):
    prev_state = data
    next_state = []
    neigh = []
    for r, row in enumerate(prev_state):
        next_row = []
        for c, col in enumerate(row):
            if col == "L":
                if part1:
                    neigh = check_neighbors(prev_state, r, c)
                else:
                    neigh = next_neighbor(prev_state, [r, c])
                if "#" not in neigh:
                    next_row.append("#")
                else:
                    next_row.append(col)
            else:
                next_row.append(col)
        next_state.append(next_row)
    return next_state

def check_neighbors(data, row, col):
    neighbors = []

    if row > 0:
        neighbors.append(data[row - 1][col])
        if col > 0:
            neighbors.append(data[row - 1][col - 1])
        if col < len(data[row])-1:
            neighbors.append(data[row - 1][col + 1])
    if row < len(data)-1:
        neighbors.append(data[row + 1][col])
        if col > 0:
            neighbors.append(data[row + 1][col - 1])
        if col < len(data[row])-1:
            neighbors.append(data[row + 1][col + 1])
    if col > 0:
        neighbors.append(data[row][col - 1])
    if col < len(data[row])-1:
        neighbors.append(data[row][col + 1])
    return neighbors



def locate_neighbor(data, y, x, y1, x1):
    x += x1
    y += y1
    if x < 0 or x > len(data[0])-1 or y < 0 or y > len(data)-1:
        return ""
    while data[y][x] == ".":
        x += x1
        y += y1
        if x < 0 or y > len(data)-1 or y < 0 or x > len(data[0])-1:
            return ""
    return data[y][x]

def next_neighbor(data, coord):
    steps = [[1, 0], [1, -1], [1, 1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1]]
    neighbors = []
    for step in steps:
        neighbors.append(locate_neighbor(data, coord[0], coord[1], step[0], step[1]))
    return neighbors





file = open(r'C:\Python\Advent_of_code_2020\Day11.txt')
text = file.read()
rows = text.split('\n') #[row][col]
#print(len(rows))
print(seating(rows), "seats were occupied in the end")
print(seating2(rows), "seats were occupied in the end with the new rules")