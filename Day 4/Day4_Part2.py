file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2023\\Day 4\\Day4.txt', 'r')

result = 0
number = ""

scratches = [0] * len(file.readlines())

file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2023\\Day 4\\Day4.txt', 'r')

for line in file:
    i = 0
    winners = 0
    winning = []
    scratch_number = ""
    number = ""
    points = 0

    while True:
        if line[i] == ":":
            break
        elif line[i].isdigit():
            scratch_number += line[i]
        i += 1

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
                    winners += 1
                    scratches[int(scratch_number) + winners - 1] += scratches[int(scratch_number)-1] + 1
                    result += scratches[int(scratch_number)-1] + 1
            number = ""
        
        i += 1

    result += 1

print(result)