file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2023\\Day 1\\Day1.txt', 'r')

result = 0

for line in file:
    first = ""
    last = ""

    for i in range(len(line)):
        if line[i].isdigit():
            if first == "":
                first = line[i]
            last = line[i]
        
        elif line[i] == "o" and len(line) > i+1:
            if line[i+1] == "n" and line[i+2] == "e":
                if first == "":
                    first = "1"
                last = "1"

        elif line[i] == "t":
            if len(line) > i+1:
                if line[i+1] == "w" and line[i+2] == "o":
                    if first == "":
                        first = "2"
                    last = "2"

            if len(line) > i+3:
                if line[i+1] == "h" and line[i+2] == "r" and line[i+3] == "e" and line[i+4] == "e":
                    if first == "":
                        first = "3"
                    last = "3"
        
        elif line[i] == "f" and len(line) > i+2:
            if line[i+1] == "o" and line[i+2] == "u" and line[i+3] == "r":
                if first == "":
                    first = "4"
                last = "4"

            elif line[i+1] == "i" and line[i+2] == "v" and line[i+3] == "e":
                if first == "":
                    first = "5"
                last = "5"

        elif line[i] == "s":
            if len(line) > i+1:
                if line[i+1] == "i" and line[i+2] == "x":
                    if first == "":
                        first = "6"
                    last = "6"
            if len(line) > i+3:
                if line[i+1] == "e" and line[i+2] == "v" and line[i+3] == "e" and line[i+4] == "n":
                    if first == "":
                        first = "7"
                    last = "7"

        elif line[i] == "e" and len(line) > i+3:
            if line[i+1] == "i" and line[i+2] == "g" and line[i+3] == "h" and line[i+4] == "t":
                if first == "":
                    first = "8"
                last = "8"

        elif line[i] == "n" and len(line) > i+2:
            if line[i+1] == "i" and line[i+2] == "n" and line[i+3] == "e":
                if first == "":
                    first = "9"
                last = "9"
    
    result += int(first + last)

print(result)