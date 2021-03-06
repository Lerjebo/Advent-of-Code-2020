

def sumerizing_counts(data):

    group = ""
    sum = 0
    for row in rows:
        if row != "":
            group = group + row
        else:
            sum += len(set(group))
            group = ""
    sum += len(set(group))
    return sum

def sumerizing_counts2(data):
    group = ""
    sum = 0
    for row in rows:
        if group == "":
            group = row
        elif row != "":
            group = set(group).intersection(row)
        else:
            sum += len(set(group))
            group = ""
    sum += len(set(group))
    return sum

file = open(r'C:\Python\Advent_of_code_2020\Day6.txt')
text = file.read()
rows = text.split('\n')

print("total amount of different yeses ", sumerizing_counts(rows))
print("total amount of questions every person in a group said yes to ", sumerizing_counts2(rows))