file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2023\\Day 3\\Day3.txt', 'r')

result = 0
array = []

for line in file:
    line_array = []

    for char in line:
        if char.isdigit():
            line_array += char
        elif char == ".":
            line_array += char
        elif char != "\n":
            line_array += "#"
    
    array += [line_array,]
i = 0

while i < len(array):
    j = 0
    
    while j < len(array[i]):
        number = ""
        valid = False

        if array[i][j].isdigit():
            
            number += array[i][j]

            if i > 0:
                if j > 0:
                    if array[i-1][j-1] == "#":
                        valid = True

                if j+2 <= len(array[i]):
                    if array[i-1][j+1] == "#":
                        valid = True

                if array[i-1][j] == "#":
                    valid = True

            if i+2 <= len(array):
                if j > 0:
                    if array[i+1][j-1] == "#":
                        valid = True

                if j+2 <= len(array[i]):
                    if array[i+1][j+1] == "#":
                        valid = True
                
                if array[i+1][j] == "#":
                    valid = True

            if j > 0:        
                if array[i][j-1] == "#":
                    valid = True

            if j+2 <= len(array[i]):
                if array[i][j+1] == "#":
                    valid = True
            
            while True:
                if j+2 <= len(array[i]):
                    j += 1
                    if array[i][j].isdigit():
                        number += array[i][j]
                        if not valid:
                            if j+2 <= len(array[i]):
                                if i+2 <= len(array):
                                    if array[i+1][j+1] == "#":
                                        valid = True
                                if i > 0:
                                    if array[i-1][j+1] == "#":
                                        valid = True
                                if array[i][j+1] == "#":
                                    valid = True
                    else:
                        break
                else:
                    break
            
            if valid:
                result += int(number)   

        j += 1
    i += 1


print(result)