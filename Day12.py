

def navigation(data, direction, waypoint=[0, 0], part1=True):
    north = 0
    east = 0
    for instruction in data:
        if instruction[0] == "R" or instruction[0] == "L":
            direction, waypoint = rotate(instruction, direction, waypoint)
        elif part1:
            east, north = travel(instruction, east, north, direction)
        elif instruction[0] == "F":
            east, north = forward_movement(instruction, east, north, waypoint)
        else:
            waypoint = waypoint_length(instruction, waypoint)
    return (abs(north) + abs(east))


def waypoint_length(ins, waypoint):
    x_point = waypoint[0]
    y_point = waypoint[1]
    if ins[0] == "N":
        y_point += int(ins[1:])
    elif ins[0] == "E":
        x_point += int(ins[1:])
    elif ins[0] == "S":
        y_point -= int(ins[1:])
    elif ins[0] == "W":
        x_point -= int(ins[1:])
    return [x_point, y_point]


def forward_direction(direction):
    action = ""
    if direction == 0:
        action = "N"
    elif direction == 90:
        action = "E"
    elif direction == 180:
        action = "S"
    elif direction == 270:
        action = "W"
    return action

def forward_movement(ins, x, y, waypoint):
    value = ins[1:]
    x += waypoint[0]*int(value)
    y += waypoint[1]*int(value)
    return x, y





def travel(instruction, x, y, direction):
    action = instruction[0]
    value = int(instruction[1:])
    if action == "F":
        action = forward_direction(direction)
    if action == "E":
        x += value
    elif action == "W":
        x -= value
    elif action == "N":
        y += value
    elif action == "S":
        y -= value

    return x, y


def rotate(ins, dir, waypoint):
    action = ins[0]
    value = int(ins[1:])
    way = waypoint

    rotations = int(value/90)
    for i in range(0, rotations):
        if action == "R":
            dir += 90
            dir = dir % 360
            way = [way[1], -way[0]]
        elif action == "L":
            dir -= 90
            dir = dir % 360
            way = [-way[1],way[0]]
    return dir, way

file = open(r'C:\Python\Advent_of_code_2020\Day12.txt')
text = file.read()
rows = text.split('\n')
start_direction = 90
print("With the old rules our manhattan distance is: ", navigation(rows, start_direction))
print("With the new rules our manhattan distance is: ", navigation(rows, start_direction, [10, 1], False))