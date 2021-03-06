
def halting(data):
    accumulator = 0
    visited = []
    execution = 0
    jump = 0
    while True:
        instruction = data[execution]
        if execution not in visited:
            visited.append(execution)
        else:
            break
        command, value = instruction.split(" ")
        value = int(value)
        if command == "jmp":
            execution += value
        elif command == "acc":
            accumulator += value
            execution += 1
        elif command == "nop":
            execution += 1
    return accumulator


def iterating(data):
    accumulator = 0
    visited = []
    execution = 0
    while True:
        if execution >= len(data):
            return accumulator
        instruction = data[execution]
        if execution not in visited:
            visited.append(execution)
        else:
            break
        command, value = instruction.split(" ")
        value = int(value)
        if command == "jmp":
            execution += value
        elif command == "acc":
            accumulator += value
            execution += 1
        elif command == "nop":
            execution += 1
    return 0


def corruption(data):
    for count, info in enumerate(data):
        x = data.copy()
        accumulator = 0
        instruction, value = info.split(" ")
        if instruction == "nop":
            x[count] = "jmp " + value
            accumulator = iterating(x)
        elif instruction == "jmp":
            x[count] = "nop " + value
            accumulator = iterating(x)
        if accumulator != 0:
            break

    return accumulator


file = open(r'C:\Python\Advent_of_code_2020\Day8.txt')
text = file.read()
rows = text.split('\n')
print("accumulator when program getting halted: ", halting(rows))
print(corruption(rows))


