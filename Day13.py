import numpy as np
#from sympy.btheory.modular import crt
def closest_bus(time, buses):
    bus_timing = {}
    for bus in buses:
        tot_time = 0
        start_time = bus
        while tot_time < time:
            tot_time += start_time
            bus_timing[bus] = tot_time
    sorted_bus = sorted(bus_timing.items(), key=lambda x: x[1])
    return (sorted_bus[0][1]-time)*sorted_bus[0][0]


#chinese remainder theorem
#https://www.youtube.com/watch?v=zIFehsBHB8o
def sequence(buses):
    modulo = []
    remainder = []
    for i in range(len(buses)):
        if buses[i].isdigit():
            modulo.append(int(buses[i]))
            remainder.append(modulo[-1]-i)

    print(remainder)
    print(modulo)
    N = 1
    for mod in modulo:
        N = N*mod
    Ni = []
    xi = []
    for n in modulo:
        ni = int(N/n)
        Ni.append(ni)
        xi.append(pow(ni, -1, n)) #mod inverse
    total = 0
    for index in range(len(modulo)):
        total += xi[index]*Ni[index]*remainder[index]

    return int(total % N)


file = open(r'C:\Python\Advent_of_code_2020\Day13.txt')
text = file.read()
rows = text.split('\n')
time = int(rows[0])
buses = rows[1].split(",")
buses_no_x = [int(x) for x in buses if not "x" in x]
print("minutes we have to wait times bus ID: ", closest_bus(time, buses_no_x))
print("Earliest time they follow the correct sequence: ", sequence(buses))