#

input_str = input("Nhap dau vao: ")
print(input_str)

dimension = [int(x) for x in input_str.split(', ')]
print(dimension)

rowNum = dimension[0]
colNum = dimension[1]

multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
print(multilist)


for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col

print(multilist)