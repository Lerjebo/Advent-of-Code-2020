def password_debug1(data):
    valid_password = 0
    for row in data:
        splitted = row.split(":")
        min = int((splitted[0].split("-"))[0])
        max = int((splitted[0].split("-"))[1].split(" ")[0])
        specific_letter = splitted[0][-1]
        counter = 0
        for letter in splitted[1]:
            if letter == specific_letter:
                counter += 1
        if counter >= min and counter <= max:
            valid_password += 1
    return valid_password

def password_debug2(data):
    valid_passowrd = 0
    for row in data:
        splitted = row.split(":")
        index1 = int((splitted[0].split("-"))[0])
        index2 = int((splitted[0].split("-"))[1].split(" ")[0])
        specific_letter = splitted[0][-1]
        if (splitted[1][index1] == specific_letter or splitted[1][index2] == specific_letter) and (splitted[1][index1] != splitted[1][index2]):
            valid_passowrd += 1

    return valid_passowrd



file = open(r'C:\Python\Advent_of_code_2020\Day2.txt')
text = file.read()
rows = text.split('\n')
print(password_debug1(rows))
print(password_debug2(rows))
#numbers = list(map(int, numbers))