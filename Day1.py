def calculating(numbers):
    for num in numbers:
        for num2 in numbers:
            for num3 in numbers:
                if num + num2 + num3== 2020:
                    return num*num2*num3


file = open(r'C:\Python\Advent_of_code_2020\Day1.txt')
text = file.read()
numbers = text.split('\n')
numbers = list(map(int, numbers))
#print(numbers)
print(calculating(numbers))