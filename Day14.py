
def masking(data):
    mask = ""
    mem = {}
    for row in data:
        instruction, value = row.split(" = ")
        if instruction == "mask":
            mask = value
        else:
            bin_value = format(int(value), '#038b')
            mem_pos = instruction.split("[")[1].split("]")[0]
            #print(mem_pos)
            x = to_integer(mask, bin_value[2:])
            mem[mem_pos] = x
    total = 0
    for key, item in mem.items():
        total += item

    return total



def to_integer(mask, value):
    #mask = 0
    masked_val = 0
    for i in range(len(value)):
        #print(mask[i], len(value)-1 - i)
        if value[i] == "1" and mask[i] != "0":
            masked_val += int(value[i])*pow(2, len(value)-1-i)
        elif value[i] == "0" and mask[i] != "1":
            masked_val += int(value[i]) * pow(2, len(value)-1 - i)
        elif mask[i] == "1" or mask[i] == "0":
            masked_val += int(mask[i]) * pow(2, len(value)-1 - i)
        #masked_val += int(value[i])*pow(2, len(value)-i)
    return masked_val


file = open(r'C:\Python\Advent_of_code_2020\Day14.txt')
text = file.read()
rows = text.split('\n')
print("Part1: ", masking(rows))
