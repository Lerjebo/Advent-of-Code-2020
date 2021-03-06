
def xmas(data, preemble, part1 = True):
    for first_non_preemble in range(len(data)-1):
        found = False
        for i in range(first_non_preemble, first_non_preemble+preemble):
            wanted = str(int(data[first_non_preemble+preemble]) - int(data[i]))
            if wanted in data[first_non_preemble:first_non_preemble+preemble]:
                found = True
                break
        if not found and part1:
            return data[first_non_preemble+preemble]
        elif not found and not part1:
            return first_non_preemble+preemble
    return -1


def adding(data, preemble):
    max = xmas(data, preemble, part1=False)
    #print(max)
    wanted = int(data[max])
    for i in range(max):
        smallest, biggest = wanted, 0
        current = 0
        x = i
        while current < wanted:# and x < len(data):
            if int(data[x]) > biggest:
                biggest = int(data[x])
            if int(data[x]) < smallest:
                smallest = int(data[x])
            current += int(data[x])
            x += 1
        if current == wanted:
            return biggest + smallest

    return -1


file = open(r'C:\Python\Advent_of_code_2020\Day9.txt')
text = file.read()
rows = text.split('\n')

print("First non valid number: ",xmas(rows, 25))
print("Sum of the largest and smallest number of the sequence that added to the non valid number: ", adding(rows, 25))

