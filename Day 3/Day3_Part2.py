file = open('C:\\Users\\afons\\Ambiente de Trabalho\\Advent of Code 2023\\Day 3\\Day3.txt', 'r')

result = 0
array = []

for line in file:
    line_array = []

    for char in line:
        if char.isdigit():
            line_array += char
        elif char == "*":
            line_array += char
        elif char != "\n":
            line_array += "."
    
    array += [line_array,]

def get_number(i,j):
    number = array[i][j]
    
    k = 1
    while j+k < len(array[i]):
        if array[i][j+k].isdigit():
            number += array[i][j+k]
            k += 1
        
        else:
            break
    
    k = 1
    while j-k >= 0:
        if array[i][j-k].isdigit():
            number = array[i][j-k] + number
            k += 1
        
        else:
            break

    return [int(number),]

def search_gear(i,j):
    valid = False
    numbers = []

    # Search for numbers on top 
    if i > 0:
        top_left = False
        top_up = False
        top_right = False

        if j+1 < len(array[i]):
            if array[i-1][j+1].isdigit():
                top_right = True
        if j > 0:
            if array[i-1][j-1].isdigit():
                top_left = True
        if array[i-1][j].isdigit():
            top_up = True

        if top_left and top_right and top_up:
            numbers += get_number(i-1, j-1)
        
        elif top_left and top_right:
            numbers += get_number(i-1, j-1)
            numbers += get_number(i-1, j+1)
        
        elif top_left and top_up:
            numbers += get_number(i-1, j-1)
        
        elif top_right and top_up:
            numbers += get_number(i-1, j)
        
        elif top_right:
            numbers += get_number(i-1, j+1)
        
        elif top_left:
            numbers += get_number(i-1, j-1)
        
        elif top_up:
            numbers += [int(array[i-1][j]),]

    if j+1 < len(array[i]):
        if array[i][j+1].isdigit():
            numbers += get_number(i, j+1)
    
    if j > 0:
        if array[i][j-1].isdigit():
            numbers += get_number(i, j-1)

    # Search for numbers on bottom 
    if i+1 < len(array):
        down_left = False
        down_down = False
        down_right = False

        if j+1 < len(array[i+1]):
            if array[i+1][j+1].isdigit():
                down_right = True
        if j > 0:
            if array[i+1][j-1].isdigit():
                down_left = True
        if array[i+1][j].isdigit():
            down_down = True

        if down_left and down_right and down_down:
            numbers += get_number(i+1, j-1)
        
        elif down_left and down_right:
            numbers += get_number(i+1, j-1)
            numbers += get_number(i+1, j+1)
        
        elif down_left and down_down:
            numbers += get_number(i+1, j-1)
        
        elif down_right and down_down:
            numbers += get_number(i+1, j)
        
        elif down_right:
            numbers += get_number(i+1, j+1)
        
        elif down_left:
            numbers += get_number(i+1, j-1)
        
        elif down_down:
            numbers += [int(array[i+1][j]),]

    if len(numbers) == 2:
        valid = True

    return valid, numbers

i = 0

while i < len(array):
    j = 0
    
    while j < len(array[i]):

        if array[i][j] == "*":
            
            valid, numbers = search_gear(i,j) 

            if valid:
                result += numbers[0] * numbers[1]

        j += 1
    i += 1


print(result)