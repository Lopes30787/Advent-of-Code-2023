file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2023\\Day 4\\Day4.txt', 'r')

result = 0
number = ""

for line in file:
    i = 0
    winning = []
    points = 0

    while True:
        if line[i] != ":":
            i+=1
        else:
            break
    
    while i < len(line):
        if line[i].isdigit():
            number += line[i]
        
        elif line[i] == "|":
            break

        else:
            if number != "":
                winning += [number,]
            number = ""
        
        i += 1
    
    number = ""
    while i < len(line):
        if line[i].isdigit():
            number += line[i]

        else:
            if number != "":
                if number in winning:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2
            number = ""
        
        i += 1
    
    result += points

print(result)