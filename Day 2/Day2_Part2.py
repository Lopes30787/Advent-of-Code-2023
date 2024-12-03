file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2023\\Day 2\\Day2.txt', 'r')

result = 0

for line in file:
    game_number = ""
    i = 0
    number = ""
    valid = True

    max_red = 0
    max_green = 0
    max_blue = 0

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
            if int(number) > max_blue:
                max_blue = int(number)
            i += 3
            number = ""
            
        elif line[i] == "g":
            if int(number) > max_green:
                max_green = int(number)
            i += 4
            number = ""

        elif line[i] == "r":
            if int(number) > max_red:
                max_red = int(number)
            i += 2
            number = ""
        
        i += 1
    
    if valid:
        result += max_red * max_blue * max_green

print(result)