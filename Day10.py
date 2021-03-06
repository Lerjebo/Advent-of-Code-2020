def jolt_differences(input_data, part2 = False):
    add_one = 0
    add_three = 0
    data = input_data.copy()
    for index in range(len(data)-1):
        diff = data[index+1] - data[index]
        if diff == 1:
            add_one += 1
        elif diff == 3:
            add_three += 1
    return add_one*add_three


def jolt(data):
    current_data = data.copy()
    total_combinations = []
    total_combinations.append(data.copy())
    i = 0
    #j = i + 2
    x = 0
    while total_combinations != []:
        current_data = total_combinations.pop(-1)
        print(current_data)

        while current_data[i+2]-current_data[i] <= 3:
            #i += 1
            #if current_data[i+2]-current_data[i] <= 3:
            current_data.pop(i+1)
            x += 1
            total_combinations.append(current_data.copy())
        #break
        i += 1
    #print(x)
    print(total_combinations)


total_combinations = {}
def jolt_combination(data, i=0):
    if i == len(data)-1:
        return 1
    if i in total_combinations:
        return total_combinations[i]
    ans = 0
    for j in range(i+1, len(data)):
        if data[j]-data[i] <= 3:

            ans += jolt_combination(data, j)
        else:
            break

    total_combinations[i] = ans
    return ans


file = open(r'C:\Python\Advent_of_code_2020\Day10.txt')
text = file.read()
rows = text.split('\n')
numbers = [int(x) for x in rows]
numbers.append(0)
numbers.append(max(numbers)+3)
numbers.sort()
print(numbers)
print("Part1: ", jolt_differences(numbers))
print("Part2: ", jolt_combination(numbers))

