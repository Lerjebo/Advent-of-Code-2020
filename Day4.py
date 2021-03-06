def validicity(key, item):
    if key == "byr" and int(item) <= 2002 and int(item) >= 1920:
        return True
    if key == "iyr" and int(item) <= 2020 and int(item) >= 2010:
        return True
    if key == "eyr" and int(item) <= 2030 and int(item) >= 2020:
        return True
    if key == "hgt":
        if item[-2:] == "cm" and item[0:3].isdigit():
            if int(item[0:3]) >= 150 and int(item[0:3]) <= 193:
                return True
        elif item[-2:] == "in" and int(item[0:2]) >= 59 and int(item[0:2]) <= 76:
            return True
    if key == "hcl" and item[0] == "#" and len(item) == 7:
        return True
    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if key == "ecl" and item in ecl:
        return True
    #print(item[1:].isdigit(), len(item))
    if key == "pid" and item[1:].isdigit() and len(item) == 9:
        return True

    return False


def passport_check(passport):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    check = {}
    #print(passport)
    for id in passport:
        key, item = id.split(":")
        check[key] = item

    valid = 0
    for key, item in check.items():
        #print(key[:-2])
        if key in required and validicity(key, item):
           valid += 1
    if valid == 7:
        return 1
    return 0



file = open(r'C:\Python\Advent_of_code_2020\Day4.txt')
text = file.read()
rows = text.split('\n')
password = []
current = ""

#passport_check(password)
total = 0
for row in rows:
    if row.strip():
        current = current + " " + row
    else:
        total += passport_check(current[1:].split(" "))
        current = ""
total += passport_check(current[1:].split(" "))
print(total)
