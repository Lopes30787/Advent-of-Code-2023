file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2023\\Day 2\\Day2.txt', 'r')

result = 0

for line in file:
    game_number = ""
    i = 0
    number = ""
    valid = True

    while True:
        if line[i] == ":":
            break
        elif line[i].isdigit():
            game_number += line[i]
        i += 1

    while i < len(line):
        if line[i].isdigit():
            number += line[i]
        
        elif line[i] == "b":
            if int(number) > 14:
                valid = False
                break
            i += 3
            number = ""
            
        elif line[i] == "g":
            if int(number) > 13:
                valid = False
                break
            i += 4
            number = ""

        elif line[i] == "r":
            if int(number) > 12:
                valid = False
                break
            i += 2
            number = ""
        
        i += 1
    
    if valid:
        result += int(game_number)

print(result)