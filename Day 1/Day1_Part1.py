file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2023\\Day 1\\Day1.txt', 'r')

result = 0

for line in file:
    first = ""
    last = ""

    for char in line:
        if char.isdigit():
            if first == "":
                first = char
            last = char
    
    result += int(first + last)

print(result)