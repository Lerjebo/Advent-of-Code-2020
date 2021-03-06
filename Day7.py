def outer_bags(bags, wanted):
    visited = []
    while wanted != []:
        current = wanted.pop(0)
        for key, item in bags.items():
            if current in item and key[:-1] not in visited:
                wanted.append(key[:-1])
                visited.append(key[:-1])
    return len(visited)


def inner_bags(bags, start):
    visited = {}
    while start != []:

        current = start.pop(0)
        for key, item in bags.items():
            if current[2:-2] in key:
                contained = item.split(", ")
                visited[current[2:]] = contained
                for bag in contained:
                    start.append(bag)

    return(recursive(visited, "iny gold bag") - 1)


def recursive(path, head):
    total = 1
    if head not in path:
        return total
    for item in path[head]:
        if item[0].isdigit():
            total += int(item[0]) * recursive(path, item[2:])

        elif item == "no other bags.":
            return 1

    return total


file = open(r'C:\Python\Advent_of_code_2020\Day7.txt')
text = file.read()
rows = text.split('\n')

bags = {}
wanted_bag = ["shiny gold bag"]
for row in rows:
    key, item = row.split(" contain ")
    bags[key] = item
    #print(bags)

print("potential outer bags: ", outer_bags(bags, wanted_bag.copy()))
print("bags inside a shiny gold bag: ", inner_bags(bags, wanted_bag.copy()))