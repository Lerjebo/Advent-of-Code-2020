import math

def limit(data, limit):
    if limit == "R" or limit == "B":
        return [data[0] + math.ceil((data[1] - data[0]) / 2), data[1]]
    else:
        return [data[0], data[1] - math.ceil((data[1] - data[0]) / 2)]


def seat_id(data):
    row_data = data[:7]
    seat_data = data[-3:]
    row = [0, 127]
    seat = [0, 7]
    for letter in row_data:
        row = limit(row, letter)
    for letter in seat_data:
        seat = limit(seat, letter)

    return row[0]*8+seat[0]


file = open(r'C:\Python\Advent_of_code_2020\Day5.txt')
text = file.read()
rows = text.split('\n')
id = []
our_seat = []
for row in rows:
    id.append(seat_id(row))
    if row[:7] != "BBBBBBB" or row[:7] != "FFFFFFF":
        our_seat.append(id[-1])

id.sort(reverse=True)
print("highest seat ID: ", id[0])

our_seat.sort(reverse=True)
compare1 = our_seat.pop(0)
while our_seat != []:
    compare2 = our_seat.pop(0)
    if abs(compare1 -compare2) > 1:
        print("our seat ID: ", compare2+1)
        break
    compare1 = compare2